def introduction():
    print("Welcome to python class")
def subtraction(num1,num2=3):
    diff=num1-num2
    return diff
def total_sum(*var):
    sum=0
    mul=1
    for i in var:
        sum+=i
    for i in var:
        mul+=i

    return sum,mul

# introduction()
# difference=subtraction(num2=3,num1=4)
# print(difference)
# sum,mul=total_sum(3,7,1,2)
# print(sum)
# print(mul)
def find_max(num1,num2,num3):
    if(num1==num2==num3):
        return "equal"
    if(num1==num2):
        return num1
    if(num1==num3):
        return num3
    if(num2==num3):
        return num2
    if(num2==num1):
        return num2
    if num1>num2 and num1>num3:
        return num1
    if num2>num3 and num2>num1:
        return num2
    if num3>num1 and num3<num2:
        return num
largest = find_max(8,1,8)
# print(largest)

def find_sum(num):
    length = len(num)
    sum = 0
    mul=1
    for i in range(length):
        sum+=num[i]
        mul*=num[i]
    return sum,mul

my_num=[1,2,3,4,5,6,7,8,9,10]
sum,mul=find_sum(my_num)
print(sum)
print(mul)


