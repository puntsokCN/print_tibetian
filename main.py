#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author   : pingcuo
# Blog     : 
# Date     : 2019-09-03
# Name     : 
# Software : vscode
# Note     : 

'执行程序'

import data_print

all = data_print.words + data_print.symbols

# 主函数
def main() :
    
    # 所有存在字符
    with open(r"D:\平措\ex\programe\print_tibetian\正字规范下的藏文\data.txt", mode="w", encoding="UTF-16") as f:
        for line in all :
            f.write(line + "\n")  # 每行占一个字符写入文件

if __name__ == '__main__':
    main()

