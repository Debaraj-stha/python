#profram that accept list and return distinct element of list
def find_distinct(items):
    my_set=set(items)
    new_list=list(my_set)
    return new_list
distinct_list=find_distinct([1,2,3,4,5,1,4,2,9,5,6,8,9,10,11,12,13,14,15])
print("distinct element of list",distinct_list)
##program to find factorial of give number
def find_factorial(num):
    flag=0
    factorial=1
    if(num<0):
        flag=1
        factorial=0
    elif(num==1 or num==0):
        factorial=1
        flag=0
    else:
        for i in range(1,num+1):
            factorial*=i
        flag=0
    return factorial, flag
n=5
factorial,flag=find_factorial(n)
if(flag==1):
    print("factorial of negative number can not be calculated")
else:
    print(f"factorial of {n} is {factorial}")
##program to check whether a given number is prefect or not

def check_nember(num):
    sum=0
    for i in range(1,num):
        if(num%i==0):
            sum+=i
    if(sum==num):
        return True
    else:
        return False
num=5
if(check_nember(num)):
    print(f"{num } the number is perfect")
else:
    print(f"{num } the number is not perfect")

##program to check whether a number is prime or not

def check_prime(num):
    flag=1
    for i in range(2,num-1):
        if(num%i==0):
            flag=0
            break
    if(num<=1):
        flag=0
    if(flag==1):
        return True
    else:
        return False
num=10
if(check_prime(num)):
    print(f"{num } prime")
else:
    print(f"{num } not prime")

##python program to reverse a string
def reverse_string(string):
    reversed_string = string[::-1]
    return reversed_string
mystring="Hello World"
print("reverse of ",mystring,"is",reverse_string(mystring))





##program to count upper and lower case letters
def countt_upper_letters(string):
    lowercase=0
    uppercase=0
    for i in string:
        if i.isupper():
            uppercase+=1
        if i.islower():
            lowercase+=1
    return lowercase,uppercase

lowercase,uppercase=countt_upper_letters(mystring)
print("given string is",mystring)
print("lowercase character=",lowercase)
print("uppercase character=",uppercase)


##program to print only even numbers from list

def print_even_number(num_list):
    new_list=[]
    for i in num_list:
        if(i%2==0):
            new_list.append(i)
    
    return new_list

my_list=[1,2,3,4,5,6,7,8,10,22]
even_numbers=print_even_number(my_list)
print("even number from list ",my_list,"is",even_numbers)



##program to check whether a given number falls in a given range or not
def check_in_range(num,start,end):
    isFall=False
    if num in range(start,end+1):
        isFall=True
    return isFall
num=6
start=1
end=9
checkIsFall=check_in_range(num,start,end)
if(checkIsFall):
    print(f"{num} fall is given range of {start},{end}")
else:
    print(f"{num}not fall in given range {start},{end}")