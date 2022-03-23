from wild_cat_zoo.employee import Employee
from wild_cat_zoo.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
    