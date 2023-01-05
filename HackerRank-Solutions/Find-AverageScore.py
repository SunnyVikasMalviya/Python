def findAverageScore(records, name):
    '''
    Function to get average score for a given student name.
    '''
    averageScore = float(sum(records[name])/len(records[name]))
    print("%.2f" % averageScore)
    return

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    findAverageScore(student_marks, query_name)
