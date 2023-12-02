# read from the file
file = open('part1.txt', 'r')

nums=[]
num_words = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5,'six':6,'seven':7,'eight':8,'nine':9}
count = 0
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words = ""
words2 = ''
truth = False

def reverse_str(x):
  return x[::-1]

lines = file.readlines()
for i in lines:
    for j in i:
        words += j
        if (j.isdigit()):
            nums.append(int(j)*10)
            words=""
            break
        for k in numbers:
            if (k in words):
                nums.append(int(num_words[k])*10)
                truth = True
                break
        if (truth):
            truth = False
            words = ""
            break
    for j in reverse_str(i):
        words2 = j + words2
        if (j.isdigit()):
            nums[len(nums) - 1] += int(j)
            words2 = ""
            break
        for k in numbers:
            if (k in words2):
                nums[len(nums) - 1] += int(num_words[k])
                truth = True
                break
        if (truth):
            truth = False
            words2 = ""
            break
    count += 1
sum = 0
for i in nums:
    sum += i
print(sum)        

file.close()