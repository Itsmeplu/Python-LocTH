amount_of_num = int(input())
final_num = 0
for _ in range(amount_of_num):
    checking_num = int(input())
    if checking_num == 0:
        final_num += 1
print(final_num)