"""
文件名: alien_colors_3.py
描述: 练习 5.5 - 使用 if-elif-else 结构处理三种颜色的得分
"""

# --- 练习 5.5: 外星人颜色 3 ---

# 为了在一份代码中演示三个版本，我将定义一个函数或者多次赋值
# 你可以通过修改 current_color 的值来测试不同分支

# 1. 数据准备: 设置当前测试的颜色
current_color = 'red'  # 尝试改为 'green' 或 'yellow'

print(f"Current alien color is: {current_color}")

# 2. 多重逻辑判断
if current_color == 'green':
    # 分支 1: 绿色
    print("You earned 5 points!")
elif current_color == 'yellow':
    # 分支 2: 黄色
    print("You earned 10 points!")
else:
    # 分支 3: 红色 (或其他任何颜色)
    # 💡 提示: else 捕获所有剩余情况
    print("You earned 15 points!")