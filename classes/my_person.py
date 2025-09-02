class Person:
    def __init__(self, first_name:str, last_name:str, age:int, weight:float, city:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.weight = weight
        self.city = city
        self.is_employed = False

    def introduce(self) -> None:
        print(f"Hello, my name is {self.first_name} {self.last_name}. I am {self.age} years old and I live in {self.city}.")

    def relocate(self, new_city: str) -> None:
        self.city = new_city
        print(f"{self.first_name} has relocated to {self.city}.")
    
