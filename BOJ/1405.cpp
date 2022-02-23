//https://www.acmicpc.net/problem/1405

#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

vector < vector<int> > visited (100, vector<int> (100, 0));;
vector < vector<int> > map (100, vector<int> (100));
vector<double> dir(4, 0);
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int n;
int cnt;

double
go_robot(int w, int h, int depth, double p) 
{
	if (visited[w][h] > 0) {
		return 0;
	}

	if (depth == n) {
		return p;
	}

	visited[w][h] ++;
	double ret = 0;
	for (int i = 0; i < 4; i ++) {
		if (dir[i] == 0) {
			continue;
		}
		ret = ret + go_robot(w + dx[i], h + dy[i], depth + 1, p * dir[i]);
	}

	visited[w][h] --;
	return ret;
}

int
main ()
{
	scanf("%d %lf %lf %lf %lf", &n, &dir[0], &dir[1], &dir[2], &dir[3]);
	//cin >> n >> dir[0] >> dir[1] >> dir[2] >> dir[3];

	dir[0] = dir[0] * 0.01;
	dir[1] = dir[1] * 0.01;
	dir[2] = dir[2] * 0.01;
	dir[3] = dir[3] * 0.01;
	cnt = 0;

	for(auto &d: dir) {
		if (d != 0) {
			cnt ++;
		}
	}

	printf("%0.10lf", go_robot(50, 50, 0, 1));
	//cout.precision(11); cout << go_robot(50, 50, 0)/pow(cnt, n);
}
