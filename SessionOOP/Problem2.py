class Ward:
    def __init__(self, name):
        """
        Constructor for Ward class.
        """
        self.__name = name
        self.__list_person = []

    def add_person(self, person):
        """
        Add a person to the ward.
        """
        self.__list_person.append(person)

    def describe(self):
        """
        Print the details of the ward and all people in it.
        """
        print(f"Ward Name: {self.__name}")
        for person in self.__list_person:
            person.describe()


class Student:
    def __init__(self, name, yob, grade):
        self.__name = name
        self.__yob = yob
        self.__grade = grade

    def describe(self):
        """
        Print the details of the student.
        """
        print(f"Student - Name: {self.__name} - Year: {self.__yob} - Grade: {self.__grade}")


class Doctor:
    def __init__(self, name, yob, specialist):
        self.__name = name
        self.__yob = yob
        self.__specialist = specialist

    def describe(self):
        """
        Print the details of the doctor.
        """
        print(f"Doctor - Name: {self.__name} - Year: {self.__yob} - Specialist: {self.__specialist}")


class Teacher:
    def __init__(self, name, yob, subject):
        self.__name = name
        self.__yob = yob
        self.__subject = subject

    def describe(self):
        """
        Print the details of the teacher.
        """
        print(f"Teacher - Name: {self.__name} - Year: {self.__yob} - Subject: {self.__subject}")


# Create instances of people
student1 = Student("Vu Nam Anh", 2005, "14")
teacher1 = Teacher("Dam The Phong", 1975, "Math")
doctor1 = Doctor("Vu Hong Tuan", 1945, "Heart")
teacher2 = Teacher("Do Thi Dien", 1972, "Biology")
doctor2 = Doctor("Trinh Hong Son", 1975, "Skeleton")

# Describe individual people
student1.describe()
teacher1.describe()
doctor1.describe()

print()

# Create a ward and add people to it
ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

# Describe the ward
ward1.describe()
