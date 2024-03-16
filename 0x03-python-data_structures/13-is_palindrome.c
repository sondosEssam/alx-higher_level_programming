#include "lists.h"
/**
 * connecting_through_back - make the linked list an array
 * @head: head of the linked_list
 * Return: int
*/
int *connecting_through_back(listint_t **head)
{
	listint_t *curr = *head, *curr2 = *head;
	int n = 0, i = 1;

	while (curr != NULL)
	{
		n++;
		curr = curr->next;
	}
	int *p = malloc(sizeof(int) * (n + 1));

	p[0] = n;
	while (curr2 != NULL)
	{
		p[i] = curr2->n;
		i++;
		curr2 = curr2->next;
	}
	return (p);
}
/**
 * is_palindrome - functon to check palindrome of the list
 * @head: head of the linked list
 * Return: int
*/
int is_palindrome(listint_t **head)
{
	int *p = connecting_through_back(head);
	int n = p[0] + 1, i = 0;

	for (i = 1; i < n; i++)
	{
		if (p[i] != p[n - i])
			return (0);
	}
	return (1);
}
