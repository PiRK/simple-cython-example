#include <stdio.h>
#include "mymax.h"


float cmax(float num1, float num2)
{
    /* local variable declaration */
    float result;

    printf("print from c function\n");

    if (num1 > num2)
        result = num1;
    else
        result = num2;

    return result;
}
