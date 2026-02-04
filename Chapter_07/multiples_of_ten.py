"""
文件名: multiples_of_ten.py
描述: 练习 7.3 - 10的整数倍。使用求模运算符判断。
"""

# --- 练习 7.3: 10的整数倍 ---

# 1. 获取输入并转换
number = input("Give me a number, please: ")
number = int(number)

# 2. 使用求模运算符 (%) 判断
# 💡 逻辑: 如果一个数除以 10 余数为 0，说明它是 10 的倍数
if number % 10 == 0:
    print(f"{number} is a multiple of 10.")
else:
    print(f"{number} is not a multiple of 10.")

# 作者: Kris
# 日期: 2026-02-04