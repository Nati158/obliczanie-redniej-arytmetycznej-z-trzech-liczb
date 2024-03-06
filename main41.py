def calculate_average(num1, num2, num3):
    return (num1 + num2 + num3) / 3

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))
    average = calculate_average(num1, num2, num3)
    print("The average is:", average)
