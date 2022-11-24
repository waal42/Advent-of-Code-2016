from functions import comma_separated_line, timer


@timer
def load_data(file):
    return comma_separated_line(file)


@timer
def star_one(data_in):
    orientation = 0
    pos_x = 0
    pos_y = 0
    for move in data_in:
        if move[0] == "L":
            orientation = (orientation - 90) % 360
        elif move[0] == "R":
            orientation = (orientation + 90) % 360
        else:
            print("error")
        steps = int(move[1:])
        if orientation == 0:
            pos_y += steps
        elif orientation == 90:
            pos_x += steps
        elif orientation == 180:
            pos_y -= steps
        elif orientation == 270:
            pos_x -= steps
        else:
            print("error")
        # print(orientation, pos_x, pos_y)
    return abs(pos_x) + abs(pos_y)


@timer
def star_two(data_in):
    orientation = 0
    pos_x = 0
    pos_y = 0
    visited = [(pos_x, pos_y)]
    solution = 0
    for move in data_in:
        if move[0] == "L":
            orientation = (orientation - 90) % 360
        elif move[0] == "R":
            orientation = (orientation + 90) % 360
        else:
            print("error")
        steps = int(move[1:])
        for _ in range(steps):
            if orientation == 0:
                pos_y += 1
            elif orientation == 90:
                pos_x += 1
            elif orientation == 180:
                pos_y -= 1
            elif orientation == 270:
                pos_x -= 1
            else:
                print("error")
            if (pos_x, pos_y) in visited:
                solution = abs(pos_x) + abs(pos_y)
                break
            else:
                visited.append((pos_x, pos_y))
        if solution:
            break
    # print(visited)
    return solution


@timer
def main():
    # data = ["R8", "R4", "R4", "R8"]
    data = load_data("day01input.txt")
    print(star_one(data))
    print(star_two(data))


if __name__ == "__main__":
    main()
