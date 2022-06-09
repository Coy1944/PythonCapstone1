class Courses:

    def __init__(self, name, location, cost):
        self.name = name
        self.location = location
        self.cost = cost

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.name, self.location)

    def __repr__(self):
        return "Courses('{}', '{}', '{}')".format(self.name, self.location, self.cost)