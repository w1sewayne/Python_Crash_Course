import pandas as pd
import matplotlib.pyplot as plt
import io

# ==========================================
# 1. 获取数据 (模拟从数据库或CSV读取)
# ==========================================
# 真实场景中，数据往往是不完美的：
# - 有的行是空的 (NaN)
# - 日期是字符串格式，电脑不认识
# - 价格可能混入了奇怪的字符
csv_data = """
Order ID,Product,Quantity Ordered,Price Each,Order Date,Purchase Address
176558,USB-C Charging Cable,2,11.95,04/19/19 08:46,"917 1st St, Dallas, TX 75001"
176559,Bose SoundSport Headphones,1,99.99,04/07/19 22:30,"682 Chestnut St, Boston, MA 02215"
176560,Google Phone,1,600,04/12/19 14:38,"669 Spruce St, Los Angeles, CA 90001"
176560,Google Phone,1,600,04/12/19 14:38,"669 Spruce St, Los Angeles, CA 90001"
,nan,nan,nan,nan,nan
176561,Wired Headphones,1,11.99,04/30/19 09:27,"333 8th St, Los Angeles, CA 90001"
176562,USB-C Charging Cable,1,11.95,04/29/19 13:03,"381 Wilson St, San Francisco, CA 94016"
176563,Bose SoundSport Headphones,1,99.99,04/02/19 07:46,"668 Center St, Seattle, WA 98101"
176564,USB-C Charging Cable,1,11.95,04/12/19 10:58,"790 Ridge St, Atlanta, GA 30301"
176565,Macbook Pro Laptop,1,1700,04/24/19 10:38,"915 Willow St, San Francisco, CA 94016"
"""

# 将字符串模拟成文件读取
df = pd.read_csv(io.StringIO(csv_data))

print("--- 原始数据 (前5行) ---")
print(df.head())

# ==========================================
# 2. 数据清洗 (Data Cleaning) - 分析师最耗时的步骤
# ==========================================
print("\n--- 开始清洗数据 ---")

# 动作1：去掉全空的行 (那是脏数据)
df = df.dropna(how='all')

# 动作2：去掉重复的行 (比如系统故障导致重复记录)
df = df.drop_duplicates()

# 动作3：数据类型转换
# 把 "2" (文本) 变成 2 (数字)，把 "11.95" 变成数字
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
df['Price Each'] = pd.to_numeric(df['Price Each'])

# 动作4：处理日期
# 把 "04/19/19 08:46" 这种字符串变成Python能理解的时间对象
df['Order Date'] = pd.to_datetime(df['Order Date'])

# ==========================================
# 3. 特征工程 (Feature Engineering) - 挖掘更深的信息
# ==========================================
# 我们需要算出“总销售额”，并提取“城市”和“月份”

# 算出每单总价 = 数量 * 单价
df['Sales'] = df['Quantity Ordered'] * df['Price Each']

# 从地址中提取城市 (通过逗号分割字符串)
# lambda 是匿名函数，意思是对每一行地址 x，取它逗号分隔后的第2部分
df['City'] = df['Purchase Address'].apply(lambda x: x.split(',')[1].strip())

print("--- 清洗后的干净数据 ---")
print(df[['Product', 'City', 'Sales']].head())

# ==========================================
# 4. 数据分析与回答问题 (Analysis)
# ==========================================
print("\n--- 分析结果 ---")

# 问题1：哪个城市销售额最高？
# 这里的 groupby 就像 Excel 里的透视表
city_results = df.groupby('City')['Sales'].sum()
print(f"销售额最高的城市是: {city_results.idxmax()}，金额: ${city_results.max()}")

# ==========================================
# 5. 可视化 (Visualization) - 做进博客的内容
# ==========================================
# 画一个柱状图
cities = [city for city, df in df.groupby('City')]

plt.figure(figsize=(10, 6))
plt.bar(cities, city_results)
plt.title('Sales by City (Real World Example)')
plt.xticks(rotation=45)
plt.ylabel('Sales in USD ($)')
plt.xlabel('City Name')
plt.grid(axis='y', linestyle='--', alpha=0.7)

print("\n正在生成图表...")
plt.show()