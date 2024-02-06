#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *obj;

    printf("[*] Python list info\n");

    /* Check if the object is a Python list */
    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    /* Retrieve the size of the list and allocated memory */
    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    /* Loop through the list and print information about each element */
    for (i = 0; i < size; ++i)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);

        /* If the element is a bytes object, call print_python_bytes */
        if (PyBytes_Check(obj))
            print_python_list(obj);
    }
}

/**
 * print_python_bytes - Prints information about Python bytes
 * @p: PyObject representing a Python bytes object
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    /* Check if the object is a Python bytes object */
    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    /* Retrieve the size and string representation of the bytes object */
    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);

    str = PyBytes_AsString(p);
    printf("  trying string: %s\n", str);

    /* Print the first 10 bytes of the bytes object */
    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; ++i)
        printf("%02x%c", str[i] & 0xFF, i < 9 ? ' ' : '\n');
}

/**
 * print_python_float - Prints information about Python float
 * @p: PyObject representing a Python float object
 */
void print_python_float(PyObject *p)
{
    printf("[.] float object info\n");

    /* Check if the object is a Python float object */
    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    /* Retrieve and print the value of the float object */
    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

