#This file has created by Kickstart Agent by Danish Akhtar

def isArmstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_digits
    return sum == num

#Example usage
number = 153
if isArmstrong(number):
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")