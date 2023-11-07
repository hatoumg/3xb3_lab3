import random

def create_random_tuples(length = 20, max_weight = 75, max_value = 2000, min_weight = 50, min_value = 1000):
    return [(random.randint(min_weight, max_weight), random.randint(min_value, max_value)) for _ in range(length)]


def ks_brute_force(items, capacity):
    l = power_set(items)
    m = 0
    for i in l:
        w, v = 0,0
        for index in i:
            w += index[0]
            v += index[1]
            if w <= capacity and v > m:
                m = v
    return m

def power_set(L):
    r = [[]]
    for i in L:
        subset = [s + [i] for s in r]
        r.extend(subset)
    return r

def ks_rec(items, capacity):
    if capacity == 0:
        return 0
    if len(items) == 0:
        return 0
    if capacity - items[-1][0]>0:
        return max(ks_rec(items[:-1], capacity - items[-1][0]) + items[-1][1],ks_rec(items[:-1], capacity))
    else:
        return ks_rec(items[:-1], capacity)
    

def ks_bottom_up(items, capacity):
    sp = [[0 for j in range(capacity + 1)] for i in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for j in range(1, capacity + 1):
            if items[i-1][0] > j:
                sp[i][j] = sp[i-1][j]
            else:
                sp[i][j] = max(sp[i-1][j], sp[i - 1][j - items[i-1][0]] + items[i-1][1])
    return sp[len(items)][capacity]

def ks_top_down(items, capacity):
    sp = {}
    for i in range(len(items) + 1):
        sp[(i,0)] = True
    for i in range(capacity + 1):
        sp[(0,i)] = i == 0
    ks_top_down2(items, len(items), capacity, sp)
    return sp[(len(items), capacity)]

def ks_top_down2(items, i, capacity, sp):
    if items[i - 1][0] > capacity:
        if not (i - 1, capacity) in sp:
            ks_top_down2(items, i - 1, capacity, sp)
        sp[(i, capacity)] = sp[(i - 1, capacity)]
    else:
        if not (i - 1, capacity) in sp:
            ks_top_down2(items, i - 1, capacity, sp)
        if not (i - 1, capacity - items[i - 1][0]) in sp:
            ks_top_down2(items, i - 1, capacity - items[i-1][0], sp)
        sp[(i,capacity)] = max(sp[(i-1, capacity)], sp[(i-1, capacity-items[i-1][0])] + items[i-1][1])

def main():
    if __name__ == "__main__":
        p = [(57, 1303), (70, 1487), (63, 1948), (52, 1716), (50, 1712), (68, 1752), (68, 1981), (69, 1042), (55, 1536), (68, 1280)]
        print(ks_brute_force(p, 200))