/**
 * Ted Talk Friday
 * Linked List challenge
 * Given a Linked List and a number n, write a function that returns the value at the n’th node from the end of the Linked List.
 */

#include <stdlib.h>
#include <stdio.h>
// int * list;


// list->next*endNumber == NULL

// for() {
//     if list->next ==nULL
// }

typedef struct node {
    int val;
    struct node * next;
} node_t;

int getIndexNFromEnd(node_t * head, int indexN) {
    node_t * tempNode = malloc(sizeof(node_t));
    tempNode = head;
    int nPositions = 0;

    int tempValue;

    while (nPositions <= indexN) {
        head = head->next;
        if (head->next == NULL) {
            return head->val;
        }
        nPositions++;
    }

    while(head->next != NULL) {
        tempNode = tempNode->next;
        head= head->next;
    }

    return tempNode->val;
}

int main(void) {
    node_t * head;
    getIndexNFromEnd(head);

    return 0;
}