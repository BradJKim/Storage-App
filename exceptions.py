class DuplicateNameError(Exception):
    "Exception raised for duplicate container name"
    pass

class ContainerTypeError(Exception):
    "Exception raised for unknown container type"
    pass

class ContainerNotFoundError(Exception):
    "Exception raised when specified container does not exist"
    pass

class IncompatibleContainerType(Exception):
    "Exception raised when container type does not allow certain functions"
    pass