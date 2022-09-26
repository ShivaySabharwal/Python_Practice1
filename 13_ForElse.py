nums = [10,16,18,21,26]

for num in nums:

    if num % 5 == 0:
        print(num)
        break
else:
    print("not found")

num = 10

for i in range(2,num):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")