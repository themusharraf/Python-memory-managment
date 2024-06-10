"""
Nonesinfning yagona ob'ektidir NoneType.
Noneo'zidan boshqa hech narsaga teng emas.
Boshqa qiymatlar bilan solishtirish uchun isyoki operatordan foydalaning .is notNone
Shuni ham ta'kidlash kerakki, None ob'ekti quyidagi xususiyatlarga ega:

Nonenolga teng emas (0, 0,0, …).
Nonebilan bir xil emas False.
Nonebo'sh satr bilan bir xil emas ( '').
Har qanday qiymat bilan taqqoslash o'zidan tashqari Noneqaytariladi .FalseNone

github.com/themusharraf

"""  # noqa

None
print(type(None))

print(None == None)
print(None is None)


class Apple:
    def __eq__(self, other):
        return True


apple = Apple()

print(apple == None)

# 1) o'zgaruvchining boshlang'ich qiymati sifatida Python None dan foydalanish # noqa

state = None

print(id(state))

if state is None:
    state = 'start'


# 2) O'zgaruvchan standart argument muammosini tuzatish uchun Python None ob'ektidan foydalanish # noqa

def append(color, colors=[]):
    colors.append(color)
    return colors


colors = ['red', 'green']
append('blue', colors)

print(colors)

hs1 = append('yellow')
print(hs1)

rgb = append('red')
print(rgb)


# Muammo shundaki, funktsiya belgilangan ro'yxatni yaratadi va har bir keyingi called( chaqirilsa ) bir xil ro'yxatni ishlatadi. # noqa
# None Ushbu muammoni hal qilish uchun siz qiymatdan quyidagi tarzda standart parametr sifatida foydalanishingiz mumkin  # noqa

def append(color, colors=None):
    if colors is None:
        colors = []

    colors.append(color)
    return colors


hsl = append('hue')
print(hsl)

rgb = append('red')
print(rgb)


# 3) Funktsiyaning qaytish qiymati sifatida Python None obyektidan foydalanish # noqa
# Agar funktsiya qaytish qiymatiga ega bo'lmasa, u Nonesukut bo'yicha qaytadi.  # noqa

def say(something):
    print(something)


result = say("hello")
print(result)
# Funktsiya say()hech narsa qaytarmaydi; shuning uchun u qaytadi None. # noqa
