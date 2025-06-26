def calculate_perimeter(papers):
    grid = [[0] * 101 for _ in range(101)]

    for x, y in papers:
        for i in range(x, x + 10):
            for j in range(y, y + 10):
                grid[i][j] = 1

    perimeter = 0
    for i in range(101):
        for j in range(101):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == 100 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == 100 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter

n = int(input())
papers = [tuple(map(int, input().split())) for _ in range(n)]

print(calculate_perimeter(papers))