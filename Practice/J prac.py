num = int(input())
num += 1

total_sum = 0

for current_num in range(num):
    total_sum += current_num ** 2

print(total_sum)