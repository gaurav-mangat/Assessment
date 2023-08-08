
def prodDigits(num):
    prod=1
    while num>0:
        r=num%10
        prod=r*prod
        num=num//10
    return prod

def MDR(num):
    global counter
    counter=0
    while num//10!=0:
        counter=counter+1
        num=prodDigits(num)
    return num

def MPersistence():
    return counter




num=int(input("Enter the number:"))
ans=MDR(num)
print("Multiplicative Digital root of ",num,"is :",ans)
print("Multiplicative Persistence of ",num,"is : ",MPersistence())