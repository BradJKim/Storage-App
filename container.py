# Create and store python data strcutures with user interface
# Includes functions for item retrieval, addition, deletion, and list retrieval, addition, or delection

# Does not implement Tuples, creating tuples requires values to be inputed

from exceptions import DuplicateNameError
from exceptions import ContainerTypeError

class Container:

    # class init:
    def __init__(self) -> None:
        self.containers = []

    # class methods:
    def create_container(self, container_name, container_type):
        # checks for name duplicates
        duplicate = False
        for container in self.containers:
            if(container == container_name):
                duplicate = True 
                break;
        if(duplicate):
            raise DuplicateNameError
        elif(container_type == "List"):
            self.containers[container_name] = ["List", []]
        elif(container_type == "Stack"):
            self.containers[container_name] = ["Stack", []]
        elif(container_type == "Queue"):
            self.containers[container_name] = ["Queue", []]
        elif(container_type == "Set"):
            self.containers[container_name] = ["Set", set(())]
        elif(container_type == "Dictionary"):
            self.containers[container_name] = ["Dictionary", {}]
        else:
            raise ContainerTypeError

    def delete_container(self, container_name):
        pass

    def get_value(self, container_name, index):
        pass

    def get_index(self, container_name, value):
        pass

    def add_value(self, container_name, value):
        pass

    def add_value(self, container_name, value, index):
        pass

    def delete_value(self, container_name, value):
        pass


    """ 
    Python Class Example

    value = 0
    
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __repr__(self):
        return f'Container({self.name})'

    def get(value):
        return 0
    
    def enter(self):
        return self.name
    
    @classmethod
    def give(cls):
        return cls([1,2,3])
    
    @staticmethod
    def number(value):
        return value + 1 """