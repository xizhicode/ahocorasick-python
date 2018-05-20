# coding:utf-8

class Node(object):
    def __init__(self, str='', is_root=False, is_word=False):
        self.next_p = {}
        self.fail = None
        self.is_root = is_root
        self.is_word = is_word
        self.str = str
        self.parent = None
        self.branchlist = []

    def append(self, keyword):
        assert len(keyword) > 0
        _buff = self
        for k in keyword[:-1]:
            _buff[k] = Node(k)
            _buff = _buff[k]
        else:
            _buff[keyword[-1]] = Node(keyword[-1], is_word=True)

    def __iter__(self):
        return iter(self.next_p.keys())

    def __getitem__(self, item):
        return self.next_p[item]

    def __setitem__(self, key, value):
        _u = self.next_p.setdefault(key, value)
        _u.is_word = _u.is_word or value.is_word
        _u.parent = self


class AhoCorasick(object):
    def __init__(self, *words):
        self.words = words
        self._root = Node(is_root=True)
        map(self._root.append, self.words)
        self._make()

    def _get_all_parentnode(self, node, root_start=True):
        _u = []
        while node != self._root:
            node = node.parent
            if node != self._root:
                _u.append(node)
        if root_start == True:
            _u.reverse()
        return _u

    def _make(self):
        _endnodelist = []

        def _handlesun(node):
            for i in node:
                if node[i].next_p.keys() == []:
                    _endnodelist.append(node[i])
                if node == self._root:
                    pass
                else:
                    if node.fail.next_p.has_key(i):
                        node[i].fail = node.fail.next_p[i]
                    else:
                        if self._root.next_p.has_key(i):
                            node[i].fail = self._root[i]
                        else:
                            node[i].fail = self._root
                    parentlist = self._get_all_parentnode(node[i])[1:]
                    for index, j in enumerate(parentlist):
                        if self._root.next_p.has_key(j.str):
                            try:
                                _startnode = self._root
                                for _l in parentlist[index:] + [node[i]]:
                                    _startnode = _startnode.__getitem__(_l.str)
                                assert _startnode.is_word
                                node[i].branchlist.append(_startnode)
                            except Exception as e:
                                pass
                        else:
                            pass
                _handlesun(node[i])

        self._root.fail = self._root  
        for i in self._root:
            self._root[i].fail = self._root
            _handlesun(self._root[i])
        for i in _endnodelist:
            if i.str == i.parent.str and i.parent != self._root and i.fail.parent == self._root and i.parent.fail.fail != self._root \
                    and i.str in i.parent.fail.fail.next_p.keys():
                i.fail = i.parent.fail.fail[i.str]

    def search(self, content,with_index=False):
        result = set()
        node = self._root
        def match_case(node, current_index=None):
            if  current_index==None:
                current_index=index
            else:
                pass
            parent_times=0
            string = ''
            _len=-1
            while node != self._root:
                string = node.str +string
                _len+=1
                node = node.parent
                if node.is_word:
                    parent_times+=1
                    match_case(node,current_index=current_index-parent_times-1)
            if not  with_index:
                result.add(string)
            else:
                result.add((string,(current_index-_len,current_index+1)))

        index = 0
        for i in content:
            while 1:
                if node == self._root:   
                    if not  node.next_p.has_key(i):
                        break
                    else:
                        node=self._root[i]
                        if node.is_word:
                            if with_index:
                                result.add((i,(index,index+1)))
                            else:
                                result.add(i)
                        break
                else:    
                    if node.next_p.has_key(i): 
                        node = node.next_p[i]
                        if node.is_word:
                            match_case(node,current_index=index)
                            parentnode = [node]+ self._get_all_parentnode(node, False)
                            for _,m in enumerate(parentnode):
                                for n in m.branchlist:
                                    match_case(n,current_index=index-_)
                        break
                    else:  
                        parentnode=[node]+ self._get_all_parentnode(node, False)
                        for _,m in enumerate(parentnode):
                            for n in m.branchlist:
                                match_case(n,current_index=index-_)
                        node=node.fail
                        continue
            index += 1
        return result

