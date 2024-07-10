# WAP to print first n lines of the following pattern
'''
***
**
*'''

def pattern(n):
     for i in range(n,0,-1):
         p = "*" * i
         print(p)
a=int(input("Enter the number of line to print: "))
pattern(a)