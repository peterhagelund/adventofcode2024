import networkx as nx


def main():
    graph = nx.Graph()
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            c1, c2 = line.strip().split('-')
            graph.add_edge(c1, c2)
    largest_clique: list[str] = []
    cliques = nx.find_cliques(graph)
    for clique in cliques:
        if len(clique) > len(largest_clique):
            largest_clique = clique
    largest_clique.sort()
    answer = ','.join(largest_clique)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
