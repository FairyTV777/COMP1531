import datetime

class Student:
    def __init__(self, firstName, lastName, birth_year):
        self.name = firstName + " " + lastName
        self.birth_year = birth_year

    def get_age(self):
        return datetime.datetime.now().year - self.birth_year

if __name__ == '__main__':
    s = Student("Rob", "Everest", 1961)
    years_old = s.get_age()
    print(f"{s.name} is {years_old} old")
