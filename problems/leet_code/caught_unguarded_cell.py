def countUnguarded(m, n, guards, walls):
    """
    :type m: int
    :type n: int
    :type guards: List[List[int]]
    :type walls: List[List[int]]
    :rtype: int
    """
    grid = [[0 for c in range(n)] for r in range(m)]
    def in_bounds(i, j):
        return 0<=i<m and 0<=j<n
    guarded = 0
    for i, j in guards+walls:
        grid[i][j] = 1 
        guarded += 1
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for gi, gj in guards:
        for di, dj in directions:
            curr_i = gi + di
            curr_j = gj + dj
            while in_bounds(curr_i, curr_j) and grid[curr_i][curr_j] != 1:
                if grid[curr_i][curr_j] == 0:
                    guarded += 1
                grid[curr_i][curr_j] = 2
                curr_i += di
                curr_j += dj
    return m*n - guarded