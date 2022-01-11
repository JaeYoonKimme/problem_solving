#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int
main ()
{
	int n, k;
	cin >> n >> k;

	vector<int> arr (n + 1);
	vector<int> sol (k + 1);

	for (int i = 1; i < n + 1; i ++) {
		cin >> arr[i];
	}

	sol[0] = 1;

	for (int i = 1; i < n + 1; i ++) {
		for (int j = 1; j < k + 1; j ++) {
			int tmp = j - arr[i];
			
			if (tmp > -1) {
				sol[j] = sol[j] + sol[tmp];
			}
		}
	}

	cout << sol[k];
}
