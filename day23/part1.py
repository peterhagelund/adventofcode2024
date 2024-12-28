import networkx as nx


def main():
    graph = nx.Graph()
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            c1, c2 = line.strip().split('-')
            graph.add_edge(c1, c2)
    answer = 0
    cliques = nx.enumerate_all_cliques(graph)
    for clique in cliques:
        if len(clique) < 3:
            continue
        if len(clique) > 3:
            break
        count = sum([1 if c.startswith('t') else 0 for c in clique])
        if count > 0:
            answer += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
