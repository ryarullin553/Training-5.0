def main():
    P, V = map(int, input().split())
    Q, M = map(int, input().split())
    vasya_range = range(P - V, P + V + 1)
    masha_range = range(Q - M, Q + M + 1)
    total_trees = len(set(vasya_range).union(set(masha_range)))
    print(total_trees)


if __name__ == '__main__':
    main()
