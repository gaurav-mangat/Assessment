def factorial(num):
    if num==1 or num==0:
        return 1
    else:
        prod=1
        prod=num*factorial(num-1)
        return prod

def permutation(n,r):
    a=factorial(n)
    b=factorial(n-r)
    return a/b

def combination(n,r):
    c=permutation(n,r)
    d=factorial(r)
    return c/d
repeat=0
repeat2=0
while repeat==1:
    n=int(input("Enter the value of n: "))
    r=int(input("Enter the value of r: "))
    
    
    while repeat2==1: 
        print("\nPress 1 for performing Permutation: ")
        print("Press 2 for performing Combination: ")
        ch=int(input("Enter your choice: "))
        if ch==1:
            print("Permutaiton is : ", permutation(n,r))

        elif ch==2:
            print("Combination is : ", combination(n,r))

        else: 
            print("Invalid choice.")

        repeat2=int(input("Press 0 for exit and Press 1 to continue for same values of n and r: "))   

    repeat=int(input("Press 0 for exit and Press 1 to continue to find Permutation and Combinations for another values of n and r : "))
    if repeat==0:
        repeat2=0

