from dataclasses import dataclass


@dataclass
class Student:
    first_name: str
    last_name: str
    marks: list[int]

    def average(self) -> float:
        return sum(self.marks)/len(self.marks)


def main():
    with open("src_14.txt", "r") as file:
        data = file.readlines()

    students: list[Student] = []
    for line in data:
        first_name, last_name, *marks = line.split()
        students.append(Student(first_name, last_name, [int(mark) for mark in marks]))

    for student in students:
        if student.average() < 5:
            print(f'{student.first_name} {student.last_name:<7} {student.average():.2f}')

    average_marks = [student.average() for student in students]
    print(f'\nСредний бал по классу: {sum(average_marks)/len(average_marks):.2f}')

    with open("new_file.txt", "w") as file:
        for student in students:
            name = f"{student.last_name} {student.first_name[0]}.".ljust(15)
            print(f"{name} {student.average():.2f}", file=file)


if __name__ == '__main__':
    main()