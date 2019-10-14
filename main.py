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
    # with open("data.txt", mode="w", encoding="UTF-16") as f:
        index = 1
        for line in all :
            f.write(str(index) + ':' + line + ':' + ('+').join(line) + '\n')  
            index += 1

if __name__ == '__main__':
    main()

