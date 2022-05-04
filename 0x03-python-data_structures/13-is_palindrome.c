#include "list.h"

/**
 * is_palindrome - function
 * @head: head
 * Return: 0
 */
int is_palindrome(listint_t **head)
{
	while (*head != NULL)
	{
		if ((*head)->next != NULL)
		{
			return (0);
			*head = (*head)->next;
		}
		else
		{
			return (1);
			*head = (*head)->next;
		}
	}
	return(1);
}
