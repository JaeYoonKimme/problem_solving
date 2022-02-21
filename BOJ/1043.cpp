//https://www.acmicpc.net/problem/1043

#include <cstdio>
#include <vector>

using namespace std;

vector <int> truth_visitor;
vector < vector<int> > party;
vector <int> visitor;

int 
find (int n) 
{
	if (visitor[n] == n) {
		return n;
	}
	return find(visitor[n]);
}

bool
merge (int a, int b) 
{
	int pa = find(a);
	int pb = find(b);

	if (pa == pb) {
		return false;
	}

	if (pa < pb) {
		visitor[pb] = pa;
	}
	else {
		visitor[pa] = pb;
	}

	return true;
}

int
main ()
{
	int n, m;
	scanf("%d %d", &n, &m);
	
	party = vector < vector<int> > (m + 1);
	visitor = vector <int> (n + 1);

	for (int i = 1; i < n + 1; i ++) {
		visitor[i] = i;	
	}

	int t;
	scanf("%d", &t);

	for (int i = 1; i < t + 1; i ++) {
		int num;
		scanf("%d", &num);

		truth_visitor.push_back(num);
	}

	for (int i = 1; i < m + 1; i ++) {
		int visitor;
		scanf("%d", &visitor);

		for (int j = 0; j < visitor; j ++) {
			int num;
			scanf("%d", &num);

			party[i].push_back(num);

			if(j == 0) {
				continue;
			}
			merge(party[i][j], party[i][j - 1]);
		}
	}

	int count = 0;
	for (auto &p: party) {
		for (auto &v: p) {
			bool check = false;
			for (auto &t: truth_visitor) {
				if (find(t) == find(v)) {
					count ++;
					check = true;
					break;
				}
			}
			if (check) {
				break;
			}
		}
	}

	printf("%d", m - count);


}
