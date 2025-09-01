favorite_cars = [
    {
        "make": "Tesla",
        "model": "Model S",
        "year": 2022,
        "price": 79999.99,
        "features": ["Autopilot", "Electric", "All-Wheel Drive"],
        "is_electric": True,
        "owner": None
    },
    {
        "make": "Porsche",
        "model": "911 Carrera",
        "year": 2023,
        "price": 106500.00,
        "features": ["Sport Mode", "Rear-Wheel Drive", "Turbocharged"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Ford",
        "model": "Mustang",
        "year": 2022,
        "price": 27995.00,
        "features": ["Rear-Wheel Drive", "V8 Engine", "Fastback"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Chevrolet",
        "model": "Corvette",
        "year": 2023,
        "price": 62995.00,
        "features": ["Supercharged", "V8 Engine", "Fastback"],
        "is_electric": False,
        "owner": None
    },
    {
        "make": "Audi",
        "model": "R8",
        "year": 2023,
        "price": 144195.00,
        "features": ["All-Wheel Drive", "V10 Engine", "Convertible"],
        "is_electric": False,
        "owner": None
    }
]

count_over_100k = 0
cars_over_100k = []

# this will loop over each car in the list, find which cars are over 100,000 in price, and print out to the terminal which cars are over that price
for car in favorite_cars:
    if car["price"] > 100000.00:
        print(f"The {car['make']} {car['model']} is over $100,000!")
        count_over_100k += 1
        cars_over_100k.append(car)   # could also append just car['make']

print(f"\nTotal cars over $100k: {count_over_100k}")
print("List of cars over $100k:")
for car in cars_over_100k:
    print(f"- {car['make']} {car['model']}")