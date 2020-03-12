/// mhmmmm
#include <stdio.h>
#include <stdlib.h>

typedef struct LinkedListNode {
    void *data;
    struct LinkedListNode *next;
} LinkedListNode;

LinkedListNode * newLinkedListNode(const void *data, size_t dataSize)
{
    LinkedListNode *node = calloc(1, sizeof(LinkedListNode));
    assert(node != NULL);

    node->data = malloc(dataSize);
    assert(node->data != NULL);

    memcpy(node->data, data, dataSize);

    return node;
}

LinkedListNode * newLinkedListNodeWithIntData(int intValue)
{
    return newLinkedListNode(&intValue, sizeof(int));
}

void freeLinkedListNode(LinkedListNode *node)
{
    if (node != NULL) {
        free(node->data);
        free(node);
    }
}

// 1->2->3->4->NULL
// ------head = 3->next
// 1->2->3->NULL
// rev 4->NULL

// rev 4->3->NULL
// 1->2->NULL

// rev 4->3->2->NULL
// 1->NULL

LinkedListNode * reverseLinkedList(LinkedListNode * head) {
    LinkedListNode * revLinkedList;
    LinkedListNode * current = head; // dont delete the head
    LinkedListNode * currentRev = revLinkedList; // dont delete rev head
    int notAtEnd = 1;


        if (current->next == NULL) {
            // currentRev->next = current;
            return current;
        }
        if (current->next->next == NULL) {
            currentRev = current->next;
            current->next = NULL;



            currentRev->next = reverseLinkedList(currentRev->next);
        }

    // free unneeded linked lists?

    return revLinkedList;
}
