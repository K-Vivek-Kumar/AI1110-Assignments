/*
From the given theory equations, we obtained the value of a as 10.
Verifying the value of a from the below 'C' programme !!
*/
#include <stdio.h>

int main()
{
    // Frequencies as given in the table
    int fi[] = {7, 10, 8, 10, 5};

    // Mid-Values of the respective
    int xi[] = {5, 15, 25, 35, 45};

    int sum_of_fi = 0;
    int sum_of_product_fixi = 0;

    for (int i = 0; i < 5; i++)
    {
        sum_of_fi = sum_of_fi + fi[i];
    }

    for (int i = 0; i < 5; i++)
    {
        sum_of_product_fixi = sum_of_product_fixi + fi[i] * xi[i];
    }

    // As we know that, mean = (Sum of fixi)/(Sum of fi)
    if (sum_of_product_fixi / sum_of_fi == 24)
    {
        printf("The value of 'a' is verified to be 10.");
    }
    return 0;
}