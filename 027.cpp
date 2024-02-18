#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int count_primes_in_a_row(int a, int b);
bool prime(int n);

int main()
{
    int mxN = 0;
    int ab = 0;
    for (int a = -999; a < 1000; a++)
    {
        for (int b = -1000; b <= 1000; b++)
        {
            if (const int n = count_primes_in_a_row(a, b); n > mxN)
            {
                ab = a * b;
                mxN = n;
            }
        }
    }

    //-59231
    cout << ab;

    return 0;
}

int count_primes_in_a_row(const int a, const int b)
{
    for (int n = 0;; n++)
    {
        if (const int product = n * n + a * n + b; !prime(product))
        {
            return n;
        }
    }
}

bool prime(const int n)
{
    if (n < 2) return false;
    for (int x = 2; x * x <= n; x++)
    {
        if (n % x == 0) return false;
    }
    return true;
}
