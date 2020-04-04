#include <bits/stdc++.h>
using namespace std;
#define pb_ push_back
#define eb_ emplace_back
#define mp_ make_pair
//#define endl '\n'
typedef long long ll;
typedef unsigned long long ull;
typedef pair<long,long> pll;
typedef pair<int,int> pii;

const int MN = 1e5+5;

int uf[MN],N,M;
vector<int> ids;

int find(int u){
    if(uf[u]<0)return u;
    return uf[u]=find(uf[u]);
}

void merge(int u, int v){
    u=find(u),v=find(v);
    if(u==v)return;
    if(uf[u]>uf[v])swap(u,v);
    uf[u]+=uf[v],uf[v]=u;
}

int main(){
    cin.tie(0),cout.tie(0),ios::sync_with_stdio(0);
    cin>>N>>M;
    memset(uf,-1,sizeof uf);
    for(int i = 1,a,b; i <=M ; i++){
        cin>>a>>b;
        if(find(a)!=find(b)){
            merge(a,b);
            ids.pb_(i);
        }        
    }
    if(-uf[find(1)]==N){
        for(int i : ids)cout<<i<<endl;
    }
    else cout<<"Disconnected Graph"<<endl;
    
    
}
