from aocd import get_data, submit

data = get_data(day=4, year=2024)


def part_two():
    grid = data.splitlines()

    def count_x_mas(grid):
        rows, cols = len(grid), len(grid[0])
        count = 0

        def is_mas(x, y, dx, dy):
            try:
                return (grid[x][y] == 'M' and
                        grid[x + dx][y + dy] == 'A' and
                        grid[x + 2 * dx][y + 2 * dy] == 'S')
            except IndexError:
                return False

        for r in range(1, rows - 1):
            for c in range(1, cols - 1):
                if (is_mas(r - 1, c - 1, 1, 1) and  # Top-left to bottom-right
                        is_mas(r - 1, c + 1, 1, -1)):  # Top-right to bottom-left
                    count += 1

                if (is_mas(r - 1, c + 1, 1, -1) and  # Top-right to bottom-left
                        is_mas(r - 1, c - 1, 1, 1)):  # Top-left to bottom-right
                    count += 1

        return count

    # Count the occurrences of "X-MAS"
    return count_x_mas(grid)


submit(part_two(), part='b', day=4, year=2024)
