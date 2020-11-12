import datetime

class Student:
    def __init__(self, firstName, lastName, birth_year):
        self.name = firstName + " " + lastName
        self.birth_year = birth_year

    def get_age(self):
        return datetime.datetime.now().year - self.birth_year

    def get_name(self):
        return self.name

if __name__ == '__main__':
    s = Student("Rob", "Everest", 1961)
    years_old = s.get_age()
    name = s.get_name()
    print(f"{name} is {years_old} old")
