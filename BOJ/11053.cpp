#include <iostream>
#include <vector>
#include <string>

using namespace std;

int 
main ()
{
	int N;
	cin >> N;

	vector<int> result (N + 1, 0);
	vector<int> data (N + 1);


	for (int i = 0; i < N; i ++) {
		cin >> data[i + 1];
	}
		
	for (int i = N; i > 0; i --) {
		if(i == N) {
			result[i] = 1;
			continue;
		}
		
		int tmp = 1;
		for (int j = i + 1; j < N + 1; j ++) {
			if (data[i] < data[j]) {
				tmp = max(result[j] + 1, tmp);
			}
		}
		result[i] = tmp;
	}


	int f = 0;
	for(int i = 1; i < N + 1; i ++) {
		//cout << result[i] << " ";
		f = max(f, result[i]);
	}
	
	cout << f;

}
