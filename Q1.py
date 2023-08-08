# Question 1

def merge_lists_into_dict(keys, values):
    merged_dict={}
    if len(keys) != len(values):
        print("Both lists should have the same length.")
        return
    for i in range(len(keys)):
        merged_dict[keys[i]] =values[i]
    return merged_dict

l1=[]
l2=[]
s=int(input("Define size of lists"))
for i in range(0,s):
    a=input("Enter the elements for first list:")
    l1.append(a)

for j in range(0,s):
    b=int(input("Enter the elements for second list:"))
    l2.append(b)

merged_dict = merge_lists_into_dict(l1, l2)
print(f"Merged Dictionary is : {merged_dict}")
