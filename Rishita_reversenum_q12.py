num = int(input("Enter a number: "))
reversed_num = int(str(num)[::-1])
print("Reversed Number:", reversed_num)


n = int(input("Enter a number: "))
reversed_n = 0
while n > 0:
    digit = n % 10                # Extract the last digit
    reversed_n = (reversed_ * 10) + digit  
    n//= 10               

print("Reversed Number:", reversed_n)
