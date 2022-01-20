//https://www.acmicpc.net/problem/2531

#include <cstring>
#include <cstdio>

using namespace std;

int
main ()
{
	int n, d, k, c;
	scanf("%d %d %d %d", &n, &d, &k, &c);

	vector<int> susi (n);

	for (int i = 0; i < n; i ++) {
		scanf("%d", &(susi[i]));
	}

	int result = 0;
	bool * kinds = new bool[d + 1];
	memset(kinds, false, d + 1);

	for (int i = 0; i < n; i ++) {
		int dup = 0;
		int coupon = 1;
		for(int j = i; j < i + k; j ++) {
			if(kinds[susi[j % n]] == false){
				kinds[susi[j % n]] = true;
			}
			else {
				dup ++;
			}
		}
		if(kinds[c]){
			coupon = 0;
		}
		result = max(result, (k - dup + coupon));
		memset(kinds, false, d + 1);
	}

	printf("%d\n", result);
}
