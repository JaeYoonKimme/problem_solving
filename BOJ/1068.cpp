//https://www.acmicpc.net/problem/1068

#include <cstdio>
#include <vector>

using namespace std;

vector< vector<int> > tree;
vector< bool > bool_tree;

void
remove (int index)
{
	bool_tree[index] = false;

	for (int i = 0; i < tree[index].size(); i ++) {
		remove(tree[index][i]);
	}

	tree[index].clear();
}

int 
main () 
{
	int n;
	scanf("%d", &n);

	tree = vector< vector<int> > (n);
	bool_tree = vector <bool> (n, true);
	for (int i = 0; i < n; i ++) {
		int node;
		scanf("%d", &node);

		if(node == -1) {
			continue;
		}

		tree[node].push_back(i);
	}

	int to_remove;
	scanf("%d", &to_remove);

	remove(to_remove);

	for (int i = 0; i < n; i ++) {
		for (int j = 0; j < tree[i].size(); j ++) {
			if (tree[i][j] == to_remove) {
				tree[i].erase(tree[i].begin() + j);
			}
		}
	}


	/*	
	for (int i = 0; i < n; i ++) {
		printf("%d - ", i);
		for (int j = 0; j < tree[i].size(); j ++) {
			printf("%d ", tree[i][j]);
		}
		printf("\n");
	}
	*/

	int leaf = 0;
	for (int i = 0; i < n; i ++) {
		if (bool_tree[i] == true) {
			if(tree[i].size() == 0) {
				leaf ++;
			}
		}
	}

	printf("%d\n", leaf);
	

}
