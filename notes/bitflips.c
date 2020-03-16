#include <stdlib.h>
#include <stdio.h>

void setBit(int * value, int bitMask) {
    *value = ~(~*value & ~bitMask);
}

void clearBit(int * value, int bitMask) {
    *value = ~(~*value | ~bitMask) ^ *value;
}

void setValue(int * value, int newValue) {
    *value = ~(*value & ~newValue) ^ ~(*value | newValue);
}