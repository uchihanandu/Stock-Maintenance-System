x=input()
c=0
while(1):
    if(c== len(x)-1):
        break
    if(x[c]=="W" and x[c+1]=="U" and x[c+2]=="B"):
        c=c+3
    else:
        print(x[c],end="")
        c=c+1
        if(x[c:c+3]=="WUB"):
            print(" ",end="")
    