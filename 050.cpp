#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

vector<int> generate_primes(int limit);

bool prime(int n);

int main()
{
    constexpr int limit = 1000000;
    vector<int> primes_vector = generate_primes(limit);
    unordered_set primes_set(primes_vector.begin(), primes_vector.end());

    int ans;
    int mx_cnt = 0;
    for (const auto &prime: primes_vector)
    {
        for (int i = 0; i + 1 < primes_vector.size(); i++)
        {
            int sum = primes_vector[i];
            for (int j = i + 1; j < primes_vector.size(); j++)
            {
                sum += primes_vector[j];
                if (sum > prime)
                {
                    break;
                }
                if (sum == prime && j - i + 1 > mx_cnt)
                {
                    mx_cnt = j - i + 1;
                    ans = prime;
                }
            }
        }
    }

    // 997651
    cout << ans;
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
