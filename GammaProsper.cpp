#include <stdio.h>
#include <stdlib.h>
#include <cmath>

long double gammaProsper(long double x)
{
    long double y;
    long double h = 0.0001;
    long double gamma = 0;
    long double oldgamma;

    y = h;
    do
    {
        oldgamma = gamma;
        gamma += h * pow(y, x - 1) * exp(-y);
        y += h;
    } while (oldgamma != gamma);

    return gamma;
}

int main() {
    gammaProsper();
}