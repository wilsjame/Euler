#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int sum_digit_factorials(int n);
int factorial(int n);

int main()
{
    constexpr int mn = 3;
    constexpr int mx = 999999;

    int sum = 0;
    for (int i = mn; i <= mx; i++)
    {
        if (i == sum_digit_factorials(i))
        {
            sum += i;
        }
    }

    // 40730
    cout << sum;

    return 0;
}

int sum_digit_factorials(int n)
{
    int sum = 0;
    while (n > 0)
    {
        sum += factorial(n % 10);
        n /= 10;
    }
    return sum;
}

int factorial(const int n)
{
    int sum = 1;
    for (int i = 1; i <= n; i++)
    {
        sum *= i;
    }
    return sum;
}
