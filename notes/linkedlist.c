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

/**
 * @brief remove first item from the LL
 * @param head of LL that will be removed
 * @return true if successful
 */
bool popHead(node_t ** head) {
    node_t * currentHead = *head;
    node_t * secondNode = currentHead->next;
    // printf("debug, currenHead.val = %d\n", currentHead->val);
    *head = secondNode;

    return true;
}

/**
 * @brief remove last item from LL
 * @param head of LL to which the tail will be removed
 * @return true if successful
 */
bool popTail(node_t * head) {
    node_t * current = head;

    while (current->next->next != NULL) {
        current = current->next;
    }

    current->next = NULL;

    return true;
}

/**
 * @brief remove a specific LL by index number
 * @param head of LL
 * @param index number to remove
 * @return true if successful
 */
bool popIndex(node_t * head, int index) {
    node_t * current = head;
    int currentIndex = 0;
        
    // get to index just before the one to remove
    while(currentIndex < index-1) {
        current = current->next;
        currentIndex++;
    }

    if (current->next == NULL) {
        free(current);
    } else {
        if (current->next->next != NULL) {
            current->next = current->next->next;
        } else {
            current->next == NULL;
        }

    }

    return true;
}

/**
 * @brief remove nodes with given value
 * @param head pointer to be modified
 * @param val to remove from LL
 * @return true if successful
 */
bool popValue(node_t ** head, int val) {
    node_t * current = *head;
    int currentIndex = 0;

    while (current != NULL) {
        if (current->val == val) {
            popIndex(current, currentIndex);
        }
        if (current->next != NULL) {
            current = current->next;

            currentIndex++;
        } else {
            break;
        }
    } 

    return true;
}
