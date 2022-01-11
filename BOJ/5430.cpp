#include <iostream>
#include <deque>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int 
main ()
{
	int T;
	cin >> T;

	for (int i = 0; i < T; i ++) {
		string p;
		cin >> p;

		int n;
		cin >> n;

		string s;
		cin >> s;

		s.replace(s.find("["), 1, "");
		s.replace(s.find("]"), 1, "");

		istringstream ss(s);

		deque<string> dq;

		string token;
		while (getline(ss, token, ',')) {
			dq.push_back(token);
		}
		bool error = false;
        bool reverse = false;
		for (int j = 0; j < p.size(); j ++) {
			if(p[j] == 'R') {
				reverse = !reverse;
			}
			else {
				if(dq.size() == 0){
					cout << "error\n";
					error = true;
					break;
				}
                if(reverse){
				    dq.pop_back();
                }else {
                    dq.pop_front();
                }
			}
		}
		
		if(error) {
			continue;
		}

		cout << "[";
		for (int j = 0; j < dq.size(); j ++) {
            if(reverse)
			    cout << dq[dq.size() - j - 1];
            else 
                cout << dq[j];
            
			if(j != dq.size() - 1) {
				cout << ","; 
			}
		}
		cout << "]\n";
	}
}
