//https://www.acmicpc.net/problem/1976

#include <cstdio>
#include <vector>

using namespace std;

int 
main () 
{
	int n, m;
	//cin >> n;
	//cin >> m;
	scanf("%d", &n);
	scanf("%d", &m);

	vector < vector<int> > map (n + 1, vector<int> (n + 1));
	vector <int> plan (m + 1);

	for (int i = 1; i < n + 1; i ++) {
		for (int j = 1; j < n + 1; j ++) {
			//cin >> map[i][j];
			scanf("%d" , &map[i][j]);
			if (i == j) {
				map[i][j] = 1;
			}
		}
	}
	/*
	printf("MAP INFO\n");
	for (int i = 1; i < n + 1; i ++) {
		for (int j = 1; j < m + 1; j ++) {
			printf("from %d to %d = %d\n", i, j, map[i][j]);
		}
	}

	printf("OUR PLAN\n");
	for (int i = 1; i < n + 1; i ++) {
		printf("%d ", plan[i]);
	}
	*/

	//update
	for (int k = 1; k < n + 1; k ++) {
		for (int i = 1; i < n + 1; i ++) {
			for (int j = 1; j < n + 1; j ++) {
				if(map[i][k] && map[k][i]) {
					map[i][j] = 1;
				}
			}
		}
	}

	/*
	printf("UPDATED MAP\n");
	
	for (int i = 1; i < n + 1; i ++) {
		for (int j = 1; j < m + 1; j ++) {
			printf("%d ", map[i][j]);
		}
		printf("\n");
	}
	*/
	bool is_possible = true;
	for (int i = 1; i < m + 1; i ++) {
		//cin >> plan[i];
		scanf("%d", &plan[i]);
		if (i == 1) {
			continue;
		}

		if(!map[plan[i - 1]][plan[i]]) {
			is_possible = false;
		}

	}


	if (is_possible) {
		printf("YES");
	}
	else {
		printf("NO");
	}
}
