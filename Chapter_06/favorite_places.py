"""
文件名: favorite_places.py
描述: 练习 6.9 - 在字典中存储列表，记录每个人喜欢的多个地方
"""

# --- 练习 6.9: 喜欢的地方 ---

# 1. 数据结构: 创建字典，键是人名，值是包含多个地点的列表
favorite_places = {
    'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
    'erin': ['hawaii', 'iceland'],
    'willie': ['mt. verstovia', 'the playground', 'new hampshire'],
}

# 2. 双层遍历: 先遍历字典的人，再遍历这个人的地点列表
# 逻辑: name 是键，places 是列表
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    
    # 3. 内部循环: 遍历列表中的每一个地点
    for place in places:
        print(f"- {place.title()}")

# 作者: Kris
# 日期: 2026-01-13