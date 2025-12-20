start_num = int(input())
end_num = int(input())

if end_num % 2 ==0:
    end_num += 1

if start_num % 2 == 0:
    for final_num in range(start_num,end_num,2):
        print(final_num)
elif start_num % 2 > 0:
    start_num += 1
    for final_num in range(start_num,end_num,2):
        print(final_num)