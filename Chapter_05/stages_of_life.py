"""
文件名: stages_of_life.py
描述: 练习 5.6 - 根据年龄判断人生阶段 (if-elif-else 链)
"""

# --- 练习 5.6: 人生的不同阶段 ---

# 1. 数据准备: 设置年龄
age = 18

# 2. 逻辑判断: 这是一个很长的 if-elif 链
# 💡 技巧: 只需要检查上限 ( < x )，因为下限已经被上面的条件排除了
if age < 2:
    print("This person is a baby.")
elif age < 4:
    # 隐含逻辑: age >= 2 且 age < 4
    print("This person is a toddler.")
elif age < 13:
    # 隐含逻辑: age >= 4 且 age < 13
    print("This person is a child.")
elif age < 18:
    # 隐含逻辑: age >= 13 且 age < 18
    print("This person is a teenager.")
elif age < 65:
    # 隐含逻辑: age >= 18 且 age < 65
    print("This person is an adult.")
else:
    # 隐含逻辑: age >= 65
    print("This person is an elder.")