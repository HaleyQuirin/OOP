import random

wings = 2
legs = 4


class Insect:
    def __int__(self):
        self.amount = "wings"

    def number(self):
        if random.randint(0, 10):
            self.amount = "wings"
        else:
            self.amount = "legs"

    def get_amount(self):
        return self.amount
