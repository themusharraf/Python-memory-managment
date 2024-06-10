import ctypes

counter = 100

print(counter)  # 100

print(id(counter))  # 11757064

print(hex(id(counter)))  # 0xb36608

counter = 100

max = counter

print(id(counter))
print(id(max))

max = 999
print(id(max))

counter = 1
print(id(counter))


# ctypes.c_long.from_address(counter).value()

def ref_count(address):
    return ctypes.c_long.from_address(address).value


numbers = [1, 2, 3]

numbers_id = id(numbers)

print(ref_count(numbers_id))  # 1

ranks = numbers

print(ref_count(numbers_id))  # 2

ranks = None

print(ref_count(numbers_id))  # 1

numbers = None

print(ref_count(numbers_id))  # 0
