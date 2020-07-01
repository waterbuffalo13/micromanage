

class Task:
    """A sample Employee class"""

    def __init__(self, created, content):
        self.created = created
        self.content = content

    # @property
    # def email(self):
    #     return '{}.{}@email.com'.format(self.first, self.last)
    #
    # @property
    # def fullname(self):
    #     return '{} {}'.format(self.first, self.last)

    def __repr__(self):
        return "Task('{}', '{}', {})".format(self.first, self.last, self.pay)