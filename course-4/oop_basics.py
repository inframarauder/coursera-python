class Student:
    name = ''
    roll = ''

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show_details(self):
        print('Name', self.name)
        print('Roll Number', self.roll)


def main():
    student = Student('Subhasis', '1751034')
    student.show_details()


main()
