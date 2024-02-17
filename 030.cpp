#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int sum_fifth_powers_of_digits(int n);

int main()
{
    constexpr int mn = 2;
    constexpr int mx = 999999;

    int sum = 0;
    for (int i = mn; i <= mx; i++)
    {
        if (i == sum_fifth_powers_of_digits(i))
        {
            sum += i;
        }
    }

    // 443839
    cout << sum;

    return 0;
}

int sum_fifth_powers_of_digits(int n)
{
    int sum = 0;
    while (n > 0)
    {
        sum += pow(n % 10, 5);
        n /= 10;
    }
    return sum;
}
