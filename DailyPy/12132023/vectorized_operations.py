#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 00:03:56 2023

@author: zhihaowang
"""

import pandas as pd

# 创建一个示例DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)
print(df)

# 矢量化操作示例 - 将'A'列的每个元素加上1
df['A'] = df['A'] + 1
print(df)

# 矢量化操作示例 - 对'B'列取平方根
df['B'] = df['B'].apply(lambda x: x ** 0.5)
print(df)

# 矢量化操作示例 - 创建新列'C'，该列是'A'列和'B'列对应元素的和
df['C'] = df['A'] + df['B']
print(df)