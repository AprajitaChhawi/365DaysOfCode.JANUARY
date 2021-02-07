// { Driver Code Starts

// Driver Code
#include<bits/stdc++.h>
#define ll long long int
using namespace std;

 // } Driver Code Ends



// Complete this function
long long int count(long long int n)
{
	long long int table[n+1],i;
	memset(table, 0, sizeof(table));
	table[0]=1;   
	for(i=3;i<=n;i++)
	{
	    table[i]=table[i-3]+table[i];
	}
	for(i=5;i<=n;i++)
	{
	    table[i]=table[i-5]+table[i];
	}
	for(i=10;i<=n;i++)
	{
	    table[i]=table[i-10]+table[i];
	}// If 0 sum is required number of ways is 1.
	
	// Your code here
	
	return table[n];
}

// { Driver Code Starts.



int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		ll n;
		cin>>n;
		cout<<count(n)<<endl;
	}
	return 0;
}  // } Driver Code Ends
