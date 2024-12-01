def main():
    left: list[int] = []
    right: list[int] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            location_ids = line.strip().split()
            left.append(int(location_ids[0]))
            right.append(int(location_ids[1]))
    similarity = 0
    for location_id in left:
        similarity += location_id * right.count(location_id)
    print(f'similarity score = {similarity}')


if __name__ == '__main__':
    main()
