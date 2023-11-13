def num_of_wc_runs(n, m):
    #wc[i][j] represents the worst case for i bricks and j forces
    wc = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(len(wc)):
        wc[i][1] = 1
        wc[i][0] = 0
    for i in range(n+1):
        wc[1][i] = i
    for i in range(2, m+1):
        for j in range(2, n+1):
            wc[i][j] = 999999999999999
            for x in range(1, j + 1):
                min = 1 + max(wc[i-1][x-1], wc[i][j-x])
                if min < wc[i][j]:
                    wc[i][j] = min
    return wc[m][n]

def next_setting(n,m):
    min_wc = num_of_wc_runs(n,m)

    setting = [[0 for j in range(min_wc+1)] for i in range(m+1)]
    for i in range(len(setting)):
        setting[i][1] = 1
    for i in range(min_wc+1):
        setting[1][i] = i
    for i in range(2,m+1):
        for j in range(2,min_wc+1):
            setting[i][j] = 1 + setting[i-1][j-1] + setting[i][j-1]
    return setting[m-1][min_wc-1] + 1

print(num_of_wc_runs(100, 3))
print(next_setting(100,3))