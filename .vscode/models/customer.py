class Customer():
    """[Creating id, name, address, status, location.id fields for Animal class] """
    
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, animal_id, email):
        self.id = id #id is the feild that stors the id
        self.name = name
        self.animal_id = animal_id#name is the field that stores the value name
        self.email = email #address
        
new_animal_one = Customer(1, "Linda", 1, "ldimbe20@gmail.com")

