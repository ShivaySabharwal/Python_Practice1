nums = [1,2,3,4,5,6]
print(nums[0])
print(nums[4:])
print(nums[-1])

names = ['shivay', 'pranav', 'satvik']

mil = [nums, names]
print(mil)

nums.append(24)
print(nums)
nums.insert(2,55)
print(nums)

#nums.remove(23)
print(nums)
nums.pop()
print(nums)

nums.extend([2,5,7,9,1])
print(nums)

print(min(nums))
print(max(nums))

nums.sort()
print(nums)