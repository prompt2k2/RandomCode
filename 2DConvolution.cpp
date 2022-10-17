// C++ program for the above approach
// #include <bits/stdc++.h>
using namespace std;

#define ll long long

const ll mod = 998244353, maxn = 3e6;
ll a[maxn], b[maxn];

// Iterative FFT function to compute
// the DFT of given coefficient vector
void fft(ll w0, ll n, ll *a)
{
    // Do bit reversal of the given array
    for (ll i = 0, j = 0; i < n; i++)
    {

        // Swap a[i] and a[j]
        if (i < j)
            swap(a[i], a[j]);

        // Right Shift N by 1
        ll bit = n >> 1;

        for (; j & bit; bit >>= 1)
            j ^= bit;
        j ^= bit;
    }

    // Perform the iterative FFT
    for (ll len = 2; len <= n; len <<= 1)
    {

        ll wlen = w0;
        for (ll aux = n; aux > len; aux >>= 1)
        {
            wlen = wlen * wlen % mod;
        }

        for (ll bat = 0; bat + len <= n; bat += len)
        {

            for (ll i = bat, w = 1; i < bat + len / 2;
                 i++, w = w * wlen % mod)
            {

                ll u = a[i], v = w * a[i + len / 2] % mod;

                // Update the value of a[i]
                a[i] = (u + v) % mod,

                // Update the value
                // of a[i + len/2]
                    a[i + len / 2] = ((u - v) % mod + mod) % mod;
            }
        }
    }
}

// Function to find (a ^ x) % mod
ll binpow(ll a, ll x)
{
    // Stores the result of a ^ x
    ll ans = 1;

    // Iterate over the value of x
    for (; x; x /= 2, a = a * a % mod)
    {

        // If x is odd
        if (x & 1)
            ans = ans * a % mod;
    }

    // Return the resultant value
    return ans;
}

// Function to find the
// inverse of a % mod
ll inv(ll a) { return binpow(a, mod - 2); }

// Function to find the
// convolution of two arrays
void findConvolution(ll a[], ll b[], ll n, ll m)
{
    // Stores the first power of 2
    // greater than or equal to n + m
    ll _n = 1ll << 64 - __builtin_clzll(n + m);

    // Stores the primitive root
    ll w = 15311432;
    for (ll aux = 1 << 23; aux > _n; aux >>= 1)
        w = w * w % mod;

    // Convert arrays a[] and
    // b[] to point value form
    fft(w, _n, a);
    fft(w, _n, b);

    // Perform multiplication
    for (ll i = 0; i < _n; i++)
        a[i] = a[i] * b[i] % mod;

    // Perform inverse fft to
    // recover final array
    fft(inv(w), _n, a);
    for (ll i = 0; i < _n; i++)
        a[i] = a[i] * inv(_n) % mod;

    // Print the convolution
    for (ll i = 0; i < n + m - 1; i++)
        cout << a[i] << " ";
}

// Driver Code
int main()
{
    // Given size of the arrays
    ll N = 4, M = 5;

    // Fill the arrays
    for (ll i = 0; i < N; i++)
        a[i] = i + 1;

    for (ll i = 0; i < M; i++)
        b[i] = 5 + i;

    findConvolution(a, b, N, M);

    return 0;
}
