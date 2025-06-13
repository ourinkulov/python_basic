yosh = int(input("Iltimos yoshingizni kiriting"))

if yosh >= 18:
    print("Siz balog'at yoshidasiz")
elif yosh >= 13:
    print("Siz o'smir yoshidasiz")
else:
    print("Siz bolasiz")


number = int(input("Raqam kiriting"))
if number > 0:
    print(f'{number} raqami musbat son xisoblanadi.')

first_number = int(input("Birinchi raqamni kiriting"))
second_number = int(input("Ikkinchi raqamni kiriting"))
if (first_number == second_number):
    max_number = "Raqamlar teng"
elif(first_number < second_number):
    max_number = second_number
elif (first_number > second_number):
    max_number = first_number

print(f'Maxmimal raqam = {max_number}')

n = 10
if n > 10:
    pass
print("Hello")
