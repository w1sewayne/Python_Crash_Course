import time

def start_game():
    print("==================================")
    print("🏰 欢迎来到《迷失古堡》文字版")
    print("==================================")
    time.sleep(1)
    
    print("\n你醒来时，发现自己站在两扇大门前。")
    print("左边的门上画着一条【龙】 🐉")
    print("右边的门上画着一个【宝箱】 💰")
    
    # 这里用到了 input() 获取玩家输入
    choice = input("\n你想打开哪扇门？(输入 '左' 或 '右'): ")
    
    # 这里就是你刚学的 if 语句！
    if choice == '左':
        print("\n🚪 你推开了左边的门...")
        time.sleep(1)
        print("一条巨大的火龙正盯着你！")
        print("它喷出火焰... 🔥")
        print("GAME OVER (游戏结束 - 你变成了烤肉)")
        
    elif choice == '右':
        print("\n🚪 你推开了右边的门...")
        time.sleep(1)
        print("屋子里金光闪闪！✨")
        print("你发现了传说中的 Python 宝藏书！")
        print("YOU WIN (恭喜通关！)")
        
    else:
        print("\n❌ 你犹豫不决，天花板塌下来了...")
        print("GAME OVER")

# 启动游戏
start_game()