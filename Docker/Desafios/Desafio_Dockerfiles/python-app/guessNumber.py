import random

print('Adivinhe o número...\n')

print('Escolha os limites')
min = int(input('Minimo: '))
max = int(input('Máximo: '))

chosen = random.randint(min, max)

guess=False
while not guess:
    choice = int(input("Escolha um número: "))
    if choice == chosen:
        print("\nAcertaste no número!")
        guess=True







