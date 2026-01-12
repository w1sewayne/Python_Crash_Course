"""
文件名: conditional_tests.py
描述: 练习 5.1 - 编写一系列条件测试 (Conditional Tests)
"""

# --- 练习 5.1: 条件测试 ---

# 1. 数据准备: 定义一个变量用于测试
car = 'subaru'

# --- 第一组测试: 结果预测为 True 的情况 ---

# 测试 1
print("\nIs car == 'subaru'? I predict True.")
print(car == 'subaru')

# 测试 2
# 💡 逻辑: 变量值完全匹配
print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

# 测试 3
food = 'pizza'
print("\nIs food == 'pizza'? I predict True.")
print(food == 'pizza')

# 测试 4
score = 100
print("\nIs score == 100? I predict True.")
print(score == 100)

# 测试 5
language = 'python'
print("\nIs language == 'python'? I predict True.")
print(language == 'python')


# --- 第二组测试: 结果预测为 False 的情况 ---

# 测试 6
# 💡 注意: 大小写敏感，'Subaru' 不等于 'subaru'
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

# 测试 7
print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

# 测试 8
print("\nIs food == 'burger'? I predict False.")
print(food == 'burger')

# 测试 9
# 💡 逻辑: 100 不等于 99，所以 (score == 99) 为 False
print("\nIs score == 99? I predict False.")
print(score == 99)

# 测试 10
print("\nIs language == 'java'? I predict False.")
print(language == 'java')


# 作者: Kris
# 日期: 2026-1-12