# 是否是数字
def isnum(c):
    if c not in '+-*/':
        return True
    return False


#分离数字和操作符
def splitCal(content):
    numLst = []
    opLst = []
    temp = ''
    for i in range(len(content)):
        if isnum(content[i]):
            if i == len(content) - 1:
                numLst.append(float(content[len(temp) + 1:]))
        else:
            if content[i] != '.':
                start = len(temp)
                if start > 0:
                    start = len(temp) + 1
                numLst.append(float(content[start:i]))
                opLst.append(content[i])
                temp = content[:i]

    return numLst,opLst


def cal(a,op,b):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b


# 分离数字和操作符
def calculator(content='1+1'):
    numLst,opLst = splitCal(content)
    #先算乘除
    i = 0
    while i < len(opLst):
        if opLst[i] in '*/':
            numLst[i] = cal(numLst[i],opLst[i],numLst[i+1])
            del opLst[i]
            del numLst[i+1]
        else:
            i += 1
    #再算加减
    i = 0
    while i < len(opLst):
        numLst[i] = cal(numLst[i], opLst[i], numLst[i+1])
        del opLst[i]
        del numLst[i + 1]

    return numLst[0]



# n, o = splitCal('1+1')
# print(n, o)
print(calculator('1+2'))
