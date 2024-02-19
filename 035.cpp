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
    for (int i = 2; i < limit; i++)
    {
        int num = i;
        deque<int> digits = int_digits_to_deque(num);
        int OK = true;
        int shifts = 7; // cheese
        while (--shifts)
        {
            if (!primes_set.contains(num))
            {
                OK = false;
            }
            digits = rotate_deque(digits);
            num = deque_digits_to_int(digits);
        }
        if (OK)
        {
            cnt++;
        }
    }

    // 55
    cout << cnt;

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
