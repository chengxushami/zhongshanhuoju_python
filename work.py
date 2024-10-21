# -*-coding:utf-8-*-
def jijie():
    # 季节判断机器人
    num=int(input("请输入月份："))
    if num<=3:
        print("春季")
    elif num>=4 and num<=6:
        print("夏季")
    elif num >=7 and num <=9:
        print("秋季")
    elif num>=10 and num<=12:
        print("冬季")
    else:
        print("机器故障")
    pass
def jiage():
    # 价格预警机器人
    product=input("输入商品名称（A,B,C）:")
    price=int(input("请输入降价值:"))
    if product=='A':
        if price<=30:
            print("未达预期")
        elif price>=30:
            print(f"{product}已降价{price}元")
    if product=='B':
        if price<=20:
            print("未达预期")
        elif price>=20:
            print(f"{product}已降价{price}元")
    if product=='C':
        if price<=10:
            print("未达预期")
        elif price>=10:
            print(f"{product}已降价{price}元")
    pass

def kaoshi():
    # 考试评语机器人
    score=int(input("输入成绩（0-100）："))
    if score<=60:
        print('要加油呀！')
    elif score<80 and score>=60:
        print('不错呀，认真学习了！')
    elif score>=80:
        print('考得不错，不要骄傲！')
    else:
        pass
    pass

def kongtiao():
    # 智能空调机器人
    season=input("输入‘winter’或‘summer’：")
    tem=int(input('输入温度：'))
    if season=='winter' and tem<10:
        print("太冷了，开热空调")
    elif season=='summer' and tem>27:
        print("太热了，开冷空调")
    else:
        pass
    pass

if __name__ == '__main__':
    # 选择机器人
    print("请选择机器人")
    print("1.季节判断机器人")
    print("2.价格预警机器人")
    print("3.考试评语机器人")
    print("4.智能空调机器人")
    num=int(input("请输入机器人编号："))
    if num==1:
        jijie()
        pass
    elif num==2:
        jiage()
        pass
    elif num==3:
        kaoshi()
        pass
    elif num==4:
        kongtiao()
        pass
    else:
        print("输入有误，请重新输入")
    pass
