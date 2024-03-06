from memory_profiler import profile


@profile
def main():
    # P - номер дерева, у которого стоит ведро Васи
    # V - на сколько деревьев он может от него удаляться
    P, V = map(int, input().split())
    # P - номер дерева, у которого стоит ведро Маши
    # V - на сколько деревьев она может от него удаляться
    Q, M = map(int, input().split())
    vasya_range = range(P - V, P + V + 1)
    masha_range = range(Q - M, Q + M + 1)
    total_trees = set(vasya_range) | set(masha_range)
    print(len(total_trees))


if __name__ == '__main__':
    main()
