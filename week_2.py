def count_substrings(S):
    c = {}
    for x in S: 
        c[x] = c.get(x, 0) + 1
    return sum(v * (v + 1) // 2 for v in c.values())

if __name__ == "__main__":
    print(count_substrings("abcdefedcba"))