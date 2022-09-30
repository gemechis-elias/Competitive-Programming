#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
    int m,n;
    cin>>m>>n;
    if(m%2==0)
    {
        if(n%2==0)
        {
            cout<<(n/2)*m<<endl;
        }
        else
        {
            cout<<(m/2)*n<<endl;
        }
    }
    else
    {
        if(n%2==0)
        {
            cout<<(n/2)*m<<endl;
        }
        else
        {
            cout<<((max(m,n)/2)*min(m,n))+(min(m,n)/2)<<endl;
        }
    }
}
