#!/usr/bin/python3

def swap(val, size):
    newVal = int()
    bits = size - 1
    # for n in range(size + 1, 0, -1):
    for n in range(0, size):
        newVal = newVal | (((val >> (bits - n)) & 0x1) >> n)
        # print(f"n = {n}, bits-n = {bits-n}, newVal = {newVal}")
        # tempValue = (val >> (bits -n)) & 0x1
        # print(f"tempValue = {tempValue}")
        # tempValue2 = tempValue >> n
        # print(f"tempValue2 = {tempValue2}")
        # newVal |= tempValue2        
    return newVal

val = 8
newVal = swap(val, 4)
print(f"val = {val} and newVal = {newVal}")

val = 81
newVal = swap(val, 8)
print(f"val = {val} and newVal = {newVal}")