#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author   : pingcuo
# Blog     : 
# Date     : 2019-09-03
# Name     : 
# Software : vscode
# Note     : 

'根据需求自定义执行程序'

import data, process
    
# 1.基本字母
l_1 = data.words
# 2.带音标的 基本字母
l_2 = process.add_symbol(data.words)
# 3. 上加字
l_3 = process.add_top_word(data.words)   
# 4. 带音标的 上加字
l_4 = process.add_symbol(l_3)
# 5. 下加字
l_5 = process.add_under_word(data.words)
# 6. 带音标的 下加字
l_6 = process.add_symbol(l_5)
# 7. 上下加字
l_7 = process.add_top_under_word()
# 8  带音标的  上下加字
l_8 = process.add_symbol(l_7)
# 9  镜像翻转字
l_9 = process.add_mirror_word(data.words)  
# 10 带音标的 镜像字
l_10 = process.add_symbol(l_9)
# 11 特殊 下加字
l_11 = process.add_special_word(data.words)
# 12 带音标的  特殊下加字
l_12 = process.add_symbol(l_11)
# 13  音标
l_13 = data.symbol

# 主函数
def main() :
    
    # 所有存在的字符
    all = l_1 + l_2 + l_3 + l_4 + l_5 + l_6 + l_7 + l_8 + l_9 + l_10 + l_11 + l_12 +l_13

    # 将字符写到 txt文件
    with open("data.txt", mode="w", encoding="UTF-16") as f:
        for line in all:
            f.write(line + "\n")  # 每行占一个字符写入文件

if __name__ == '__main__':
    main()