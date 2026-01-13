"""
文件名: cities_extended.py
描述: 练习 6.12 - 扩展练习，自动计算人口密度等级
"""

# --- 练习 6.12: 扩展 ---

cities = {
    'tokyo': {
        'country': 'japan',
        'population': 37_400_000,
        'fact': 'largest metropolitan area',
    },
    'vatican city': {
        'country': 'vatican',
        'population': 825,
        'fact': 'smallest country in the world',
    },
}

print("=== 🏙️ City Analysis Report ===")

for city, info in cities.items():
    print(f"\nAnalyzing: {city.title()}...")
    
    # 1. 扩展逻辑: 根据人口数量自动添加标签
    # 💡 逻辑: 这里演示了如何在循环中对数据进行处理和判断
    pop = info['population']
    if pop > 10_000_000:
        size_label = "Mega City (超大城市)"
    elif pop < 1000:
        size_label = "Micro City (微型城市)"
    else:
        size_label = "Medium City"
        
    print(f"\tLocated in: {info['country'].title()}")
    print(f"\tPopulation: {pop:,} ({size_label})") # 使用 :, 添加千位分隔符
    print(f"\tFun Fact: {info['fact']}")

# 作者: Kris
# 日期: 2026-01-13