def main():
    left: list[int] = []
    right: list[int] = []
    with open('puzzle_input.txt', 'rt') as f:
        for line in f:
            location_ids = line.strip().split()
            left.append(int(location_ids[0]))
            right.append(int(location_ids[1]))
    left.sort()
    right.sort()
    answer = 0
    for i in range(len(left)):
        distance = abs(left[i] - right[i])
        answer += distance
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
