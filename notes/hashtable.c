#include <stdlib.h> // NULL
#include <stdbool.h> // true


// use linked list for hash collisions
typedef struct node
{
    char* word;
    struct node* next;
}
node;

node* first[26] = {NULL}; // All posotions will be null

int main(char* name)
{
    // hash the name into a spot
    int hashedValue = hash(name);

    // insert the name in table with hashed value
    insert(hashedValue, name);
}

/*
 * takes a string and hashes it into the correct bucket
 */
int hash(const char* buffer)
{
    // assign a number to the first char of buffer from 0-25
    return tolower(buffer[0]) - 'a';
}

/*
 * takes a string and inserts it into a linked list at a part of the hash table
 */
void insert(int key, const char* buffer)
{
    // try to instantiate node to insert word
    node* newptr = malloc(sizeof(node));
    if (newptr == NULL)
    {
        return;
    }

    // make a new pointer
    strcpy(newptr->word, buffer);
    newptr->next = NULL;

    // check for empty list
    if (first[key] == NULL)
    {
       first[key] = newptr;
    }
    // check for insertion at tail
    else
    {
        node* predptr = first[key];
        while (true)
        {
            // insert at tail
            if (predptr->next == NULL)
            {
                predptr->next = newptr;
                break;
            }

            // update pointer
            predptr = predptr->next;
        }
    }
}
