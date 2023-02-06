groupmates = [
    {
        "name": "Настя",
        "surname": "Каморина",
        "exams": ["Информатика", "Высшая математика", "История"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Настя",
        "surname": "Львова",
        "exams": ["Высшая математика", "АиГ", "История"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Карпова",
        "surname": "Екатерина",
        "exams": ["Философия", "ВВиТ", "АиГ"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Даваасурэн",
        "surname": "Улзийсурэн",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Владимр",
        "surname": "Нюдлеев",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Захаров",
        "surname": "Крилл",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    }
]


def print_students(students):
    print(u"Имя".ljust(15), u"Фамилия".ljust(10), u"Экзамены".ljust(50), u"Оценки".ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10), str(student["exams"]).ljust(50), str(student["marks"]).ljust(20))


print_students(groupmates)
