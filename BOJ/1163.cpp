//https://www.acmicpc.net/problem/1034

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int
count_zero(string s) 
{
	int count = 0;
	for (int i = 0; i < s.size(); i ++) {
		if (s[i] == '0') {
			count ++;
		}
	}
	return count;
}

int 
main ()
{
	int n, m, k;
	cin >> n >> m;

	vector<string> lamp (n);

	for (int i = 0; i < n; i ++) {
		cin >> lamp[i];
	}
	
	cin >> k;


	int result = 0;
	for (int i = 0; i < n; i ++) {
		int count = 0;
		int num_of_zero = count_zero(lamp[i]);
		if (num_of_zero <= k && num_of_zero%2 == k%2) {
			for (int j = 0; j < n; j ++) {
				if(lamp[i].compare(lamp[j]) == 0) {
					count ++;
				}
			}
		}
		result = max(result, count);
	}

	cout << result;


}
