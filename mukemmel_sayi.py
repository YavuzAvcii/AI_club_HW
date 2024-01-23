# Bir sayının kendisi hariç pozitif bölenlerinin toplamı sayıya eşitse bu sayı *Mükemmel Sayıdır*

number = int(input("Please enter a number "))
multipliers = []

for i in range(1, 10):
    if number % i == 0 and i != number:
        multipliers.append(i)

total = sum(multipliers)

if sum(multipliers) == number:
    print("This is a perfect number")
else:
    print("This is not a perfect number")

