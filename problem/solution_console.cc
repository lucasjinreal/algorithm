#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#define mod 1000000001
#define N 21
using namespace std;
typedef long long ll;
int n;
int a[N][N];
ll f[N][70010];
int vis[100100];
int line[N];


ll calc(int x)
{
    a[1][1] = x;
    int tmp;
    for (int i = 1;; i++)
    {
        if (i != 1)
        {
            a[i][1] = a[i - 1][1] * 2;
            if (a[i][1] > n)
            {
                tmp = i - 1;
                break;
            }
        }
        vis[a[i][1]] = 1;
        for (int j = 2;; j++)
        {
            a[i][j] = a[i][j - 1] * 3;
            if (a[i][j] > n)
            {
                line[i] = j - 1;
                break;
            }
            vis[a[i][j]] = 1;
        }
    }
    line[0] = 1;
    for (int i = 0; i <= tmp; i++)
        for (int j = 0; j < (1 << line[i]); j++)
            f[i][j] = 0;
    line[tmp + 1] = 0, f[tmp + 1][0] = 0;
    f[0][0] = 1;
    for (int i = 0; i <= tmp; i++)
    {
        for (int j = 0; j < (1 << line[i]); j++)
        {
            if (f[i][j])
            {
                if (j & (j >> 1))
                    continue;
                for (int k = 0; k < (1 << line[i + 1]); k++)
                {
                    if (j & k)
                        continue;
                    f[i + 1][k] = (f[i + 1][k] + f[i][j]) % mod;
                }
            }
        }
    }
    return f[tmp + 1][0];
}


int main()
{
    scanf("%d", &n);
    ll ans = 1;
    for (int i = 1; i <= n; i++)
        if (!vis[i])
            ans = ans * calc(i) % mod;
    printf("%lld\n", ans-1);
}