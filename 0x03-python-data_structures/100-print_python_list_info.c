#include "Python.h"

/**
 * print_python_list_info - prints
 * @p: Python object (list)
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *listobj;
	int i;

	if (p)
	{
	listobj = (PyListObject *) p;
	printf("[*] Size of the Python List = %d\n", (int)PyList_Size(p));
	printf("[*] Allocated = %d\n", (int)listobj->allocated);
	for (i = 0; i < Py_SIZE(p); i++)
		printf("Element %d: %s\n", i, listobj->ob_item[i]->ob_type->tp_name);
	}
}
