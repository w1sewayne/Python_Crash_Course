"""
文件名: movie_tickets.py
描述: 练习 7.5 - 电影票。根据不同年龄段收取不同费用。
"""

# --- 练习 7.5: 电影票 ---

prompt = "\nHow old are you?"
prompt += "\n(Enter 'quit' when you are finished.) "

# 1. 循环询问年龄
while True:
    age = input(prompt)

    # 2. 退出检查
    if age == 'quit':
        break

    # 3. 将输入转换为整数以便比较
    age = int(age)

    # 4. 根据年龄段判定价格
    if age < 3:
        print("  You get in free!")
    elif age < 12:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")

# 作者: Kris
# 日期: 2026-02-04