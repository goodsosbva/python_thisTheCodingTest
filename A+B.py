#A,B=input().split(" ",2)
#N = int(input())
#k = int(0)
#for i in range(N):
#while(True):

#    A, B = input().split(" ", 2)
    #k = k + 1
#    C = int(A) + int(B)

#    print("Case #%d: %d" %(k,C) )

#################################
#import sys

#for line in sys.stdin:
#    A, B = map(int, line.split())
#    if A == 0 and B == 0:
#        break

#    C = A + B
#    print(C)

#import sys

#for line in sys.stdin:
#    a, b = map(int, line.split())
#    print(a + b)

N = int(input())
k = int(0)
for i in range(N):
#while(True):

    A, B = input().split(" ", 2)
    k = k + 1
    C = int(A) + int(B)
    print("Case #%d: %s + %s = %d"%(k, A ,B, C) )