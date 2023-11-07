from knapsack import create_random_tuples
import timeit

def test_time(function, n = 20, m = 50, step = 1):
    times = []
    list_sizes = []
    for i in range(0, n, step):
        time = 0
        for _ in range(m):
            L = create_random_tuples(length=i)
            start = timeit.default_timer()
            function(L, 200)
            end = timeit.default_timer()
            time += end - start
        times.append(time/m)
        list_sizes.append(i)
    return list_sizes, times