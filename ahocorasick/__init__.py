# coding:utf-8
# write by zhou
from collections import defaultdict

class Node(object):
    """
    node
    """
    def __init__(self, str='', is_root=False):
        self._next_p = {}
        self.fail = None
        self.is_root = is_root
        self.str = str
        self.parent = None

    def __iter__(self):
        return iter(self._next_p.keys())

    def __getitem__(self, item):
        return self._next_p[item]

    def __setitem__(self, key, value):
        _u = self._next_p.setdefault(key, value)
        _u.parent = self

    def __repr__(self):
        return "<Node object '%s' at %s>" % \
               (self.str, object.__repr__(self)[1:-1].split('at')[-1])

    def __str__(self):
        return self.__repr__()


class AhoCorasick(object):
    """
    Ac自动机对象
    """
    def __init__(self, *words):
        self.words_set = set(words)
        self.words = list(self.words_set)
        self.words.sort(key=lambda x: len(x))
        self._root = Node(is_root=True)
        self._node_meta = defaultdict(set)
        self._node_all = [(0, self._root)]
        _a = {}
        for word in self.words:
            for w in word:
                _a.setdefault(w, set())
                _a[w].add(word)

        def node_append(keyword):
            assert len(keyword) > 0
            _ = self._root
            for _i, k in enumerate(keyword):
                node = Node(k)
                if k in _:
                    pass
                else:
                    _[k] = node
                    self._node_all.append((_i+1, _[k]))
                if _i >= 1:
                    for _j in _a[k]:
                        if keyword[:_i+1].endswith(_j):
                            self._node_meta[id(_[k])].add((_j, len(_j)))
                _ = _[k]
            else:
                if _ != self._root:
                    self._node_meta[id(_)].add((keyword, len(keyword)))

        for word in self.words:
            node_append(word)
        self._node_all.sort(key=lambda x: x[0])
        self._make()

    def _make(self):
        """
        build ac tree
        :return:
        """
        for _level, node in self._node_all:
            if node == self._root or _level <= 1:
                node.fail = self._root
            else:
                _node = node.parent.fail
                while True:
                    if node.str in _node:
                        node.fail = _node[node.str]
                        break
                    else:
                        if _node == self._root:
                            node.fail = self._root
                            break
                        else:
                            _node = _node.fail

    def search(self, content, with_index=False):
        result = set()
        node = self._root
        index = 0
        for i in content:
            while 1:
                if i not in node:
                    if node == self._root:
                        break
                    else:
                        node = node.fail
                else:
                    for keyword, keyword_len in self._node_meta.get(id(node[i]), set()):
                        if not with_index:
                            result.add(keyword)
                        else:
                            result.add((keyword, (index - keyword_len + 1, index + 1)))
                    node = node[i]
                    break
            index += 1
        return result


if __name__ == '__main__':
    ac = AhoCorasick("abc", 'abe', 'acdabd', 'bdf', 'df', 'f', 'ac', 'cd', 'cda')
    print(ac.search('acdabdf', True))
