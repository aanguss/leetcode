#include <stdio.h>


// to use with: pair_t hash_table[size];
typedef struct pair {
    int value;
    int key;
}pair_t;

// to use with: struct pair hast_table[size];
struct pair {
    int value;
    int key;
};

// void display(struct pair[],);
void main()
{
    int size, temp;
    printf("Enter the size of the table: ");
    scanf("%d", &size);

    struct pair hash_table[size];
    // pair_t hash_table[size];
    
    printf("Enter the elements: ");
    for(int i = 0; i < size; i++) {
        scanf("%d", &temp);
        hash_table[temp % size].value = temp;
        hash_table[temp % size].key = temp % size;
    }
    printf("\n");
}


// open addressing = just find next one available
// seperate chaining = just chain to another link list or array(?)