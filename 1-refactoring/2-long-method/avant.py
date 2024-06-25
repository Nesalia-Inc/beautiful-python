def process_students(students: list[dict], subject: str) -> dict:
    total = 0
    count = 0
    best_student = None
    highest_score = 0
    summary = ""

    for student in students:
        if subject in student['grades']:
            score = student['grades'][subject]
            total += score
            count += 1
            if score > highest_score:
                highest_score = score
                best_student = student['name']

    average = total / count if count > 0 else 0

    summary += f"Average score in {subject}: {average:.2f}\n"
    summary += f"Best student in {subject}: {best_student} with score {highest_score}\n"

    return {
        'average': average,
        'best_student': best_student,
        'highest_score': highest_score,
        'summary': summary
    }



if __name__ == '__main__':
    students = [
        {
            'name': 'Alice',
            'grades': {
                'math': 85,
                'science': 92,
                'literature': 78
            }
        },
        {
            'name': 'Bob',
            'grades': {
                'math': 90,
                'science': 88,
                'literature': 82
            }
        },
        {
            'name': 'Charlie',
            'grades': {
                'math': 95,
                'science': 85,
                'literature': 80
            }
        }
    ]

    print(process_students(students, "math"))