#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <deque>
#include <numeric>
using namespace std;

bool is_pandigital(vector<int> digits);
vector<int> concant_digits(long a, long b, long c);

int main()
{
    constexpr long limit = 4321; // sense
    unordered_set<long> products;
    long sum = 0;
    for (long i = 1; i < limit; i++)
    {
        for (long j = i + 1; j < limit; j++)
        {
            vector<int> digits = concant_digits(i, j, i * j);
            if (digits.size() == 9 && is_pandigital(digits))
            {
                products.insert(i * j);
                sum = accumulate(products.begin(), products.end(), 0);
                cout << i << " * " << j << " = " << i * j << " " << sum << endl;
            }
        }
    }

    // 45228
    sum = accumulate(products.begin(), products.end(), 0);
    cout << sum;

    return 0;
}

vector<int> concant_digits(long a, long b, long c)
{
    vector<int> digits;
    while (a)
    {
        digits.push_back(a % 10);
        a /= 10;
    }
    while (b)
    {
        digits.push_back(b % 10);
        b /= 10;
    }
    while (c)
    {
        digits.push_back(c % 10);
        c /= 10;
    }

    return digits;
}

bool is_pandigital(vector<int> digits)
{
    ranges::sort(digits);

    bool OK = true;
    for (int i = 0; i < digits.size(); i++)
    {
        if (i + 1 != digits[i])
        {
            OK = false;
        }
    }
    return OK;
}
