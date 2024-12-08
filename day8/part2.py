def find_antinodes(locations: list[tuple[int, int]], height: int, width: int) -> set[tuple[int, int]]:
    antinodes: set[tuple[int, int]] = set(locations)
    for i in range(len(locations)):
        for j in range(len(locations)):
            if j == i:
                continue
            a1 = locations[i]
            a2 = locations[j]
            dy = a1[0] - a2[0]
            dx = a1[1] - a2[1]
            y, x = a1[0] + dy, a1[1] + dx
            while y >= 0 and y < height and x >= 0 and x < width:
                antinodes.add((y, x))
                y += dy
                x += dx
            y, x = a2[0] - dy, a2[1] - dx
            while y >= 0 and y < height and x >= 0 and x < width:
                antinodes.add((y, x))
                y -= dy
                x -= dx
    return antinodes


def main():
    antennas: dict[str, list[tuple[int, int]]] = {}
    map: list[str] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            map.append(line.strip())
    height = len(map)
    width = len(map[0])
    for y in range(height):
        for x in range(width):
            c = map[y][x]
            if c == '.':
                continue
            locations = antennas.get(c)
            if locations is None:
                locations = [(y, x)]
                antennas[c] = locations
            else:
                locations.append((y, x))
    antinodes: set[tuple[int, int]] = set()
    for locations in antennas.values():
        antinodes.update(find_antinodes(locations, height, width))
    print(f'answer = {len(antinodes)}')


if __name__ == '__main__':
    main()
