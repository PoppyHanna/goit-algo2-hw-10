class Teacher:
    def __init__(self, first_name, last_name, age, email, can_teach_subjects):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = set(can_teach_subjects)
        self.assigned_subjects = set()

def create_schedule(subjects, teachers):
    uncovered_subjects = set(subjects)
    schedule = []

    while uncovered_subjects:
        best_teacher = None
        best_covered = set()

        for teacher in teachers:
            can_cover = teacher.can_teach_subjects & uncovered_subjects

            if len(can_cover) > len(best_covered) or (
                len(can_cover) == len(best_covered) and best_teacher and teacher.age < best_teacher.age
            ):
                best_teacher = teacher
                best_covered = can_cover

        if not best_teacher or not best_covered:
            return None

        best_teacher.assigned_subjects = best_covered
        schedule.append(best_teacher)

        uncovered_subjects -= best_covered

    return schedule


if __name__ == '__main__':
    subjects = {'Mathematics', 'Physics', 'Chemistry', 'Computer Science', 'Biology'}

    teachers = [
        Teacher('Olexander', 'Ivanenko', 45, 'o.ivanenko@example.com', {'Mathematics', 'Physics'}),
        Teacher('Maria', 'Petrenko', 38, 'm.petrenko@example.com', {'Chemistry'}),
        Teacher('Sergey', 'Kovalenko', 50, 's.kovalenko@example.com', {'Computer Science', 'Mathematics'}),
        Teacher('Natalia', 'Shevchenko', 29, 'n.shevchenko@example.com', {'Biology', 'Chemistry'}),
        Teacher('Dmitry', 'Bondarenko', 35, 'd.bondarenko@example.com', {'Physics', 'Computer Science'}),
        Teacher('Olena', 'Grytsenko', 42, 'o.grytsenko@example.com', {'Biology'})
    ]

    schedule = create_schedule(subjects, teachers)

    if schedule:
        print("Class schedule:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} years, email: {teacher.email}")
            print(f"Teaches subjects: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("It is not possible to cover all subjects with the available teachers.")
