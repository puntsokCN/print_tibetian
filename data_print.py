#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'打印选项'

import data, process

### 文字部分 *****************************************************************
# 1.基本字母 + 镜像字
l_1 = data.words + list(data.mirror_value.values()) 
# 2. 上加字
l_2 = process.add_top_word(data.words)    
# 3. 下加字
l_3 = process.add_under_word(data.words)  
# 4. 上下加字
l_4 = process.add_top_under_word() 
# 5. སཾསྐྲྀཏ་ (somedreed) 字
l_5 = data.somedreed_word + data.special_words
# 6. སཾསྐྲྀཏ་ (somedreed) 字 下加字
l_6 = process.add_under_word_for_somedreed_word(l_5)
# 7. 所有字 可带 普适 音标
l_7 = process.add_normal_symbol_of_phonetic(l_1 + l_2 + l_3 + l_4 + l_5 +l_6)
# 8. སཾསྐྲྀཏ་ (somedreed) 字添加专有音标
l_8 = process.add_somedreed_symbol_of_phonetic(l_5 + l_6)
# 9  所有字都可以加 后加字  输入顺序在 音标后 
l_9 = process.add_behind_word(l_1 + l_2 + l_3 + l_4 + l_5 + l_6 + l_7 + l_8)

#  字的总和
words =  l_1 + l_2 + l_3 + l_4 + l_5 +l_6 + l_7 + l_8 + l_9


# 符号 ********************************************************************
# 10. 数字
l_10 = data.numbers
# 11.# 句标
l_11 = data.single_symbol
# 12. # 标点符号
l_12 = data.punctuation
# 13.# སཾསྐྲྀཏ་ (somedreed)四 字标
l_13 = data.symbol_of_somedreed_word 
# 14. # སཾསྐྲྀཏ་ (somedreed) 符号 单独成立
l_14 = data.symbol_of_somedreed
# 15. # 天文学中的符号  单独成立
l_15 = data.symbol_of_calendar
# 16. 藏文中的 音符  单独成立
l_16 = data.symbol_of_sound
# 17. 经文常见符号 单独成立
l_17 = data.symbol_of_buddhist_scriptures

# 18. 拿出 音标
l_18 = data.symbol + data.symbol_of_somedreed_phonetic
# 19. 拿出 下加字变体
l_19 = data.add_under
# 20. 拿出 后加字和符号
l_20 = data.add_behind

##  21.符号合计
symbols = l_10 + l_11 + l_12 + l_13 + l_14 + l_15 + l_16 + l_17 + l_18 + l_19 + l_20
