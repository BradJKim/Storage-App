# Create and store python data strcutures with user interface
# Includes commands for item retrieval, addition, deletion, and list retrieval, addition, or delection
# retrieve both item value by index and vice versa

# optional renaming command

# list of storage lists
containers = {}

option = ''

print("\nSimple Python Storage App\n")

while(1):
    print("\nCurrent Containers:")
    print(containers)

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

        type = input("Enter container type: ")
        name = input("Name of container: ")

        # TODO: check for name types duplicates

        if(type == "List"):
            print("Creating List")
            containers[name].append([])
        elif(type == "Stack"):
            print("Creating Stack")
            containers[name].append([])
        elif(type == "Queue"):
            print("Creating Queue")
            containers[name].append([])
        elif(type == "Tuple"):
            print("Creating Tuple")
            tuple_values_array = [] # Tuple values need to be inputed when created
            print("Enter tuple values: ")
            user_input_value = input()
            while(user_input_value != ''):
                tuple_values_array.append(user_input_value)
                user_input_value = input()
            containers[name].append(tuple(tuple_values_array))
        elif(type == "Set"):
            print("Creating Set")
            containers[name].append(())
        elif(type == "Dictionary"):
            print("Creating Dictionary")
            containers[name].append({})
        else:
            print("Invalid Response, try again")

    # check if called to manipulate values but no containers exist
    elif(len(containers) == 0):
        if(option != 'c'):
            print("No containers created, please create a container")
            continue
    
    elif():
        pass
    
    elif():
        pass
    
    elif():
        pass
    
    else:
        print("Invalid response, try again")
        continue