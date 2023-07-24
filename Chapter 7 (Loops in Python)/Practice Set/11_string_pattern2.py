#WAP to generate following pattern
'''
     C
    CI
   CIT
  CITY'''

a="CITY"
v=len(a)
for i in range (1,v+1):
    space= " " * (v-i)
    pattern = a[0:i]
    print(space,pattern)