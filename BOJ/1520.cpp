#include <iostream>
#include <vector>

using namespace std;

int success_count = 0;
vector < vector <int> > map;
vector < vector <bool> > visited;
vector < vector <int> > complete;

int diry[4] = {1, -1, 0, 0};
int dirx[4] = {0, 0, 1, -1};

int m, n;

int
dfs (int y, int x)
{
	if(y == m && x == n) {
		complete[y][x] = 1;
		return 1;
	}

	visited[y][x] = true;


	int cnt = 0;
	for (int i = 0; i < 4; i ++) {
		int tmpy = y + diry[i];
		int tmpx = x + dirx[i];

		if (tmpy > m || tmpy < 1 || tmpx > n || tmpx < 1) {
			continue;
		}

		if (visited[tmpy][tmpx] == true) {
			continue;
		}

		if (complete[tmpy][tmpx] != -1 && map[tmpy][tmpx] < map[y][x]) {
			cnt = cnt + complete[tmpy][tmpx];
			continue;
		}

		if (map[tmpy][tmpx] < map[y][x]) {
			cnt = cnt + dfs(tmpy, tmpx);
		}
	}
	visited[y][x] = false;
	complete[y][x] = cnt;
	return complete[y][x]; 
}

int 
main ()
{
	cin >> m >> n;

	map = vector < vector <int> >(m + 1 , vector<int>(n + 1, 0));

	visited = vector < vector <bool> > (m + 1, vector<bool>(n + 1, false));

	complete = vector < vector <int> > (m + 1, vector<int>(n + 1, -1));

	for (int i = 1; i < m + 1; i ++) {
		for (int j = 1; j < n + 1; j ++) {
			cin >> map[i][j];	
		}
	}

	cout << dfs(1, 1) << "\n";

	/*	
	for (int i = 1; i < m + 1; i ++) {
		for (int j = 1; j < n + 1; j ++) {
			cout << complete[i][j] << " ";
		}
		cout << "\n";
	}
	*/
	//cout << complete[1][1];
}
