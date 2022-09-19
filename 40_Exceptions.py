a = 5
b = 0

try:
    print('resource open')
    print(a/b)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong...")

finally:
    print('resource close')

print('Bye')