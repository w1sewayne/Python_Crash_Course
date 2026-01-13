# 1. 练习 4.13: 定义一个包含 5 种食品的元组
# 注意：元组使用圆括号 ()
foods = ('burger', 'pizza', 'carrot cake', 'cannoli', 'ice cream')

# 2. 使用 for 循环打印原始菜单
print("Original menu:")
for food in foods:
    print(food)

# 3. 尝试修改其中的一个元素 (这一步是为了演示报错)
# Python 不允许修改元组元素，如果取消下面这行的注释，程序会报错 (TypeError)
# foods[0] = 'sushi'

# 4. 餐馆调整菜单：替换了两种食品
# 虽然不能修改元组元素，但我们可以给变量 foods 重新赋值一个新的元组
print("\n--- Menu works changed ---")
foods = ('sushi', 'pizza', 'carrot cake', 'cannoli', 'taco')

# 5. 打印新的菜单
print("Modified menu:")
for food in foods:
    print(food)

# 作者: Kris
# 日期: 2026-1-12