#include <iostream>
#include <vector>
#include <utility>
#include <queue>

using namespace std;

int 
main (void) 
{
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int v, e;
	cin >> v >> e;

	v = v + 1;

	int k;
	cin >> k;


	vector< vector< pair<int, int> > > vec (v);


	for (int i = 0; i < e; i ++) {
		int a, b, c;
		cin >> a >> b >> c;
		
		vec[a].push_back(pair<int, int>(b,c));
	}

	vector<int> result (v, 10000000);
	result[k] = 0;

	priority_queue< pair<int,int> > q;

	q.push(pair<int, int>(0, k));

	while(!q.empty()){
		pair<int,int> tmp = q.top();
		q.pop();
		int t = tmp.second;

		if(- tmp.first > result[t])
			continue;

		for(int i = 0; i < vec[t].size(); i++){
			int dst = vec[t][i].first;
			int val = vec[t][i].second;

			if(result[dst] > val + result[t]){
				result[dst] = val + result[t];

				q.push(pair<int, int>(-val, dst) );
			}
		}
	}

	for(int i = 1; i < v; i ++){
		if(result[i] == 10000000){
			cout << "INF" << "\n";
		}
		else {
			cout << result[i] << "\n";
		}
		
	}
}
