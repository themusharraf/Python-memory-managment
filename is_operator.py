"""
is Ikki o'zgaruvchining bir xil ob'ektga murojaat qilishini tekshirish uchun operatordan foydalaning .
is Ikki o'zgaruvchining identifikatsiyasini tekshirish va ==ikkita o'zgaruvchining tengligini tekshirish uchun operatordan foydalaning .
not Operator natijasini bekor qilish uchun operatordan foydalaning is.
github.com/themusharraf

"""  # noqa

a = 100
b = a
result = a is b
print(result)
print(id(a))  # 11757064
print(id(b))  # 11757064

a = 100
b = 100
result = a is b
print(result)

ranks = [1, 2, 3]
rates = [1, 2, 3]

result = ranks is rates
print(result)

print(id(ranks))
print(id(rates))

a = 100
b = a
print(id(a))
print(id(b))

is_identical = a is b
is_equal = a == b

print(is_identical)
print(is_equal)

ranks = [1, 2, 3]
rates = [1, 2, 3]

is_identical = ranks is rates
is_equal = ranks == rates

print(is_identical)
print(is_equal)

print(id(ranks))
print(id(rates))

"""
Python is not operator
"""

ranks = [1, 2, 3]
rates = [1, 2, 3]

result = ranks is not rates
print(result)  # True
