program to print following pattern using for loop
1    
12
123
1234
12345

n = 5 

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#program to print  first 10 natural numbers using while loop

n=1
while (n<=10):
    print(n)
    n=n+1
program to print following pattern using while loop
1    
12
123
1234
12345

    i=1;
    while(i<=5):
        j=1
        while(j<=i):
            print(j, end=" ")
            j=j+1
        print()
        i=i+1

findmultiplication table of number given by user
output:
    Enter any number10
10* 1=10
10* 2=20
10* 3=30
10* 4=40
10* 5=50
10* 6=60
10* 7=70
10* 8=80
10* 9=90
10* 10=100

number=int(input("Enter any number:"))
for i in range(1,11):
    print(f"{number}*{i}={number*i}")

program to print fibonacci series
output:
    Enter number of terms:8
0
1
1
2
3
5
8
13

first=0
second =1
terms=int(input("Enter number of terms:"))
for i in range (0,terms):
    if(i<=1):
        print(i)
    else:
        next=first+second
        first=second
        second=next
        print(next)

Write a program to check whether a given user's number is prime or not.
Output:
enter a number to check prime or not:17
17 is  a prime number
enter a number to check prime or not:10
10 is not  a prime number

number=int(input("enter a number to check prime or not:"))
flag=1
for i in range(2,number-1):
    if(number%i==0):
        flag=0
        break
if(number<=1):
    flag=0
if(flag==1):
    print(f"{number} is  a prime number")
else:
    print(f"{number} is not  a prime number")


Write a program to find the factorial of a number.
output:
    Enter a numter to find factorial:7
factorial of 7 is 5040
Enter a numter to find factorial:5
factorial of 5 is 120

number=int(input("Enter a numter to find factorial:"))
factorial=1;

if(number<=1):
    factorial=1
else:
    for i in range(1,number):
        factorial+=factorial*i
print(f"factorial of {number} is {factorial}")

Write a program to find the sum of natural numbers entered by the user.
enetr a number to find sum:16
The sum of first 16 natural number is 136

number=int(input("enetr a number to find sum:"))
sum=0;
for i in range(1,number+1):
    sum=sum+i;
print(f"The sum of first {number} natural number is {sum}")


Write a program to find the sum of all even numbers between 1 to n
Enter a positive number: 10
The sum of even numbers from 1 to %10 is 30

n = int(input("Enter a positive number: ")) 
total = 0 
for num in range(1, n+1): 
    if num % 2 == 0: 
        total += num 
print(f"The sum of even numbers from 1 to %{n} is {total}")


# Write a program to check whether a given number is a palindrome or not.
# output:
# enter a number:2634
# the number is not palindrome
# enter a number:121
# the number is palindrome


# num=int(input("enter a number:"))
# reverse=0
# temp=num
# while num!=0:
#     reminder=num%10
#     reverse=reverse *10 + reminder
#     num//=10
# if(reverse==temp):
#     print("the number is palindrome")
# else:
#     print("the number is not palindrome")


# write a program to print the following pattern:
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
 
for i in range(n-1, 0, -1): 
    for j in range(i, 0, -1):
        print("*", end=" ") 
    print() #