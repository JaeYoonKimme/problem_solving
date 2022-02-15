//https://www.acmicpc.net/problem/1197

#include<cstdio>
#include<vector>
#include<tuple>
#include<queue>
#include<vector>

using namespace std;

vector<int> set;

int
find (int v) 
{
	if (set[v] == v) {
		return v;
	}
	else {
		return find(set[v]);
	}
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
		set[pb] = pa;
	}
	else {
		set[pa] = pb;
	}
	return true;
}
int
main ()
{
	int v, e;
	scanf("%d %d", &v, &e);

	priority_queue< tuple<int, int, int> > edges;
	set = vector<int> (v + 1);

	int min_weight = 0;

	for (int i = 1; i < v + 1; i ++) {
		set[i] = i;
	}	

	for (int i = 0; i < e; i ++) {
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);

		edges.push(make_tuple(-c, a, b));
	}

	int count = 0;
	while(count != v - 1) {
		auto [w, a, b] = edges.top();
		edges.pop();
	
		if (merge(a, b)) {
			count = count + 1;
			min_weight = min_weight + (-w);
		}
	}
	printf("%d", min_weight);

}
