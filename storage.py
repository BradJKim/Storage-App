# Create and store python data strcutures with user interface
# Includes commands for item retrieval, addition, deletion, and list retrieval, addition, or delection, and
# retrieve both item value by index and vice versa.

# NOTE: All values are stored as strings in order for index function to work properly. 
#       If non strings are somehow stored, the method will only look for strings and won't detect numbers.
#       User would have to specific whether they are looking for a string or int in order to be specify.
#       This will most likely not be an issue for the container class as type can be more easily specified.

# TODO: Convert options into functions that we can call, seperate function logic from application logic

# list of storage lists
containers = {"list":["List", ["1","2","3"]], "dict":["Dictionary", {"apple":"orange", "banana":"peach"}]}

option = ''

print("\nSimple Python Storage App\n")

while(1):
    print("\nCurrent Containers:")
    for name in containers:
        print(name)

    print("\nOptions:")
    print("\tCreate Storage Container - c")
    print("\tDelete Storage Container - D")
    print("\tRename Storage Container - t")
    print()
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

        # checks for name duplicates
        duplicate = False
        for container_name in containers:
            if(container_name == name):
                duplicate = True 
                break;

        if(duplicate):
            print("Duplicate name found, use a different name for container")
        elif(container_type == "List"):
            print("Creating List")
            containers[name] = ["List", []]
        elif(container_type == "Stack"):
            print("Creating Stack")
            containers[name] = ["Stack", []]
        elif(container_type == "Queue"):
            print("Creating Queue")
            containers[name] = ["Queue", []]
        elif(container_type == "Tuple"):
            print("Creating Tuple")
            tuple_values_array = [] # Tuple values need to be inputed when created
            print("Enter tuple values: ")
            user_input_value = input()
            while(user_input_value != ''):
                tuple_values_array.append(user_input_value)
                user_input_value = input()
            containers[name] = ["Tuple", tuple(tuple_values_array)]
        elif(container_type == "Set"):
            print("Creating Set")
            containers[name] = ["Set", set(())]
        elif(container_type == "Dictionary"):
            print("Creating Dictionary")
            containers[name] = ["Dictionary", {}]
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

    # TODO: add condition for no values added yet 

    elif(option == 'r'):
        container_name = input("Select a container: ")

        # Prints all values for set and tuples, key value for dict, and index values for others 
        try:
            container = containers[container_name]

            if(len(container[1]) == 0):
                print("Container is empty")
            else:
                if(container[0] == "Set" or container[0] == "Tuple"):
                    print("Values: " + str(container))
                elif(container[0] == "Dictionary"): 
                    try:
                        key = input("Enter key: ")
                        print("Value: " + str(container[1][key]))
                    except KeyError:
                        print("Key not found, try again")
                else:
                    try:
                        index = int(input("Enter desired value index: "))
                        value = container[1][index]
                        print("Value: " + str(value))
                    except IndexError:
                        print("Out of bounds error, try again")
                    except KeyError:
                        print(container_name + f' not found, try again')
        except KeyError:
            print("Container not found, try again")

    elif(option == 'i'):
        container_name = input("Select a container: ")

        # Prints value key for dict, and value indices for others 
        try:
            container = containers[container_name]

            if(len(container[1]) == 0):
                print("Container is empty")
            else:
                if(container[0] == "Set"):
                    print("Index cannot be given")
                elif(container[0] == "Dictionary"): 
                    value_input = input("Enter value: ")

                    found = False
                    for key in container[1]:
                        if(container[1][key] == value_input):
                            print("Key: " + str(key))
                            found = True
                            break
                    if(not found):
                        print("No key found, value does not exist in container")
                else:
                    try:
                        value_input = input("Enter value: ")  
                        print("Index: " + str(container[1].index(value_input)))
                    except ValueError:
                        print("Index not found, value does not exist in container")
        except KeyError:
            print("Container not found, try again")
    
    elif(option == 'a'): # all ints and numbers must be stored as a string for index to be found, ex: 1 vs "1", 
        container_name = input("Select a container: ")

        try:
            container = containers[container_name]
            
            if(container[0] == "Tuple"):
                print("Cannot add more values to Tuple, try a different container")
            
            elif(container[0] == "Dictionary"):
                key_name = input("Enter key: ")
                key_value = input("Enter value: ")
                container[1][key_name] = key_value
                print("Key-value pair added to Dictionary")
            
            elif(container[0] == "Queue"):
                value = input("Enter value: ")
                container[1].put(value)
                print("Value added to Queue")
            
            elif(container[0] == "Stack"):
                value = input("Enter value: ")
                container[1].append(value)
                print("Value added to Stack")
            
            elif(container[0] == "List"):
                value = input("Enter value: ")
                container[1].append(value)
                print("Value added to List")
            
            elif(container[0] == "Set"):
                value = input("Enter value: ")
                container[1].add(value)
                print("Value added to Set")
        except KeyError:
            print("Container not found, try again") 

    elif(option == 'd'):
        container_name = input("Select a container: ")

        try:
            container = containers[container_name]
            
            if(container[0] == "Tuple"):
                print("Cannot delete values from Tuple, try a different container")
            
            elif(container[0] == "Dictionary"):
                key_name = input("Enter key: ")
                container[1].pop(key_name)
                print("Key-value pair removed from Dictionary")
            
            elif(container[0] == "Queue"):
                value = input("Enter value: ")
                container[1].remove(value)
                print("Value removed from Queue")
            
            elif(container[0] == "Stack"):
                value = input("Enter value: ")
                container[1].remove(value)
                print("Value removed from Stack")
            
            elif(container[0] == "List"):
                value = input("Enter value: ")
                container[1].remove(value)
                print("Value removed from List")
            
            elif(container[0] == "Set"):
                value = input("Enter value: ")
                container[1].remove(value)
                print("Value removed from Set")
        except KeyError:
            print("Container not found, try again") 

    else:
        print("Invalid response, try again")
    
    # TODO: Add options for pop / push for queue and stack
        