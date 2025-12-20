# sentence1 = 'Hello, how are you?'

# sentence2 = '''Hello,
#    how are you?'''

# print(sentence2)

# sentence_3 = "I'm a boy' # I'm a boy."
# sentence_4 = 'She said, "I am hungry."'
# sentence_5 = 'He said, \\ \n \"I\'m a boy.'
# print(sentence_3)
# print(sentence_5)

# print(len('''Doraemon the cat 
# robot'''))

# sentence6 = 'piano is playing game.'
# print(sentence6[7])
# sentence7 = 'angie walks into the room.'
# print(sentence7[12])
# print(sentence7[-5])

# print('hello world'[1:7])
# print('coding is awesome!'[-4])

# print(sentence7[-5::-1])
# name = 'plu'
# print(f'hello my name is {name}')




# Password


# password = input('create pass')
# while len(password)<8:
#     if len(password)>8 and len(password)<20:
#         print('OK')
#     else:
#         print("Pls change")
#         password = input('pls create new pass')

# entered_password = input('enter password')
# num_trial = 0
# while entered_password != password:
#     if num_trial == 3:
#         print('too much attempt')
#         break
    
#     else:
#         print('incorrect password')
#         num_trial += num_trial+1
#         entered_password = input('enter password')
# if entered_password == password:
#         print('Welcome')
# if 'abc' in 'abc123':
#     print('A')

#     print('hel' not in 'Hello')

string = 'hello world'
# for index in range(len(string)):
#          print(string[index])

for kanplu in string:
    print(kanplu)

    for index in range(len(string)):
        if index == 1:
            continue