# 一个最简单的计算，支持+, -, *, / 四种运算。仅需考虑输入输出为整数的情况(除法结果就是商，忽略余数)
def com(a:int,b:int,C:str) :
    if C=='+':
        print(f"{a}+{b}={a+b}")
    elif C=='-':
        print(f"{a}-{b}={a-b}")
    elif C=='*':
        print(f"{a}*{b}={a*b}")
    elif C=='/':
        print(f"{a}/{b}={a/b}")
com()
# 有1,2,3,4,个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
def num():
    count=0
    for i in range(1,5):
        for q in range(1,5):
            for w in range(1,5):
                if i!=q and i!=w and q!=w:
                    count+=1
                    print(i,q,w)
    print(f"有{count}个")
num()








