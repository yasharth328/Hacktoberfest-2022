# Python Program to Calculate the Sum of Arithmetic Progression
# Series Using Math Formula

# Take the Input from the User
first_Num = int(input("Enter First Number of an A.P Series: "))
Total_num = int(input("Enter the Total Numbers in this A.P Series: "))
diff = int(input("Enter the Common Difference: "))

# Calculation
total = (Total_num * (2 * first_Num + (Total_num - 1) * diff)) / 2
tn = first_Num + (Total_num - 1) * diff

# Print the Output
print("\nThe Sum of Arithmetic Progression Series = " , total)
print("The tn Term of Arithmetic Progression Series = " , tn)
