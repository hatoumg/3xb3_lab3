from knapsack import ks_bottom_up
from knapsack import ks_top_down
from experiment import test_time
import matplotlib.pyplot as plot

def main():
    list_sizes_s, times_s = test_time(ks_bottom_up, n=50, m=100)
    list_sizes_i, times_i = test_time(ks_top_down, n=50, m=100)
    plot.plot(list_sizes_s, times_s)
    plot.plot(list_sizes_i, times_i)
    plot.legend(["Bottom Up","Top Down"])
    plot.xlabel("Number of Items")
    plot.ylabel("Runtime (s)")
    plot.show()

if __name__ == "__main__":
    main()