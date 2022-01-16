#include <iostream>
#include <vector>

using namespace std;

vector<int> seq;
vector< vector<int> > board;

int
panlinedrome (int a, int b)
{
	if (board[a][b] != -1) {
		return board[a][b];
	}
	if (seq[a] != seq[b]) {
		board[a][b] = 0;
		return 0;
	} 
	else {
		board[a][b] = panlinedrome(a + 1, b - 1);
		return board[a][b];
	}
}

int
main ()
{
	int n, m;
	//cin >> n;
	scanf("%d", &n);

	seq = vector<int> (n + 1);
	board = vector< vector<int> > (n + 1, vector<int>(n + 1, -1));
	
	for (int i = 1; i < n + 1; i ++) {
		//cin >> seq[i];
		scanf("%d", &seq[i]);
		board[i][i] = 1;

		if (i > 1 && seq[i] == seq[i - 1]){
			board[i - 1][i] = 1;
		} 
	}
	//cin >> m;
	scanf("%d", &m);

	vector<int> result (m);

	for (int i = 0; i < m; i ++) {
		int a, b;
		//cin >> a >> b;
		scanf("%d %d", &a, &b);

		result[i] = panlinedrome(a,b);
	}


	for (int i = 0; i < m; i ++) {
		//cout << result[i] << "\n";
		printf("%d\n", result[i]);
	}	
}
