amount_of_loop = int(input())
no1_loop = amount_of_loop+1
no2_loop = amount_of_loop-1
final_num = 0
plus_num = 0
miss_num = 0
for count1 in range(no1_loop):
    plus_num += count1

for count2 in range(no2_loop):
    miss_num += int(input())

final_num = plus_num-miss_num
print(final_num)


