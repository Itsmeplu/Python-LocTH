# the_word = input()
# char_num = int(input())
# char_num -=1
# print(the_word[char_num])

# wins_record = input()
# Alice =0
# Bob =0

# for result in wins_record:
#      if result == ('A'):
#         Alice +=1
# for result2 in wins_record:
#     if result2 == ('B'):
#          Bob +=1

# if Alice > Bob:
#     print('ALICE')
# if Bob > Alice:
#        print('BOB')
# if Alice == Bob:
#        print('DRAW')

# print(Bob,Alice)

# giant_string = input()

# for single_char in giant_string:
#     print(single_char)

magic_string = input()

how_many_string = len(magic_string)
the_half_a = how_many_string // 2
the_half_b = how_many_string // 2

print(magic_string[the_half_b:how_many_string]+magic_string[0:the_half_a])