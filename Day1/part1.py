# read from the file
file = open('part1.txt', 'r')

nums = []
count = 0

def reverse_str(x):
  return x[::-1]

lines = file.readlines()
for i in lines:
    for j in i:
        if (j.isdigit()):
            nums.append(int(j)*10)
            break
    for j in reverse_str(i):
        if (j.isdigit()):
            nums[len(nums) - 1] += int(j)
            break
    count += 1
sum = 0
for i in nums:
    sum += i
print(sum)        

file.close()