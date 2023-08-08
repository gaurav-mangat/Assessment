# Implementing NAND function:

def nand(a,b):
    return not(a and b)
ch='1'
while(ch!='e'):
    print("Enter 0 for giving input False \nEnter 1 for giving input True")
    i1=int(input("Enter first input:"))
    i2=int(input("Enter second input:"))
    if(i1==0):
        a=False
    else:
        a=True
    if(i2==0):
        b=False
    else:
        b=True


    ans=nand(a,b)
    print(ans)
    ch=input("Enter e to Exit and 1 to Continue: ")