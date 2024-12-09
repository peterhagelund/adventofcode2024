def main():
    with open('puzzle_input.txt', 'rt') as f:
        input = f.read().strip()
    file_id = 0
    is_file = True
    disk_map: list[tuple[int, bool]] = []
    for c in input:
        if is_file:
            id = file_id
            file_id += 1
        else:
            id = -1
        length = int(c)
        for _ in range(length):
            entry = (id, is_file)
            disk_map.append(entry)
        is_file = not is_file
    free_index = 0
    while disk_map[free_index][1] is True:
        free_index += 1
    file_index = len(disk_map) - 1
    while free_index < file_index:
        disk_map[free_index] = disk_map[file_index]
        disk_map[file_index] = (-1, False)
        free_index += 1
        while disk_map[free_index][1] is True and free_index < file_index:
            free_index += 1
        if free_index == file_index:
            break
        file_index -= 1
        while disk_map[file_index][1] is False and file_index > free_index:
            file_index -= 1
        if file_index == free_index:
            break
    answer = 0
    for i in range(len(disk_map)):
        if disk_map[i][1] is False:
            continue
        answer += i * disk_map[i][0]
    print(f'answer = {answer}')


if __name__ == '__main__':
    main()
