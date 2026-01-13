"""
文件名: cities.py
描述: 练习 6.11 - 在字典中存储字典，记录城市的详细信息
"""

# --- 练习 6.11: 城市 ---

# 1. 数据结构设计: 
# 外层字典的键: 城市名 (string)
# 外层字典的值: 另一个包含详细信息的字典 (dict)
cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_158_000,
        'fact': 'nearby andes mountains',
    },
    'talkeetna': {
        'country': 'alaska',
        'population': 876,
        'fact': 'also nearby mountains',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 1_003_285,
        'fact': 'located in himalaya',
    },
}

# 2. 遍历外层字典: 获取城市名 (city) 和信息字典 (city_info)
# 逻辑: city_info 现在是一个字典，包含 country, population 等键
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    
    # 3. 从内层字典中提取数据
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    # 4. 打印格式化信息
    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact}")

# 作者: Kris
# 日期: 2026-01-13