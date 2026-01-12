"""
文件名: ordinal_numbers.py
描述: 练习 5.11 - 打印数字 1-9 的序数 (1st, 2nd, 3rd...)
"""

# --- 练习 5.11: Ordinal Numbers ---

# 1. 数据准备: 创建包含 1 到 9 的列表
# range(1, 10) 会生成 1 到 9 的数字
numbers = list(range(1, 10))

# 2. 遍历数字列表
for number in numbers:
    # 3. 判定序数后缀
    # 💡 逻辑: 1, 2, 3 有特殊的后缀，其余的都是 'th'
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        # 处理 4-9 的情况
        print(f"{number}th")