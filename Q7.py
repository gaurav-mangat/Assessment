List=[]
ch=1
gcd=0
print("You have to enter the elments for the list(should be two or more than two) : ")
while ch==1:
    i=int(input("\nEnter the element: "))
    List.append(i)
    ch=int(input("Press 1 to enter next element or Press 0 if you have completed the list : "))

print("List is : ",List)
    
min_ele=min(List)
for a in range(1,min_ele+1):
    for b in List:
        if b%a==0:
            gcd=a
        else:
            gcd=0

print("\n Greatest Common Divisor is : ",gcd)


