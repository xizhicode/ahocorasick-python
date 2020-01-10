# coding:utf-8
__author__ = "zhou"
# create by zhou on 2020/1/10
import ahocorasick

if __name__ == '__main__':
    ac = ahocorasick.AhoCorasick('tes', 'es', 's', 'te')
    print(ac.search('test'))
