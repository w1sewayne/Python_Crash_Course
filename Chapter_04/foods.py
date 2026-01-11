"""
文件名: foods.py
描述: 练习 4.12 - 使用 for 循环遍历多个列表
"""

# --- 练习 4.12: 使用多个循环 ---

# 1. 数据准备与复制
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # 使用切片创建独立副本

# 2. 数据修改：确保两个列表内容不再相同
my_foods.append('cannoli')
friend_foods.append('ice cream')

# 3. 遍历输出：展示我的食品
print("My favorite foods are:")
for food in my_foods:
    print(food)

# 4. 遍历输出：展示朋友的食品
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)

# 作者: Kris
# 日期: 2026-1-11
