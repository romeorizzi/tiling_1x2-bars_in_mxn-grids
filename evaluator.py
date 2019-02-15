import turingarena as ta

H = 0   # horizontal placement of a tile
V = 1   # vertical placement of a tile


def test_case(m,n):
    with ta.run_algorithm(ta.submission.source) as p:
        print(f"case (m={m}, n={n})")
        res = p.functions.is_tilable(m, n)
        print(f"got {res}")
        if res != 1 - (m % 2) * (n %2 ):
            if res == 0:
                print("According to your is_tilable function, the %dx%d-grid is not tilable. However, look at this: " % (m,n) )
                display_a_tiling(m,n)
                ta.goals["decision"] = False
                if m1 == 1:
                    ta.goals["decision_m1"] = False
            if res != 0:
                print("According to your is_tilable function, the %dx%d-grid is tilable. Are you sure?" )
        
        if (m % 2) * (n %2 ) == 1:
            return

        posed_tiles = 0
        covered = [ [False for _ in range(n) ] for _ in range(m) ]
        def place_tile(row,col,dir):
            nonlocal posed_tiles
            nonlocal covered
            row, col = row - 1, col - 1
            if dir == H:
                cells = [ [row,col], [row,col+1] ]
            else:    
                cells = [ [row,col], [row+1,col] ]
            posed_tiles += 1
            for cell in cells:
                def turn_off_goal_flags():
                    ta.goals["one_tiling"] = False
                    if m == 1:
                        ta.goals["one_tiling_m1"] = False

                row = cell[0]
                col = cell[1]
                if row < 0 or col < 0 or row >= m or col >= n:
                    print("La tua tessera fuoriesce dalla scacchiera nella cella (%d,%d)." % (row+1,col+1))
                    turn_off_goal_flags()
                    return
                if covered[row][col]:
                    print("Due delle tue tegole coprono la cella (%d,%d)." % (row+1,col+1))
                    turn_off_goal_flags()
                    return
                covered[row][col] = True
                if 2*posed_tiles == m*n:
                    print("Complimenti! Hai riempito perfettamente la griglia. Il tuo tiling è stato verificato.")

        print("mostra il tiling")
        p.procedures.compose_tiling(m, n, callbacks = [place_tile] )

def run_all_test_cases():
    for m in range(1,5):
        for n in range(1,5):
            test_case(m,n)
        
run_all_test_cases()

ta.goals.setdefault("decision_m1", True)
ta.goals.setdefault("decision", True)
ta.goals.setdefault("one_tiling_m1", True)
ta.goals.setdefault("one_tiling", True)

print(ta.goals)

