#include <iostream>
#include <vector>

#define INF 1000000009

using namespace std;

int 
main () 
{
	int T;
	cin >> T;

	vector<long long> data (1000000, -1);

	data[4] = 7;
	data[3] = 4;
	data[2] = 2;
	data[1] = 1;

	for(int i = 5; i < 1000000; i ++) {
		data[i] = (data[i - 1] + data[i - 2] + data[i - 3]) % INF;
	}


	vector<int> input (T);	
	for (int i = 0; i < T; i ++) {
		int n;
		cin >> n;

		input[i] = n;
	}

	for (int i = 0; i < T; i ++) {
		cout << data[input[i]] << "\n";
	}
}
