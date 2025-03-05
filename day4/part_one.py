from aocd import get_data, submit

data = get_data(day=4, year=2024)


def part_one():
    grid = data.splitlines()

    DIRECTIONS = [
        (0, 1),  # Horizontal right
        (1, 0),  # Vertical down
        (1, 1),  # Diagonal down-right
        (1, -1),  # Diagonal down-left
        (0, -1),  # Horizontal left
        (-1, 0),  # Vertical up
        (-1, -1),  # Diagonal up-left
        (-1, 1)  # Diagonal up-right
    ]

    def count_occurrences(grid, word):
        rows, cols = len(grid), len(grid[0])
        word_len = len(word)
        count = 0

        for r in range(rows):
            for c in range(cols):
                for dr, dc in DIRECTIONS:
                    # Check if the word fits in the current direction
                    if 0 <= r + (word_len - 1) * dr < rows and 0 <= c + (word_len - 1) * dc < cols:
                        found = True
                        for k in range(word_len):
                            nr, nc = r + k * dr, c + k * dc
                            if grid[nr][nc] != word[k]:
                                found = False
                                break
                        if found:
                            count += 1
        return count

    return count_occurrences(grid, "XMAS")


submit(part_one(), part='a', day=4, year=2024)
