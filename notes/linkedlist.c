#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// LINKED LIST
/**
 * @brief simple linked list
 * @param none so dont list it
 * @return none so dont list it
 */
typedef struct node {
    int val;
    char * name;
    struct node * next;
} node_t;

/**
 * @brief add node to end of linked list
 * @param head - head of linked list
 * @param val - value to add to node
 * @return true if completed correctlyj
 */
bool linkedList_pushTail(node_t * head, int val) {
    node_t * current = head;
    while (current->next != NULL) {
        current = current->next;
    }

    current->next = (node_t *)malloc(sizeof(node_t));
    current->next->val = val;
    current->next->next = NULL;

    return true;
}

/**
 * @brief add node to head of LL
 * @param head valid head of LL
 * @return true if completed correctly
 */
bool linkedList_pushHead(node_t ** head, int val) {
    node_t * newHead = (node_t *)malloc(sizeof(node_t));
    newHead->val = val;
    newHead->next = *head;
    
    *head = newHead;
    return true;
}


