def pyramid(n):
    for i in range(n):
        for j in range(i, n):
            print("",end="")
        for j in range(i+1):
            print("*",end="")
        for j in range(i):
            print("*",end="")
        print("")



pyramid(7)

###########################################################################################

num = int(input("enter odd number")) #5
cnt = num//2 #2

scnt =1
for i in range(cnt+1):
    print(cnt*""+"*"*scnt)
    cnt=cnt-1
    scnt=scnt+2
scnt=num-2
cnt=1
for i in range(num//2):
    print(cnt*""+"*"*scnt)
    scnt=scnt-2
    cnt=+1


