# coding:utf-8
__author__ = 'zhoukunpeng'
# --------------------------------
# Created by zhoukunpeng  on 2015/8/15.
# ---------------------------------
from setuptools import setup, find_packages

with open("README.md", "rb") as f:
    long_description_b = f.read()
try:
    long_description = long_description_b.decode("utf-8")
except  Exception as e:
    try:
        long_description = long_description_b.decode("gbk")
    except Exception as _e:
        long_description = ''

setup(
    name="ahocorasick-python",
    packages=["ahocorasick"],
    version='0.0.9',
    description="this project is a aho-corasick automaton implementation by python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/zhoukunpeng504/ahocorasick-python',
    author="zhoukunpeng",
    author_email="zhoukunpeng504@163.com",
    package_data={
        '': ['*.rst'],
    }
)
