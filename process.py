#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author   : pingcuo
# Blog     : 
# Date     : 2019-09-03
# Name     : 
# Software : vscode
# Note     : 

'功能函数模块'

import data


# 添加  普适音标
def add_normal_symbol_of_phonetic(words=[]) :
    '''
    添加音标
    :param word：lsit, 待处理字母数组
    :return：list, 处理后的字符数组 
    '''
    get_words = []  # 接收字符 的数组
    for x in data.symbol :  # 循环给 word数组 加 音标(x)
        for y in words :     # 循环给 word数组元素(y)  加音标（x）
            word = y + x
            get_words.append(word)   # 压入 数组
    
    return get_words 

# 添加 somedreed 专用音标
def add_somedreed_symbol_of_phonetic(words=[]) :
    '''
    添加 somedreed 音标
    :param word：lsit, 待处理字母数组 
    :return：list, 处理后的字符数组 
    '''
    get_words = []  # 接收字符 的数组
    for symbol in data.symbol_of_somedreed_phonetic  :  # 循环给 word数组 加 音标(x)
        for word in words :     # 循环给 word数组元素(y)  加音标（x）
            word = word + symbol
            get_words.append(word)   # 压入 数组
    return get_words 


# 添加 上加字
def add_top_word(words=[]) :
    '''
    添加 上加字
    :param word：lsit, 待处理字母数组
    :return：list, 处理后的字符数组
    '''
    get_words = [] # 接收字符
   
    for word in words :  # 循环给 words 的元素(word) 加上加字
        # 分别判断 语法里是否有对应的上加字
        if word in data.top_ha :  
            a =  'ཧ' + data.sub_word[word]   # 查询对应的下加字符、合并
            get_words.append(a)    # 压入 数组
        
        if word in data.top_la :
            a =  'ལ' + data.sub_word[word]   # 查询对应的下加字符、合并
            get_words.append(a)    # 压入 数组
        if word in data.top_ra:
            a =  'ར' + data.sub_word[word]   # 查询对应的下加字符、合并
            get_words.append(a)    # 压入 数组
        if word in data.top_sa: 
            a =  'ས' + data.sub_word[word]   # 查询对应的下加字符、合并
            get_words.append(a)    # 压入 数组
  
    return get_words


# 添加 下加字
def add_under_word(words =[]) :
    '''
    添加下加字
    :param word：lsit, 待处理字母数组
    :return：list, 处理后的字符数组
    '''
    get_words = [] # 接收字符

    for word in words :  # 循环给 words 的元素(word) 加下加字
        # 分别判断 语法里是否有对应的上加字
        if word in data.under_ya:  
            a =  word + 'ྱ'  #  给 word 加 对应的下加字
            get_words.append(a)    # 压入 数组
        if word in data.under_ra :
            a =  word + 'ྲ'  # 给 word 加 对应的下加字
            get_words.append(a)    # 压入 数组
        if word in data.under_la :
            a =  word + 'ླ'  # 给 word 加 对应的下加字
            get_words.append(a)    # 压入 数组
        if word in data.under_wa: 
            a =  word + 'ྭ'  # 给 word 加 对应的下加字
            get_words.append(a)    # 压入 数组
        
    return get_words


# 添加特殊下加字
def add_special_word(words=[]) :
    '''
    添加特殊下加字
    :param word：lsit, 待处理字母数组
    :return：list, 处理后的字符数组
    '''
    get_words = [] # 接收字符

    for word in words :  # 循环给 words 的元素(word) 加下加字
        # if word in data.under_ha: 
        #     a =  word + 'ྷ'  # 给 word 加 对应的下加字
        #     get_words.append(a)    # 压入 数组
        if word in data.under_ny: 
            a =  word + 'ྙ'  # 给 word 加 对应的下加字
            get_words.append(a)    # 压入 数组
        if word in data.under_va: 
            a =  word + 'ྰ'  # 给 word 加 对应的下加字
            get_words.append(a)    # 压入 数组
    
    return get_words


# 找到 同时存在 上加字  和 下加字 的字根
def find_top_under_word(words=[]) :
    '''
    找到 同时存在 上加字  和 下加字 的字根, 用于 data 的采集
    :param word：lsit, 待处理字母数组
    :return： none
    '''
    # 1.找出可以有上加字的 字母根 
    get_top_words = []
    for word in words :
        if word in  data.top_ha or word in data.top_la or word in data.top_ra or word in data.top_sa:
            get_top_words.append(word)  # 将字母根 压入 get_top_words
    
    # 2. 找出可以有下加字的 字母根
    get_under_words = []
    for word in words :
        if word in data.under_ha or word in data.under_ya or word in data.under_ra or word in data.under_la or word in data.under_va :
            get_under_words.append(word)
    
    # 3. 找出可以 既能加 上加字 且 能加 下加字的字母根
    exist_top_under_words = set(get_top_words) & set(get_under_words)
    exist_top_under_words = sorted(list(exist_top_under_words))  # 转为 list 并 排序
    
    # 4.添加下加字
    under_words = add_under_word(exist_top_under_words)  # 添加上加字
    
    # 5 建立 同时存在上下可加字根(exist_top_under_words) 与 已加 下加字(under_words )的映射关系
    #  存储 字典数据在 data.sub_under_word


# 上下同时 加字   此方法未考虑正字规范而是罗列出来了上下同时加字的所有组合
def add_top_under_word_all() :
    '''
    所有上下同时 加字的组合方式
    :param ： 无
    :return：list, 处理后的字符数组
    '''

    # 给各个 上加字 各准备一个作用于 map 的函数
    def ha(x) :
        return 'ཧ' + x
    def ra(x) :
        return 'ར' + x
    def la(x) :
        return 'ལ' + x
    def sa(x) :
        return 'ས' + x

    get_words = []    # 用于接收结果的数组


    for word in data.exist_top_under_words :  # 循环给 words 的元素(word) 加上加字
        # 分别判断 语法里是否有对应的上加字
        # 处理 ha
        if word in data.top_ha :
            r = map(ha, data.sub_under_word[word])
            get_words = get_words + list(r)    #   合并数组

        # 处理 ra
        if word in data.top_ra :
            r = map(ra, data.sub_under_word[word])
            get_words = get_words + list(r)    #   合并数组

         # 处理 la
        if word in data.top_la :
            r = map(la, data.sub_under_word[word])
            get_words = get_words + list(r)    #   合并数组

        # 处理 sa
        if word in data.top_sa :
            r = map(sa, data.sub_under_word[word])
            get_words = get_words + list(r)    #   合并数组

    return  get_words

#  正字规范下的上下加字
def add_top_under_word() :
    '''
    正字规范下的上下同时 加字
    :param ： 无
    :return：list, 处理后的字符数组
    '''

    # 给各个 上加字 各准备一个作用于 map 的函数
    def ra(x) :
        return 'ར' + x
    def sa(x) :
        return 'ས' + x

    # 用于给 word 添加  下加字  ྱ
    def make_sub_ya(word) :
    # 由于有两种情况需要函数外 压入数组
        if word in data.under_ya:
            a =  data.sub_word[word] + 'ྱ'  #  给 word 加 对应的下加字

        return a

    # 用于给word加下加字   ྲ
    def make_sub_ra(word) :
    # 只需调用无需 压入数组
        if word in data.under_ra:
            a =  data.sub_word[word] + 'ྲ'  #  给 word 加 对应的下加字
            sub_ra.append(a)    # 压入 数组


    get_words = []    # 用于接收结果的数组
    sub_ya_1 = []
    sub_ya_2 = []
    sub_ra = []

    for word in data.words :
        ###
        # 处理 上加字 ra
        if word in data.top_ra and word in data.under_ya  :
            sub_ya_1.append(make_sub_ya(word))
            r = map(ra, sub_ya_1)
            get_words = get_words + list(r)  #   合并数组

    for word in data.words :
        # 处理 上加字 sa (1)
        if word in data.top_sa and word in data.under_ya  :
            sub_ya_2.append(make_sub_ya(word))
            r = map(sa, sub_ya_2)
            get_words = get_words + list(r)

    for word in data.words :
        # 处理 上加字 sa(2)
        if word in data.top_sa and word in data.under_ra  :
            make_sub_ra(word)
            r = map(sa, sub_ra)
            get_words = get_words + list(r)



    get_words = list(set(get_words))
    return  get_words


# 添加  后加字
def add_behind_word(words =[]) :
    '''
    添加后加字
    :param word：lsit, 待处理字母数组
    :return：list, 处理后的字符数组
    '''
    get_words = [] # 接收字符
    
    for behind in data.add_behind :
        for word in words :
            ok_word = word + behind
            get_words.append(ok_word)
    return get_words  


#  somedreed字 专用下加字
def add_under_word_for_somedreed_word(words =[]) :
    '''
    somedreed字 专用下加字
    :param word：lsit, 传入 somedreed字
    :return：list, 处理后的字符数组
    '''
    get_words = [] # 接收字符
    
    for key in data.mirror_key :
        for word in words :
            ok_word = word + data.mirror_value_as_under_of_somedreed_word[key]
            get_words.append(ok_word)
    return get_words






# 测试
# print('1', add_symbol(data.words))     # ok
# print('2', add_top_word(data.words))   # ok
# print('3', add_under_word(data.words))  # ok
# print('4', add_top_under_word())        #ok
# print('5', add_mirror_word(data.words))



# print(add_top_word('ག'))
# # b = 'ཕ' + "\u0f92"
# b = 'ཕ' + "ྭ"
# print(add_under_word('ག'))
# print(add_top_under_word("ག"))
print(add_top_under_word())



# 入口函数
if __name__ == '__main__':
    pass