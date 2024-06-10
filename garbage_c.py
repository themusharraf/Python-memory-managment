import gc
import ctypes

"""
Python Garbage Collection
github.com/themusharraf  
"""  # noqa


def ref_count(address):
    return ctypes.c_long.from_address(address).value


def object_exists(object_id):
    for object in gc.get_objects():
        if id(object) == object_id:
            return True

    return False


class A:
    def __init__(self):
        self.b = B(self)

        print(f"A: {hex(id(self))}, B: {hex(id(self.b))}")


class B:
    def __init__(self, a):
        self.a = a
        print(f"B: {hex(id(self))}, A: {hex(id(self.a))}")


gc.disable()  # on gc

a = A()

# Output
# B: 0x7cf46a6ed820, A: 0x7cf46a6ed7f0
# A: 0x7cf46a6ed7f0, B: 0x7cf46a6ed820

a_id = id(a)
b_id = id(a.b)

print(ref_count(a_id))  # 2
print(ref_count(b_id))  # 1

print(object_exists(a_id))  # True
print(object_exists(b_id))  # True

a = None

print(ref_count(a_id))  # 1
print(ref_count(b_id))  # 1

print(object_exists(a_id))  # True
print(object_exists(b_id))  # True

gc.collect()  # off gc

print(object_exists(a_id))  # False
print(object_exists(b_id))  # False

print(ref_count(a_id))  # 0
print(ref_count(b_id))  # 0
