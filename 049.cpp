#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

vector<int> generate_primes(int limit);
bool are_permutations(int a, int b, int c);
unordered_set<int> int_to_set_of_digits(int num);

int main()
{
    constexpr int limit = 9999;
    vector<int> primes_vector = generate_primes(limit);
    const unordered_set primes_set(primes_vector.begin(), primes_vector.end());

    for (const auto &prime: primes_vector)
    {
        const int mx_delta = (10000 - prime) / 2;
        for (int delta = 1; delta <= mx_delta; delta++)
        {
            int a = prime;
            int b = a + delta;
            int c = b + delta;

            if (primes_set.contains(b)
                && primes_set.contains(c)
                && are_permutations(a, b, c))
            {
                cout << a << " " << b << " " << c << endl;
                // 2969 6299 9629
                // 296962999629
            }
        }
    }
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

bool are_permutations(int a, int b, int c)
{
    const unordered_set<int> set_a = int_to_set_of_digits(a);
    const unordered_set<int> set_b = int_to_set_of_digits(b);
    const unordered_set<int> set_c = int_to_set_of_digits(c);

    return set_a == set_b && set_b == set_c;
}

unordered_set<int> int_to_set_of_digits(int num)
{
    std::unordered_set<int> digits_set;

    while (num > 0)
    {
        int digit = num % 10;
        digits_set.insert(digit);
        num /= 10;
    }

    return digits_set;
}
