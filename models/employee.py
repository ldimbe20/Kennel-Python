class Employee():
    """[Creating id, name, address, status, location.id fields for Animal class] """
    
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, address, location_id):
        self.id = id #id is the feild that stors the id
        self.name = name #name is the field that stores the value name
        self.address = address #address
        self.location_id = location_id #location is the field that stores value of location
      

