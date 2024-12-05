def data(filepath):
    with open(filepath, 'r') as file:
        lines = [line.strip() for line in file]

    # Make sure data length is the same, otherwise it's hard to iterate over a grid.
    max_length = max(len(line) for line in lines)
    puzzle = [list(line.ljust(max_length)) for line in lines]

    return puzzle


def find_christmas(grid, word):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    word_len = len(word)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),  # Up, Down, Left, Right
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]  # Diagonals

    count = 0

    def search_from(x, y, x2, y2):
        for i in range(word_len):
            nx, ny = x + i * x2, y + i * y2
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                return False
            if grid[nx][ny] != word[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            for x2, y2 in directions:
                if search_from(x, y, x2, y2):
                    count += 1

    return count


print(find_christmas(data("data.txt"), "XMAS"))
