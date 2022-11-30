from functions import lines, timer

@timer
def load_data(file):
    return lines(file)


@timer
def star_one(data_in):
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    pos_x, pos_y = 1, 1
    code = []
    for line in data_in:
        for instr in line:
            if instr == "U":
                pos_y = max(0, pos_y - 1)
            elif instr == "D":
                pos_y = min(2, pos_y + 1)
            elif instr == "L":
                pos_x = max(0, pos_x - 1)
            elif instr == "R":
                pos_x = min(2, pos_x + 1)
        code.append(keypad[pos_y][pos_x])
    return int("".join([str(x) for x in code]))

@timer
def star_two(data_in):
    keypad = [[0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, "A", "B", "C", 0], [0, 0, "D", 0, 0]]
    pos_x, pos_y = 0, 2
    code = []
    for line in data_in:
        for instr in line:
            if instr == "U":
                if pos_y - 1 >= 0 and keypad[pos_y - 1][pos_x]:
                    pos_y -= 1
            elif instr == "D":
                if pos_y + 1 <= 4 and keypad[pos_y + 1][pos_x]:
                    pos_y += 1
            elif instr == "L":
                if pos_x - 1 >= 0 and keypad[pos_y][pos_x - 1]:
                    pos_x -= 1
            elif instr == "R":
                if pos_x + 1 <= 4 and keypad[pos_y][pos_x + 1]:
                    pos_x += 1
            # print((pos_x, pos_y), keypad[pos_y][pos_x])
        # print("\n")
        code.append(keypad[pos_y][pos_x])
    return code


@timer
def main():
    # data = ["ULL", "RRDDD", "LURDL", "UUUUD"]
    data = load_data("day02input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
