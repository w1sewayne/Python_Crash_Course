"""
文件名: deli.py
描述: 练习 7.8 & 7.9 - 熟食店。处理订单列表并移动到完成列表。
"""

# --- 练习 7.8 & 7.9: 熟食店与五香烟熏牛肉 ---

# 1. 数据准备
sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'roast beef', 'pastrami']
finished_sandwiches = []

# 2. 处理“卖完了”的情况 (练习 7.9)
print("--- Notice: The deli has run out of pastrami. ---\n")

# 💡 逻辑: 只要 'pastrami' 还在列表中，就一直删除它
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# 3. 处理剩余订单 (练习 7.8)
while sandwich_orders:
    # 从列表末尾取出一个订单
    current_sandwich = sandwich_orders.pop()
    
    print(f"I made your {current_sandwich} sandwich.")
    
    # 移入完成列表
    finished_sandwiches.append(current_sandwich)

# 4. 打印结果
print("\n--- The following sandwiches have been made: ---")
for sandwich in finished_sandwiches:
    print(f" - {sandwich.title()} sandwich")

# 作者: Kris
# 日期: 2026-02-04