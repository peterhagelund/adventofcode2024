def main():
    with open('puzzle_input.txt', 'rt') as f:
        stones = [int(s) for s in f.read().strip().split()]
    for _ in range(25):
        i = 0
        while i < len(stones):
            if stones[i] == 0:
                stones[i] = 1
            else:
                s = str(stones[i])
                if len(s) % 2 == 0:
                    s1 = int(s[: len(s) // 2])
                    s2 = int(s[len(s) // 2 :])
                    stones[i] = s1
                    i += 1
                    stones.insert(i, s2)
                else:
                    stones[i] *= 2024
            i += 1
    print(f'answer = {len(stones)}')


if __name__ == '__main__':
    main()
