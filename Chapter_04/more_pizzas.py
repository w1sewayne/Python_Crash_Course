"""
文件名: more_pizzas.py
描述: 练习 4.11 - 演示列表的独立复制 (Deep Copy via Slicing)
"""

# --- 练习 4.11: 你的比萨，我的比萨 ---

# 1. 数据准备：初始化我的比萨列表
my_pizzas = ['pepperoni', 'hawaiian', 'seafood']

# 2. 核心操作：创建副本
# ⚠️ 极其重要: 必须使用 [:] 进行全切片复制
# 如果写成 friend_pizzas = my_pizzas，那只是创建了引用（别名），修改一个会影响另一个！
friend_pizzas = my_pizzas[:]

# 3. 数据差异化：分别添加不同的比萨
my_pizzas.append('durian')       # 我加榴莲
friend_pizzas.append('ice cream') # 朋友加冰淇淋

# 4. 验证输出：打印我的列表
print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

# 5. 验证输出：打印朋友的列表
# 预期结果：应该包含 'ice cream' 但不包含 'durian'
print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)

# 作者: Kris
# 日期: 2026-1-11