# coding:utf-8
__author__ = "zhou"
# create by zhou on 2020/1/10
import ahocorasick

if __name__ == '__main__':
    ac = ahocorasick.AhoCorasick('abc', 'abe', 'acdabd', 'bdf')
    print(ac.search('acdabdf'))
