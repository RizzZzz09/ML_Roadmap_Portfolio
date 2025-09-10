from collections import namedtuple


def main():
    Student = namedtuple("Student", ["name", "grade", "subject"])

    sdt1 = Student("Mark", 97, "Math")
    sdt2 = Student("Kirill", 74, "Math")
    sdt3 = Student("Ivan", 21, "Math")
    sdt4 = Student("Victor", 85, "Math")
    sdt5 = Student("Dima", 53, "Math")
    students_list = [sdt1, sdt2, sdt3, sdt4, sdt5]

    sort_students_list_math = sorted(
        [student for student in students_list if student.subject == "Math"],
        key=lambda item: item.grade,
        reverse=True,
    )

    for index, student in enumerate(sort_students_list_math[:3], 1):
        print(
            f"{index}. Name: {student.name} - Grade: {student.grade} - Subject: {student.subject}"
        )


if __name__ == "__main__":
    main()
