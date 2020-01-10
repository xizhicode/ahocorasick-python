# coding:utf-8
__author__ = "zhou"
# create by zhou on 2020/1/10

if __name__ == '__main__':
    import ahocorasick
    tree = ahocorasick.AhoCorasick("test", "book", "oo", "ok", "k")  # 构建ac自动机
    print(tree.search("test book", True))  # 检索

