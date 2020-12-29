#include <stdio.h>
#include <stdlib.h>

//
// A boring singly linked list where each node holds 1 random number
//

typedef struct ListNode
{
    struct ListNode *next;
    uint32_t random_value;
} ListNode;

static ListNode *s_list_head = NULL;

void list_add_random_value(uint32_t random_value)
{
    ListNode *node_to_add = malloc(sizeof(ListNode));
    if (node_to_add == NULL)
    {
        printf("unexpected malloc failure\n");
        return;
    }

    *node_to_add = (ListNode){
        .next = NULL,
        .random_value = random_value,
    };

    // Add entry to the front of the list
    node_to_add->next = s_list_head;
    s_list_head = node_to_add;
}

static void free_list(void)
{
    while (s_list_head != NULL)
    {
        ListNode *temp = s_list_head->next;
        free(s_list_head);
        s_list_head = temp;
    }
}

static void populate_example_list(void)
{
    for (int i = 0; i < 5; i++)
    {
        list_add_random_value(rand());
    }
}

int main(void)
{
    populate_example_list();
    free_list();
    return 0;
}