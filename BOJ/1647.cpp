#include <cstdio>
#include <vector>
#include <queue>
#include <tuple>

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
	int n, m;
	scanf("%d %d", &n, &m);
	set = vector<int> (n + 1);
	for (int i = 0; i < n + 1; i ++) {
		set[i] = i;
	}

	priority_queue< tuple<int, int, int> > pq;
	for (int i = 0; i < m; i ++) {
		int a, b, c;
		scanf("%d %d %d", &a, &b, &c);

		pq.push(make_tuple(-c, a, b));
	}

	int count = 0;
	int max_val = 0;
	int result = 0;
	while (count != n - 1) {
		auto [w, a, b] = pq.top();
		pq.pop();

		if (merge(a, b)) {
			result = result + (-w);
			max_val = max(max_val, (-w));
			count ++;
		}
	}

	printf("%d", result - max_val);








}
