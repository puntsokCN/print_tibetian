#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author   : pingcuo
# Blog     : 
# Date     : 2019-09-03
# Name     : 
# Software : vscode
# Note     : 

'实验'

import data


def f() :
    
    def g(x) :
        return 'ར' + x
    def la(x) :
        return 'ལ' + x

    get_words = []
    for word in data.exist_top_under_words :  # 循环给 words 的元素(word) 加上加字
        # 分别判断 语法里是否有对应的上加字
        if word in data.top_ra :
              
            r = map(g, data.sub_under_word[word])
            get_words = get_words + list(r)    # 压入 数组
        # 处理 la
        if word in data.top_la :
            r = map(la, data.sub_under_word[word])
            get_words = get_words + list(r)    #   合并数组
    return get_words
print(f())