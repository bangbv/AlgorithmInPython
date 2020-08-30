if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    ss = 0
    total = 0
    for s in student_marks[query_name]:
        ss = ss + s
        total = total+1
    print(ss/total)