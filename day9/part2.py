def main():
    with open('puzzle_input.txt', 'rt') as f:
        input = f.read().strip()
    disk_map: list[tuple[int, bool, int]] = []
    file_id = 0
    is_file = True
    for c in input:
        length = int(c)
        if is_file:
            entry = (file_id, True, length)
            file_id += 1
        else:
            entry = (-1, False, length)
        is_file = not is_file
        disk_map.append(entry)
    file_index = len(disk_map) - 1
    while file_index > 0:
        if disk_map[file_index][1] is True:
            length = disk_map[file_index][2]
            for free_index in range(file_index):
                if disk_map[free_index][1] is True:
                    continue
                capacity = disk_map[free_index][2]
                if capacity >= length:
                    disk_map[free_index] = (-1, False, capacity - length)
                    disk_map.insert(free_index, disk_map[file_index])
                    disk_map[file_index + 1] = (-1, False, length)
                    break
        file_index -= 1
    answer = 0
    index = 0
    for entry in disk_map:
        (id, is_file, length) = entry
        for i in range(length):
            if is_file:
                answer += index * id
            index += 1
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
