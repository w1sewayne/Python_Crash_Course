"""
文件名: favorite_numbers.py
描述: 练习 6.2 - 使用字典存储人名和他们喜欢的数字
"""

# --- 练习 6.2: 喜欢的数 ---

# 1. 数据准备: 创建字典映射人名到数字
# 💡 逻辑: 这里的键 (Key) 是人名字符串，值 (Value) 是整数
favorite_numbers = {
    'jen': 5,
    'sarah': 2,
    'edward': 10,
    'phil': 7,
    'alice': 33,
}

# 2. 访问并打印 Jen 的数据
# 技巧: title() 方法可以让名字首字母大写，看起来更正式
print(f"Jen's favorite number is {favorite_numbers['jen']}.")

# 3. 访问并打印 Sarah 的数据
print(f"Sarah's favorite number is {favorite_numbers['sarah']}.")

# 4. 访问并打印 Edward 的数据
print(f"Edward's favorite number is {favorite_numbers['edward']}.")

# 5. 访问并打印 Phil 的数据
print(f"Phil's favorite number is {favorite_numbers['phil']}.")

# 6. 访问并打印 Alice 的数据
print(f"Alice's favorite number is {favorite_numbers['alice']}.")

# 作者: Kris
# 日期: 2026-01-13