"""
文件名: alien_colors_2.py
描述: 练习 5.4 - 使用 if-else 结构处理两种得分情况
"""

# --- 练习 5.4: 外星人颜色 2 ---

# 1. 数据准备
alien_color = 'green'

# 2. 逻辑判断: 执行 if 代码块 (绿色情况)
print("\n--- Version 1: Running the if block ---")
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You just earned 10 points!")

# 3. 逻辑判断: 执行 else 代码块 (非绿色情况)
# 修改变量值为 'yellow' 或 'red'
alien_color = 'yellow'

print("\n--- Version 2: Running the else block ---")
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    # 💡 逻辑: 只要不是绿色，都会执行这里
    print("You just earned 10 points!")