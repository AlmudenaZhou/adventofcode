def count_visible_trees(grid_papers):
    new_grid_roll_paper = []
    roll_paper_n = 0
    for row_idx, row_paper in enumerate(grid_papers):
        row_solution = []
        for cell_idx, cell_paper in enumerate(row_paper):
            if cell_paper == "@":
                cell_init = (cell_idx - 1)
                cell_init = 0 if cell_init < 0 else cell_init

                row_init = (row_idx - 1)
                row_init = 0 if row_init < 0 else row_init

                surrounded_paper = [grid_paper[cell_init:(cell_idx + 2)] for grid_paper in grid_papers[row_init:(row_idx + 2)]]
                surrounded_paper = "".join(surrounded_paper)

                number_papers = surrounded_paper.count("@")
                if number_papers <= 4:
                    roll_paper_n += 1
                    row_solution.append("x")
                else:
                    row_solution.append("@")
            else:
                row_solution.append(".")
        new_grid_roll_paper.append("".join(row_solution))
    return new_grid_roll_paper, roll_paper_n


with open("input.txt", "r") as f:
    grid_papers = [line.strip() for line in f.readlines()]

# Part 1
_, roll_paper_n = count_visible_trees(grid_papers)

print(f"Part 1: {roll_paper_n}")

# Part 2
roll_paper_n = 100
all_roll_paper_n = 0
while roll_paper_n > 0:
    grid_papers, roll_paper_n = count_visible_trees(grid_papers)
    all_roll_paper_n += roll_paper_n

print(f"Part 2: {all_roll_paper_n}")
