def count_grades(grades):
    count_a = 0
    count_b = 0
    count_c = 0
    for grade in grades:
        if grade == 'A':
            count_a += 1
        elif grade == 'B':
            count_b += 1
        else:
            count_c += 1
    return [count_a, count_b, count_c]

grades = ["A", "C", "B", "A", "C", "C"]
print(count_grades(grades))
