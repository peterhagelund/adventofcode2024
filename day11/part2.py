from collections import deque


def calculate_next(stones: list[int]) -> dict[int, tuple[int, int]]:
    next: dict[int, tuple[int, int]] = {}
    queue: deque[int] = deque(stones)
    while queue:
        n = queue.pop()
        if not n in next:
            if n == 0:
                n1 = 1
                next[0] = (n1,)
                queue.append(n1)
            else:
                s = str(n)
                if len(s) % 2 == 0:
                    n1 = int(s[: len(s) // 2])
                    n2 = int(s[len(s) // 2 :])
                    next[n] = (n1, n2)
                    queue.append(n1)
                    queue.append(n2)
                else:
                    n1 = n * 2048
                    next[n] = (n1,)
                    queue.append(n1)
    return next


def main():
    with open('example_input.txt', 'rt') as f:
        stones = [int(s) for s in f.read().strip().split()]
    next = calculate_next(stones)
    print(len(next))
    queue: deque[int] = deque()
    answer = len(stones)
    for s in stones:
        queue.append(s)
        answer += 1
        for blink in range(25):
            print(blink)
            while queue:
                n = queue.pop()
                _next = next[n]
                for nn in _next:
                    answer += 1
                    queue.append(nn)
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
