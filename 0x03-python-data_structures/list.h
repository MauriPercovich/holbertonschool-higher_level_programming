#ifndef LIST_H
#define LIST_H
#include <stddef.h>

/**
 * struct listint_s - list
 * @i: int
 * @next: next
 */
typedef struct listint_s
{
    int i;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int i);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif
