# Create and store python data strcutures with user interface
# Includes functions for item retrieval, addition, deletion, and list retrieval, addition, or delection

# Does not implement Tuples, creating tuples requires values to be inputed

from exceptions import DuplicateNameError, ContainerNotFoundError, ContainerTypeError, IncompatibleContainerType

class Container:

    # class init:
    def __init__(self) -> None:
        self.containers = {}

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

    def delete_container(self, container_name): # does nothing if no containers are made
        try:
            if(len(self.containers) != 0): del self.containers[container_name]
        except:
            raise ContainerNotFoundError

    def get_value(self, container_name, index):
        # Prints all values for set and tuples, key value for dict, and index values for others 
        try:
            container = self.containers[container_name]

            if(container[0] == "Set" or container[0] == "Tuple"):
                return container
            else:
                return container[1][index]
        except:
            raise ContainerNotFoundError

    def get_index(self, container_name, value):
        # Prints value key for dict, and value indices for others 
        try:
            container = self.containers[container_name]

            if(container[0] == "Set"):
                raise IncompatibleContainerType
            elif(container[0] == "Dictionary"): 
                for key in container[1]:
                    if(container[1][key] == value):
                        return key
                return None
            else:
                    return container[1].index(value)
        except:
            raise ContainerNotFoundError
        
    def add_value(self, container_name, value, index = None): # index used as key for dictionaries, else used for lists
        try:
            container = self.containers[container_name]
            
            if(container[0] == "Tuple"):
                raise IncompatibleContainerType
                        
            elif(container[0] == "Dictionary"):
                key_name = index
                key_value = value
                container[1][key_name] = key_value
            
            elif(container[0] == "Queue"):
                container[1].put(value)
            
            elif(container[0] == "Stack"):
                container[1].append(value)
            
            elif(container[0] == "List"):
                if(index != None):
                    container[1].insert(index, value)
                else:
                    container[1].append(value)
            
            elif(container[0] == "Set"):
                container[1].add(value)

        except:
            raise ContainerNotFoundError

    # returns deleted value
    def delete_value(self, container_name, value = None, index = None): # prioritizes index for dictionaries, value for list types
        try:
            container = self.containers[container_name]
            
            if(container[0] == "Tuple"):
                raise IncompatibleContainerType
            
            elif(container[0] == "Dictionary"):
                if(index != None):
                    key_name = index
                    deleted_value = container[1][key_name]
                    del container[1][key_name]
                    return deleted_value
                else:
                    for key_value in container[1]:
                        if(container[1][key_value] == value):
                            deleted_value = container[1][key_name]
                            del container[1][key_name]
                            return deleted_value
                            break
            
            elif(container[0] == "Queue"):
                if(value != None):
                    return container[1].remove(value)
                elif(index != None):
                    deleted_value = container[1][index]
                    del container[1][index]
                    return deleted_value
                else:
                    return container[1][index].pop()
            
            elif(container[0] == "Stack"):
                container[1].remove(value)
            
            elif(container[0] == "List"):
                value = input("Enter value: ")
                container[1].remove(value)
                print("Value removed from List")
            
            elif(container[0] == "Set"):
                value = input("Enter value: ")
                container[1].remove(value)
                print("Value removed from Set")
                
        except:
            raise ContainerNotFoundError


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