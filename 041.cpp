#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <deque>
using namespace std;

vector<int> generate_primes(int limit);
bool is_pandigital(int num);

int main()
{
    constexpr int limit = 8000000; // guess
    const vector<int> primes_vector = generate_primes(limit);
    int mx = 0;
    for (const auto &prime: primes_vector)
    {
        if (is_pandigital(prime))
        {
            if (prime > mx)
            {
                mx = prime;
            }
        }
    }

    // 7652413
    cout << mx;

    return 0;
}

bool is_pandigital(int num)
{
    vector<int> digits;
    while (num > 0)
    {
        int digit = num % 10;
        digits.push_back(digit);
        num /= 10;
    }
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

vector<int> generate_primes(const int limit)
{
    vector isPrime(limit + 1, true);
    vector<int> primes;

    for (int i = 2; i * i <= limit; ++i)
    {
        if (isPrime[i])
        {
            for (int j = i * i; j <= limit; j += i)
            {
                isPrime[j] = false;
            }
        }
    }

    for (int i = 2; i <= limit; ++i)
    {
        if (isPrime[i])
        {
            primes.push_back(i);
        }
    }

    return primes;
}
