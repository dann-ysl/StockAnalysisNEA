
def halfDouble(x):
    a = [2*x,3*x,4*x]
    b = [(1/2)*x,(1/4)*x]
    return [a,b]

allArr = halfDouble(4)
print (allArr[0])
print (allArr[1])

fast = allArr[0]
slow = allArr[1]

print (fast)
print (slow)