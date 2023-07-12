#include <stdio.h>
#include <stdbool.h>
#include <time.h>
#include <limits.h>

double generate (void) {

    double n = 0; // decimal approx for pi
    int d = 1; // denominator

    /*
    time_t t1;
    time_t t2 = time(&t1);

    time_t interval = -1;
    */

    for (int i = 0; i != 2147483640; i++) {

        if (i % 2 == 0) n += 1.0/d;
        else n -= 1.0/d;
        d += 2;
    }
    return 4*n;
}

int main (void) {
    double pi = generate();
    printf("%0.15f\n", pi);
}