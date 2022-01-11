#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

#define INF 10000000

int
main () 
{
	int n, m;
	cin >> n >> m;

	vector< tuple<int, int, int> > data;

	for(int i = 0; i < m; i ++) {
		int a, b, c;

		cin >> a >> b >> c;

		data.push_back(make_tuple(a, b, c));
	}

	vector<long long> result (n+1, INF);
	result[1] = 0;

    bool cycle = false;
	for(int i = 0; i < n; i ++){
        for (int j = 0; j < data.size(); j ++){
            long long src = get<0>(data[j]);
            long long dst = get<1>(data[j]);
            long long weight = get<2>(data[j]);
            
            if(result[src] == INF){
                continue;
            }

            if(weight + result[src] < result[dst]){
                if(i == n - 1){
                    cycle = true;
                }
                
                result[dst] = result[src] + weight;
            }
        }
    }
    




    if(cycle){
        cout << -1 << endl;
    } 
    else {
        for(int i = 2; i < n+1; i ++) {
            if(result[i] == INF){
                cout << -1 << endl;
            }
            else {
                cout << result[i] << endl;
            }
        }
	}
}
