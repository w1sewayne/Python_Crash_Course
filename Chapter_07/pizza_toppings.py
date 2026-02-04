"""
文件名: pizza_toppings.py
描述: 练习 7.4 - 比萨配料。循环输入直到用户输入 'quit'。
"""

# --- 练习 7.4: 比萨配料 ---

prompt = "\nPlease enter a topping you would like on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.) "

# 1. 启动循环
while True:
    topping = input(prompt)

    # 2. 检查退出条件
    # 💡 技巧: 在执行核心逻辑前先检查是否需要退出
    if topping == 'quit':
        break
    else:
        print(f"  Adding {topping} to your pizza.")

# 作者: Kris
# 日期: 2026-02-04