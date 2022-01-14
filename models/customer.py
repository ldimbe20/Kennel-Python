class Customer():
  
    
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, email, password):
        self.id = id #id is the feild that stors the id
        self.name = name
        self.address = address#name is the field that stores the value name
        self.email = email #address
        self.password = password

