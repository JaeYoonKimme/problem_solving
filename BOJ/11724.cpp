#include<iostream>
#include<vector>

using namespace std;

vector< vector <int> > edges(1001);
vector< bool > visited(1001, false);
vector< int > counter(1001, 0);

int cnt = 0;

void
dfs (int src)
{
	visited[src] = true;
	counter[src] = cnt;
	for (int i = 0; i < edges[src].size(); i ++) {
		int dst = edges[src][i];
		if(visited[dst] != true) {
			dfs(dst);
		}
	}
}


int 
main ()
{
	int N, M;
	cin >> N >> M;

	int start = 0;
	for (int i = 0; i < M; i ++) {
		int src, dst;
		cin >> src >> dst;

		edges[src].push_back(dst);
		edges[dst].push_back(src);
	}

	
	for (int i = 1; i < N + 1; i ++) {
		if(counter[i] == 0) {
			cnt = cnt + 1;
			dfs(i);
		}
	}
	
	
	cout << cnt;
}

