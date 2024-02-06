#include <Python.h>

/**
 * print_python_list - Prints information about Python lists
 * @p: PyObject representing a Python list
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t i, size;
    PyObject *obj;

    printf("[*] Python list info\n");

    if (!PyList_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i)
    {
        obj = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(obj)->tp_name);
        if (PyBytes_Check(obj))
            print_python_bytes(obj);
    }
}

/**
 * print_python_bytes - Prints information about Python bytes
 * @p: PyObject representing a Python bytes object
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %ld\n", size);

    str = PyBytes_AsString(p);
    printf("  trying string: %s\n", str);

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

    if (!PyFloat_Check(p))
    {
        fprintf(stderr, "[ERROR] Invalid Float Object\n");
        return;
    }

    printf("  value: %f\n", ((PyFloatObject *)p)->ob_fval);
}
