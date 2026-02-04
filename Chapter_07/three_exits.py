"""
文件名: three_exits.py
描述: 练习 7.6 - 三种出路。使用变量 active 控制循环结束。
"""

# --- 练习 7.6: 三种出路 (以比萨练习为例) ---

prompt = "\nPlease enter a topping you would like on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

# 1. 定义标志变量
active = True

# 2. 使用标志变量控制 while
while active:
    topping = input(prompt)

    if topping == 'quit':
        # 3. 修改标志变量以结束循环
        active = False
    else:
        print(f"  Adding {topping} to your pizza.")

# 作者: Kris
# 日期: 2026-02-04