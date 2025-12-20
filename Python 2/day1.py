# age = int(input())
# assert age > 0, "bro still in hell"
# assert age < 150, "so old bruh"
# print(2025 - age)

# def product(num1, num2, num3):
#     result = num1 * num2 * num3
#     return result
# print(product(5, 8, 3))

# def product(**kwargs):
#     print(kwargs)

# product(a=2)

# def factorial(n):
#     return n * factorial(n-1)
# print(factorial(5))

# def factorial(n):
#     assert isinstance(n,int), 'จำนวนเต็มคับน้อง'
#     assert n > 0, 'ไม่ดีเลยนะ'
#     if n == 1 or n ==0:
#         return 1
#     return n * factorial(n-1)
# print(factorial(1000))

def fibo(n):
    if n == 1 or n==2:
        return 1
    return fibo(n-1) + fibo(n-2)

'''
fibo(1)=1
fibo(2)=1
fibo(7)= 13
'''
print(fibo(7))