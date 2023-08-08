l=[]
t=[]
i=1
flag=0
while i==1:
    l.append(int(input("Enter the element for the list: ")))
    i=int(input("Press 1 to enter next element and 0 to complete the list : "))

print(l)
target=int(input("Enter the target: "))

for j in l:
    for k in l:
        if j+k==target:
            t.append(l.index(j))
            t.append(l.index(k))
            flag=1
            break
    if flag==1:
        break
if(flag==0):
    print("Target can't be matched in this list.")
print("Output: ",t)