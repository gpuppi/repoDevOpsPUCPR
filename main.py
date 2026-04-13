import random

print(f"Insira um valor inteiro (exemplo: {random.randint(1,100)}):")
num = int(input())
binary = bin(num)[2:]
print(f"O número {num} em binário é: {binary}")