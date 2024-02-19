#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <deque>
using namespace std;

deque<int> rotate_deque(deque<int> deque);
int deque_digits_to_int(deque<int> deque);
deque<int> int_digits_to_deque(int num);
vector<int> generate_primes(int limit);

int main()
{
    constexpr int limit = 1000000;
    vector<int> primes_vector = generate_primes(limit);
    const unordered_set primes_set(primes_vector.begin(), primes_vector.end());

    int cnt = 0;
    int sum = 0;
    for (const auto &prime: primes_vector)
    {
        if (prime == 2
            || prime == 3
            || prime == 5
            || prime == 7)
        {
            continue;
        }

        // removing left to right
        bool OKLR = true;
        deque<int> dequeLR = int_digits_to_deque(prime);
        while (!dequeLR.empty())
        {
            if (!primes_set.contains(deque_digits_to_int(dequeLR)))
            {
                OKLR = false;
            }
            dequeLR.pop_front();
        }

        // removing right to left
        bool OKRL = true;
        deque<int> dequeRL = int_digits_to_deque(prime);
        while (!dequeRL.empty())
        {
            if (!primes_set.contains(deque_digits_to_int(dequeRL)))
            {
                OKRL = false;
            }
            dequeRL.pop_back();
        }

        if (OKLR && OKRL)
        {
            cnt++;
            sum += prime;
            cout << prime << " " << cnt << " " << sum << endl;
        }
    }

    // 739397 11 748317
    return 0;
}

deque<int> rotate_deque(deque<int> deque)
{
    deque.push_back(deque.front());
    deque.pop_front();
    return deque;
}

int deque_digits_to_int(deque<int> deque)
{
    int order = 1;
    int num = 0;
    while (!deque.empty())
    {
        const int digit = deque.back();
        deque.pop_back();
        num += digit * order;
        order *= 10;
    }
    return num;
}

deque<int> int_digits_to_deque(int num)
{
    deque<int> digits_deque;
    while (num > 0)
    {
        int digit = num % 10;
        digits_deque.push_front(digit);
        num /= 10;
    }
    return digits_deque;
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
