//https://www.acmicpc.net/problem/2468

#include <iostream>
#include <vector>
#include <memory.h>

using namespace std;

int n;

int dirx[4] = {1, -1, 0, 0};
int diry[4] = {0, 0, -1, 1};

vector< vector<int> > map;
vector< vector<int> > color_map;
//gray = 0
//white = 1


void
dfs_gray (int h, int w, int level)
{
	color_map[h][w] = 0;
	//printf("%d %d - %d\n", h, w, level);
	for(int dir = 0; dir < 4; dir ++) {
		int nh = h + dirx[dir];
		int nw = w + diry[dir];

		if(nh < 1 || nh > n || nw < 1 || nw > n) {
			continue;
		}

		if(color_map[nh][nw] == -1 && map[nh][nw]<= level) {
			dfs_gray(nh, nw, level);
		}

	}
}

void
dfs_white (int h, int w, int level) 
{
	color_map[h][w] = 1;
	//printf("%d %d - %d\n", h, w, level);
	for(int dir = 0; dir < 4; dir ++) {
		int nh = h + dirx[dir];
		int nw = w + diry[dir];

		if(nh < 1 || nh > n || nw < 1 || nw > n) {
			continue;
		}
		
		//printf("nh %d nw %d - %d\n",nh, nw, level);
		if(color_map[nh][nw] == -1 && map[nh][nw] > level) {
			dfs_white(nh, nw, level);
		}
	}

}

int
main ()
{
	scanf("%d", &n);

	map = vector< vector<int> >(n + 1, vector<int>(n + 1));
	color_map = vector< vector<int> >(n + 1, vector<int>(n + 1, -1));


	int max_height = 0;
	for (int i = 1; i < n + 1; i ++) {
		for (int j = 1; j < n + 1; j ++) {
			scanf("%d", &map[i][j]);
			max_height = max(max_height, map[i][j]);
		}
	}

	int max_count = -1;
	for (int level = 0; level < max_height + 1; level ++) {
		int count = 0;
		//printf("[Level %d]\n", level);
		for (int i = 1; i < n + 1; i ++) {
			for (int j = 1; j < n + 1; j ++) {
				if(color_map[i][j] == -1) {
					if(map[i][j] > level) {
						dfs_white(i, j, level);
						count ++;
					}
					else {
						dfs_gray(i, j, level);
					}
				}
			}
		}

		/*	
		for(int a = 1; a < n + 1; a ++) {
			for (int b = 1; b < n + 1; b ++) {
				printf("%d ", color_map[a][b]);
			}
			printf("\n");
		}
		*/
		max_count = max(max_count, count);
		//printf("count = %d\n", count);
		fill(color_map.begin(), color_map.end(), vector<int>(n + 1, -1));
	}


	printf("%d\n", max_count);
}
