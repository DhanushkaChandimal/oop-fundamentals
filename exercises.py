# oop principles
class FitnessTracker:
    def __init__(self, user_name):
        self.user_name = user_name
        self.__steps = 0
        self.__calories_burned = 0.0

    def add_steps(self, steps):
        self.__steps += steps

    def get_steps(self):
        return self.__steps

    def add_calories(self, calories):
        self.__calories_burned += calories

    def get_calories_burned(self):
        return self.__calories_burned

    def reset_tracker(self):
        self.__steps = 0
        self.__calories_burned = 0.0

person1_fitness = FitnessTracker("Dhanushka")
print(person1_fitness.get_steps())
print(person1_fitness.get_calories_burned())

person1_fitness.add_steps(2000)
print(person1_fitness.get_steps())

person1_fitness.add_calories(110)
print(person1_fitness.get_calories_burned())

print(person1_fitness.get_steps())
print(person1_fitness.get_calories_burned())

person1_fitness.reset_tracker()

print(person1_fitness.get_steps())
print(person1_fitness.get_calories_burned())
