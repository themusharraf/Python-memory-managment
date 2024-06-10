"""
Pythonda hamma narsa ob'ektdir. Ob'ekt o'zining ichki holatiga ega. Ba'zi ob'ektlar ichki holatini o'zgartirishga imkon beradi, boshqalari esa yo'q.
Ichki holatini o'zgartirish mumkin bo'lgan ob'ekt o'zgaruvchan ob'ekt, ichki holatini o'zgartirib bo'lmaydigan ob'ekt esa o'zgarmas ob'ekt deb ataladi.
github.com/themusharraf
Ichki holatini o'zgartirib bo'lmaydigan ob'ekt o'zgarmas deb ataladi, masalan: number, a string, and a tuple.
Ichki holatini o'zgartirish mumkin bo'lgan ob'ekt o'zgaruvchan deb ataladi, masalan: list, a set, and a dictionary.

"""  # noqa

# immutable  o'zgarmas ob'ekt # noqa

# Numbers (int, float, bool,…)
# Strings
# Tuples
# Frozen sets


# mutable  o'zgaruvchan ob'ekt # noqa
# Lists
# Sets
# Dictionaries

# immutable example

counter = 100

print(id(counter))

print(hex(id(counter)))  # 16 lik

counter = 200
print(id(counter))

# mutable example

# Sahna orqasida, Python yangi ro'yxat ob'ektini yaratadi va ranksro'yxatga havola qilish uchun o'zgaruvchini o'rnatadi: # noqa
ratings = [1, 2, 3]
print(hex(id(ratings)))

ratings.append(4)
print(hex(id(ratings)))

# o'zgarmas and o'zgaruvchan misol # noqa
low = [1, 2, 3]
high = [4, 5]

rankings = (low, high)

print(id(rankings))
high.append(6)
print(rankings)
print(id(rankings))
