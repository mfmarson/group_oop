class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def vroom(self):
        return f'{self.model} goes vroom'
    
    def __str__(self):
        return f'The make is {self.make}, the model is {self.model}, and the year is {self.year}.'
    

mickey = Car("Volkswagen", "Golf", "2018")

print(mickey)

print(mickey.vroom())
