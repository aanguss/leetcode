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

int main(void) {
    int value_1 = 0b0110; // 0x5; // 0110b
    int value_2 = 0b1001; // 0x9; // 1001b
    int value_3 = 0xF; // 1111b
    int value_4 = 0x0; // 0000b

    int mask_1  = 0x8; // 1000b
    int mask_2  = 0x1; // 0001b
    int mask_3  = 0x3; // 0011b
    int mask_4  = 0xF; // 1111b

    int bit_1   = 0x1; // 0001b
    int bit_2   = 0x2; // 0010b
    int bit_3   = 0x4; // 0100b
    int bit_4   = 0x8; // 1000b

    int tempValue, shadowReg;

    // set and clear functions
    setBit(&value_1, bit_1);
    printf("value_1 = %d\n", value_1);
    clearBit(&value_1, bit_2);
    printf("value_1 = %d\n", value_1);

    // set register value to a new value entirely
    shadowReg = value_3; // 0xF = 8
    // shadowReg = ~((shadowReg & value_2) ^ ~(shadowReg | value_2)); // expect 0xF -> 0x9
    setValue(&shadowReg, value_2); // 0x9
    printf("shadowReg = %d\n", shadowReg); // expected: 9
    setValue(&shadowReg, value_1);
    printf("shadowReg = %d\n", shadowReg); // expected 6
    setValue(&shadowReg, value_3);
    printf("shadowReg = %d\n", shadowReg); // expected 15
    setValue(&shadowReg, value_4);
    printf("shadowReg = %d\n", shadowReg); // expected 0

    return 0;
}