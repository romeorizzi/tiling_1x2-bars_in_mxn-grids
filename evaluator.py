from turingarena import run_algorithm, submission, evaluation

goals = dict( decision_m1 = True, decision = True, one_tiling_m1 = True, one_tiling = True )

def test_case(m,n):
    with run_algorithm(submission.source) as p:
        res = p.functions.is_tilable(m, n)
        if res != 1 - (m % 2) * (n %2 ):
            if res == 0:
                print("According to your is_tilable function, the %dx%d-grid is not tilable. However, look at this: " % (m,n) )
                display_a_tiling(m,n)
                goals[decision] = False
                if m1 == 1:
                    goals[decision_m1] = False
            if res != 0:
                print("According to your is_tilable function, the %dx%d-grid is tilable. Are you sure?" )
                
        if (m % 2) * (n %2 ) == 1:
            return

        posed_tiles = 0
        covered = [ [False]*n ]*m
        def place_tile(row,col,dir):
            nonlocal posed_tiles
            def turn_off_goal_flags():
                goals[ one_tiling] = False
                if m1 == 1:
                    goals[ one_tiling_m1] = False

            posed_tiles += 1
            if covered[row][col]:
                print("Due delle tue tegole coprono la cella (%d,%d)." % (row,col))
                turn_off_goal_flags()
                return
            covered[row][col] = True
            if dir:
                col = col+1
            else:    
                row = row+1
            if covered[row][col]:
                print("Due delle tue tegole coprono la cella (%d,%d)." % (row,col))
                turn_off_goal_flags()
                return
            covered[row][col] = True
            if 2*posed_tiles == m*n:
                print("Complimenti! Hai riempito perfettamente la griglia. Il tuo tiling è stato verificato.")

        
        p.procedures.compose_tiling(m, n, callbacks = [place_tile] )

def run_all_test_cases():
    for m in range(1,5):
        for n in range(1,5):
            test_case(m,n)
        
run_all_test_cases()
        
print(goals)

