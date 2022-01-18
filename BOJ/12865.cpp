//https://www.acmicpc.net/problem/12865

#include <iostream>
#include <vector>

using namespace std;

int
main ()
{
	int n, k;
	scanf("%d %d", &n, &k);

	vector< vector<int> >bag(n + 1, vector<int>(k + 1, 0));

	vector< pair<int, int> >items(n);
	for (int i = 0; i < n; i ++) {
		int w, v;
		scanf("%d %d", &w, &v);
		items[i] = make_pair(w,v);
	}

	for (int i = 1; i < n + 1; i ++) {
		int w = items[i - 1].first;
		int v = items[i - 1].second;
		for (int j = 1; j < k + 1; j ++) {
			if(j < w) {
				bag[i][j] = bag[i - 1][j];
				continue;
			}
			else {
				bag[i][j] = max(bag[i - 1][j], v + bag[i - 1][j - w]);
			}
		}
	}

	/*
	for (int i = 0; i < n + 1; i ++) {
		for (int j = 0; j < k + 1; j ++) {
			printf("%d  ", bag[i][j]);
		}
		printf("\n");
	}
	*/

	printf("%d\n",bag[n][k]);
	
}
