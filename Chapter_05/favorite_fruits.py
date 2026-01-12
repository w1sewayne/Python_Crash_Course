"""
文件名: favorite_fruits.py
描述: 练习 5.7 - 使用多个独立的 if 语句检查列表内容
"""

# --- 练习 5.7: 喜欢的水果 ---

# 1. 数据准备: 创建喜欢的水果列表
favorite_fruits = ['bananas', 'strawberries', 'apples']

# 2. 独立逻辑检查: 我们需要检查 5 种不同的水果
# 💡 注意: 这里使用 5 个独立的 if，而不是 if-elif
# 因为我们想找出所有匹配项，而不是找到一个就停下

if 'bananas' in favorite_fruits:
    print("You really like bananas!")

if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")

if 'apples' in favorite_fruits:
    print("You really like apples!")

if 'oranges' in favorite_fruits:
    print("You really like oranges!")

if 'strawberries' in favorite_fruits:
    print("You really like strawberries!")