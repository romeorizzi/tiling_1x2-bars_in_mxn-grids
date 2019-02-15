static const int H = 0; // horizontal placement of a tile
static const int V = 1; // vertical placement of a tile

int is_tilable(int m, int n) {
   return 1 - (m%2)*(n%2);
} 

void compose_tiling(int m, int n, void place_tile(int row, int col, int dir)) {
   if (n%2 == 0) {
       for(int i = 1; i <= m; i++)
           for(int j = 1; j < n; j += 2)
               place_tile(i,j,H);
   }
   else
       for(int i = 1; i <= m; i += 2)
           for(int j = 1; j < n; j++)
               place_tile(i,j,V);
}
