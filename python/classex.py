students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english":88, "science":95 },
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92},
]
print("이름", "총점","평균", sep="\t")
for student in students:
    score_sum = student["korean"] + student["math"] + student["english"] + student["science"]
    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep="\t")




def create_student(name, korean, math, english, science):
    return {
        "name" : name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

def student_get_sum(student):
    return student["korean"] + student["math"] + student["english"] + student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
           student["name"],
           student_get_sum(student),
           student_get_average(student))

students = [
    create_student("윤인성", 87,98,88,95),
    create_student("연하진", 92,98,96,98),
    create_student("구지연", 76,96,94,90),
    create_student("나선주", 98,92,96,92),
    create_student("윤아린", 95,98,92,98),
    create_student("윤명월", 64,88,92,92),
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))


class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        def get_sum(self):
            return self.korean + self.math + self.english + self.science

        def get_average(self):
            return self.get_sum() / 4

        def to_string(self):
            return "{}\t{}t{}".format(self.name,self.get_sum(),self.get_average())

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 92, 98),
    Student("윤명월", 64, 88, 92, 92),
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    print(student.to_string())