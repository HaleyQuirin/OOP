import random

wings = 2
legs = 4


class Insect:
    def __int__(self):
        self.amount = "fly"

    def number(self):
        if random.randint(0, 10):
            self.amount = "fly"

    def get_amount(self):
        return self.amount
