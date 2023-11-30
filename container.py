class Container:

    # variables: 

    # class init:
    def __init__(self) -> None:
        self.containers = []
        self.container_names = []

    # class methods:



    """ containers.append({1,7,3,4})
        containers.append([1,2,3,8])
        containers.append((1,4,6,3))
        containers.append({"one":"1","two":"2"})

        print(containers) """
    
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