# Create and store python data strcutures with user interface
# Includes commands for item retrieval, addition, deletion, and list retrieval, addition, or delection
# retrieve both item value by index and vice versa

# optional renaming command

# list of storage lists
containers = {"list":[1,2,3]}

option = ''

print("\nSimple Python Storage App\n")

while(1):
    print("\nCurrent Containers:")
    for name in containers:
        print(name)

    print("\nOptions:")
    print("\tCreate Storage Container - c")
    print("\tDelete Storage Container - D")
    print("\tRetrieve a value from a Container - r")
    print("\tRetrieve an index from a Container - i")
    print("\tAdd a value to a Container - a")
    print("\tDelete a value to a Container - d")
    print("\tQuit Program - q")

    option = input("\nEnter: ")
    print("\n")

    if(option == 'q'):
        break

    if(option == 'c'):
        print("Container Options: List, Stack, Queue, Tuple, Set, Dictionary")

        container_type = input("Enter container type: ")
        name = input("Name of container: ")

        # TODO: check for name duplicates

        if(container_type == "List"):
            print("Creating List")
            containers[name] = []
        elif(container_type == "Stack"):
            print("Creating Stack")
            containers[name] = []
        elif(container_type == "Queue"):
            print("Creating Queue")
            containers[name] = []
        elif(container_type == "Tuple"):
            print("Creating Tuple")
            tuple_values_array = [] # Tuple values need to be inputed when created
            print("Enter tuple values: ")
            user_input_value = input()
            while(user_input_value != ''):
                tuple_values_array.append(user_input_value)
                user_input_value = input()
            containers[name] = tuple(tuple_values_array)
        elif(container_type == "Set"):
            print("Creating Set")
            containers[name] = set((1,2))
        elif(container_type == "Dictionary"):
            print("Creating Dictionary")
            containers[name] = {}
        else:
            print("Invalid Response, try again")

    # check if called to manipulate values but no containers exist
    elif(len(containers) == 0):
        if(option != 'c'):
            print("No containers created, please create a container")
            continue
    
    elif(option == 'D'):
        container_name = input("Enter name of container to be removed: ")
        try:
            containers[container_name]
            confirm = input("Are you sure you want to delete this container? (y/n) ")
            if(confirm == 'y'):
                del containers[container_name]
                print(container_name + f' has been removed from containers')
            elif(confirm == 'n'):
                print("Delete request cancelled")
            else:
                print("Invalid response, cancelling delete request")
        except:
            print(container_name + f' not found, try again')

    elif(option == 'r'):
        container_name = input("Select a container: ")

        if(type(containers[container_name]) == type(set()) or type(containers[container_name]) == type(tuple())):
            print("Values: " + str(containers[container_name]))
        else:
            try:
                container = containers[container_name]
                index = int(input("Enter desired value index: "))
                value = container[index]
                print("Value: " + str(value))
            except IndexError:
                print("Out of bounds error, try again")
            except KeyError:
                print(container_name + f' not found, try again')
            except ValueError:
                print("Non digit response detected, try again")
    
    elif(option == 'i'):
        pass
    
    elif(option == 'a'):
        pass

    elif(option == 'd'):
        pass

    else:
        print("Invalid response, try again")