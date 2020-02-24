#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

typedef struct node {
    int val;
    struct node * next;
} node_t;

/**
 * @brief add node to end of linked list
 * @param head - head of linked list
 * @param val - value to add to node
 * @return true if completed correctlyj
 */
bool pushTail(node_t * head, int val) {
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
bool pushHead(node_t ** head, int val) {
    node_t * newHead = (node_t *)malloc(sizeof(node_t));
    newHead->val = val;
    newHead->next = *head;
    
    *head = newHead;
    return true;
}

/**
 * @brief print all nodes till NULL is found
 * @param head valid head of LL
 * @return none
 */
void printall_nodes(node_t * head) {
    node_t * current = head;
    
    // print each node value till NULL is found
    while (current != NULL) {
        printf("%d\n", current->val);
        current = current->next;
    } 
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
        // printf("debug popIndex @ %d", currentIndex);
        current = current->next;
        currentIndex++;
    }

    // for(int i = 0; i<99999999; i++);
    // sext next pointer to 2 ahead
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

    // if (current->val == val) {
    //     popHead
    // }
    
    // while(current->next->next != NULL) {
    //     if (current->next->val == val) {
    //         if (current->next->next == NULL)
    //         {
    //             current->next = NULL;
    //         } else {
    //             current->next = current->next->next;
    //         }
    //     }
    //     // go to next node
    //     current = current->next;
    // }

    // do {
    //     // printf("debug, current->val = %d, current->next = 0x%X\n", current->val, current->next);
    //     if (current->val == val) {
    //         if (current->next == NULL) {
    //         free(*head);
    //         break;
    //         }

    //         printf("debug, current->val = %d, current->next = 0x%X\n", current->val, current->next);
    //         popIndex(current, currentIndex);
    //         // if(popIndex(currentIndex)) {
    //         //     // printf("DEBUG, SUCCESS removed ")
    //         // }
    //     }
    //     // printf("debug, current->val = %d, current->next = 0x%X\n", current->val, current->next);

    //     // if (current->next == NULL) 
    //     // {
    //     //     if (c)
    //     // }
    //     if (current->next != NULL) {
    //         current = current->next;

    //         currentIndex++;
    //     }
    // } while (current->next != NULL);

    
        while (current != NULL) {
            // printf("debug1, current->val = %d, current->next = 0x%X\n", current->val, current->next);
            if (current->val == val) {
                // if (current->next == NULL) {
                // free(*head);
                // break;
                // }

                // printf("debug2, current->val = %d, current->next = 0x%X\n", current->val, current->next);
                popIndex(current, currentIndex);
                // *head = current;
                

                // if(popIndex(currentIndex)) {
                //     // printf("DEBUG, SUCCESS removed ")
                // }
            }
        // printf("debug, current->val = %d, current->next = 0x%X\n", current->val, current->next);

        // if (current->next == NULL) 
        // {
        //     if (c)
        // }
            if (current->next != NULL) {
                // printf("debug3, current->val = %d, current->next = 0x%X\n", current->val, current->next);
                current = current->next;

                currentIndex++;
            } else {
                break;
            }
    } 

    return true;
}

/**
 * @brief main test
 * @param none
 * @return 0 if no problem found
 */
int main(void) {
    node_t * head = (node_t *)malloc(sizeof(node_t));
    if (head == NULL) { return 1; }

    // configure initial head values
    head->val = 0;
    head->next = NULL;

    // add node 1 to tail and print list
    if(pushTail(head, 1)) {
        printf("SUCCESS adding value of 1\n");
    } else {
        printf("FAILED adding value of 1\n");
    }
    printall_nodes(head);

    // add node 2 to tail and print list
    if(pushTail(head, 2)) {
        printf("SUCCESS adding value of 2\n");
    } else {
        printf("FAILED adding value of 2\n");
    }
    printall_nodes(head);

    // add node 3 to tail and print list
    if(pushTail(head, 3)) {
        printf("SUCCESS adding value of 3\n");
    } else {
        printf("FAILED adding value of 3\n");
    }
    printall_nodes(head);

    // add node 3 to head and print list
    if(pushHead(&head, 4)) {
        printf("SUCCESS adding value of 4 to head\n");
    } else {
        printf("FAILED adding value of 4 to head\n");
    }
    printall_nodes(head);

    // remove head and print list
    if(popHead(&head)) {
        printf("SUCCESS removing head\n");
    } else {
        printf("FAILED removing head\n");
    }
    printall_nodes(head);

    // remove tail and print list
    if(popTail(head)) {
        printf("SUCCESS removing tail\n");
    } else {
        printf("FAILED removing tail\n");
    }
    printall_nodes(head);

    // remove tail and print list
    if(popIndex(head, 1)) {
        printf("SUCCESS removing index 1\n");
    } else {
        printf("FAILED removing index 1\n");
    }
    printall_nodes(head);

    // remove node with value of 2 and print list
    if(popValue(&head, 2)) {
        printf("SUCCESS removing value of 2\n");
    } else {
        printf("FAILED removing value of 2\n");
    }
    printall_nodes(head);

    return 0;
}