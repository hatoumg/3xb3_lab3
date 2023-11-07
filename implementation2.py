from knapsack import ks_brute_force
from knapsack import ks_rec
from experiment import test_time
import matplotlib.pyplot as plot

def main():
    list_sizes_s, times_s = test_time(ks_brute_force)
    list_sizes_i, times_i = test_time(ks_rec)
    plot.plot(list_sizes_s, times_s)
    plot.plot(list_sizes_i, times_i)
    plot.legend(["Brute Force","Recursion"])
    plot.xlabel("Number of Items")
    plot.ylabel("Runtime (s)")
    plot.show()

if __name__ == "__main__":
    main()