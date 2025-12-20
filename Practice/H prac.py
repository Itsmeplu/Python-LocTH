apple_cake = int(input())
orange_cake = int(input())
bag_no1 = int(input())
bag_no2 = int(input())

if apple_cake <= bag_no1 and orange_cake <= bag_no2 :
    print('YES')
elif apple_cake <= bag_no2 and orange_cake <= bag_no1 :
    print('YES')
else :
    print('NO')