#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
{
    set<double> myset;
    for (int i = 2; i <= 100; i++)
    {
        for (int j = 2; j <= 100; j++)
        {
            myset.insert(pow(i, j));
        }
    }

    // 9183
    cout << myset.size();

    return 0;
}
