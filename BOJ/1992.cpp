//https://www.acmicpc.net/problem/1992
#include <cstdio>
#include <vector>

using namespace std;

vector< vector<int> > video;

void
compact (int w, int h, int size)
{
	if (size == 1) {
		printf("%d", video[w][h]);
		return;
	}

	int color = video[w][h];
	bool fail_flag = false;
	for (int i = w; i < w + size; i ++) {
		for (int j = h; j < h + size; j ++) {
			if (video[i][j] != color) {
				fail_flag = true;
				break;
			}
		}
		if (fail_flag) {
			break;
		}
	}

	if (fail_flag) {
		printf("(");
		size = size / 2;
		compact (w, h, size);
		compact (w, h + size, size);
		compact (w + size, h, size);
		compact (w + size, h + size, size);
		printf(")");
	}
	else {
		printf("%d", color);
	}
}

int
main ()
{
	int n;
	scanf("%d", &n);

	video = vector< vector<int> > (n, vector<int> (n));

	for (int w = 0; w < n; w ++) {
		for (int h = 0; h < n; h ++) {
			char num;
			scanf(" %c", &num);
			video[w][h] = num - '0';
		}
	}

	compact(0, 0, n);
}
