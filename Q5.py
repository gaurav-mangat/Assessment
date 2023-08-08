def total_trek_length(A, B, C):
    # Use the equation Suman's distance = T meters and Suman's distance = Ravi's distance + C meters
    # to find the total length of the trek (T)
    T = (A + B + C) / 2
    return T

A = float(input("Enter the distance Amit beats Suman (in meters): "))
B = float(input("Enter the distance Amit beats Ravi (in meters): "))
C = float(input("Enter the distance Suman beats Ravi (in meters): "))

length = total_trek_length(A, B, C)
print("Total length of the trek:", length, "meters")
