#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>
using namespace std;

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int j;
    cin >> j;

    for (j; j > 0; j--)
    {
        string s, s1, s2;
        cin >> s;
        for (int i = 0; i < s.length(); i++)
        {
            if (i % 2 == 0)
            {
                s1 += s[i];
            }
            else
            {
                s2 += s[i];
            }
        }

        cout << s1 << " " << s2 << endl;
    }

    return 0;
}
