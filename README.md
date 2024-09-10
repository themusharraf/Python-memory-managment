# VARIABLES & MEMORY MANAGEMENT 
### 1. [Garbage Collection](https://github.com/themusharraf/Python-memory-managment/blob/master/garbage_c.py)
### 2. [References](https://github.com/themusharraf/Python-memory-managment/blob/master/references.py)
### 3. [Dynamic Typing](https://github.com/themusharraf/Python-memory-managment/blob/master/dynamic_type.py)
### 4. [Mutable and Immutable](https://github.com/themusharraf/Python-memory-managment/blob/master/mutable_Immutable.py)  
### 5. [Python is operator](https://github.com/themusharraf/Python-memory-managment/blob/master/is_operator.py)
### 6. [Python None](https://github.com/themusharraf/Python-memory-managment/blob/master/none_not_is.py)


 
[Garbage Collection](https://github.com/themusharraf/Python-memory-managment/blob/master/garbage_c.py) Python’da avtomatik xotira boshqaruvi va chiqindilarni tozalash mexanizmini ko’rsatadi. Kodda ctypes moduli yordamida obyektlarning xotira manzillari orqali ular ustida ishlash va chiqindilarni tozalash (garbage collection) yoqilgan va o’chirilgan holatda obyektlar mavjudligini tekshirish amalga oshiriladi.

## Funksiyalar
- `ref_count(address)`: Bu funksiya ko’rsatilgan xotira manzilidagi obyektning foydalanish sonini qaytaradi.
- `object_exists(object_id)`: Bu funksiya ko’rsatilgan obyekt identifikatori (ID) bo’yicha obyekt mavjudligini tekshiradi.
## Sinflar
- `A`: Bu sinf B sinfidan obyektni yaratadi va undan nusxa oladi.
- `B`: Bu sinf A sinfidan obyektni yaratadi va undan nusxa oladi.
## Chiqindilarni tozalash
- `gc.disable()`: Chiqindilarni tozalash mexanizmini o'chiradi.
- `gc.collect()`: Chiqindilarni tozalash mexanizmini qo'lda chaqiradi.
