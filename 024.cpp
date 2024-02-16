#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

void print(const vector<int> &myints);

int main()
{
    vector myints = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};

    for (int i = 0; i < 1000000; i++)
    {
        print(myints);
        ranges::next_permutation(myints.begin(), myints.end());
    }
    // 2783915460
    return 0;
}

void print(const vector<int> &myints)
{
    for (const int myint: myints)
    {
        cout << myint;
    }
    cout << endl;
}
