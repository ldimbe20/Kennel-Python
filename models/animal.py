class Animal():
    """[Creating id, name, breed, status, location.id, and customer.id fields for Animal class] """
    
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, breed, status, customer_id, location_id):
        self.id = id #id is the feild that stors the id
        self.name = name #name is the field that stores the value name
        self.breed = breed #breed is the field that stores the value breed
        self.status = status #status is the field that stores field
        self.customer_id = customer_id
        self.location_id = location_id #location is the field that stores value of location
         #customer is the field that stores the value customer
        
new_animal_one = Animal(1, "Snickers", "Dog", "Recreation", 1, 1)
new_animal_two = Animal(2, "Margo", "Dog", "Recreation", 1, 2)
new_animal_three = Animal(3, "Wiley", "Dog", "Recreation", 2, 3)
new_animal_four = Animal(4, "Mark", "Dog", "Recreation", 2, 4)

