#include <iostream>
#include <vector>

using namespace std;

#define INF 100000000

int 
main ()
{
	int n;
	cin >> n;

	vector<int> data (n + 1);
	vector<int> history (n + 1);
	data[1] = 0;
	data[2] = 1;
	data[3] = 1;

	history[1] = 3;
	history[2] = 2;
	history[3] = 1;


	for(int i = 4; i < n + 1; i ++) {
		int a = INF;
		int b = INF;
		int c;
		if(i % 3 == 0) {
			a = data[i/3];
		} 
		if(i % 2 == 0) {
			b = data[i/2];
		}
		c = data[i-1];

		data[i] = min(a,min(b,c)) + 1;

		if(data[i] == a + 1) {
			history[i] = 1;
		}	
		else if(data[i] == b + 1) {
			history[i] = 2;
		}
		else if(data[i] == c + 1){
			history[i] = 3;
		}
	}

	cout << data[n] << "\n";

	/*
	for(int i = 1; i < n + 1; i ++) {
		cout << history[i] << " ";
	}
	*/
	
	cout << n << " ";
	while(n != 1) {
		if(history[n] == 1) {
			n = n / 3;
			cout << n << " ";
			continue;
		} 
		else if(history[n] == 2) {
			n = n / 2;
			cout << n << " ";
			continue;
		}
		else if(history[n] == 3){
			n = n - 1;
			cout << n << " ";
		}
	}	
}
