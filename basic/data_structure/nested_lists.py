if __name__ == '__main__':
    students = [
        ['Harry', 37.21],
        ['Berry', 37.21],
        ['Tina', 37.2],
        ['Akriti', 41],
        ['Harsh', 39]]

    second_highest = sorted(list(set([marks for name, marks in students])))[1]

    for a, b in sorted(students):
        if b == second_highest:
            print(a)

