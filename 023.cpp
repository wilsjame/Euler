#include <iostream>
#include <set>
#include <vector>
using namespace std;

bool is_abundant(int n);
int sum_divisors(int n);
vector<int> get_divisors(int n);

int main()
{
    vector<int> abundant;
    for (int i = 0; i <= 29123; i++)
    {
        if (is_abundant(i))
        {
            abundant.push_back(i);
        }
    }

    set<int> myset;
    for (int i = 0; i < abundant.size(); i++)
    {
        for (int j = i; j + 1 < abundant.size(); j++)
        {
            myset.insert(abundant[i] + abundant[j]);
        }
    }

    long sum = 0;
    for (int i = 1; i <= 29123; i++)
    {
        if (!myset.contains(i))
        {
            sum += i;
        }
    }
    // 4179871
    cout << sum << endl;

    return 0;
}

bool is_abundant(const int n)
{
    return sum_divisors(n) > n;
}

int sum_divisors(int n)
{
    int sum = 0;
    const vector<int> divisors = get_divisors(n);
    for (int i = 0; i < divisors.size(); i++)
    {
        sum += divisors[i];
    }
    return sum;
}

vector<int> get_divisors(const int n)
{
    vector<int> divisors;
    for (int i = 1; i <= n / 2; i++)
    {
        if (n % i == 0)
        {
            divisors.push_back(i);
        }
    }
    return divisors;
}
