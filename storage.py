# Create and store python data strcutures with user interface
# Includes commands for item retrieval, addition, deletion, and list retrieval, addition, or delection
# retrieve both item value by index and vice versa

# optional renaming command

# list of storage lists
# TODO: Change contianer list to custom dictionary that holds python data structures with lists
containers = []
container_names = []

option = ''

print("\nSimple Python Storage App\n")

while(1):
    print("\nCurrent Containers:")
    print(containers)
    print(container_names)

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

        if(type == "List"):
            print("Creating List")
            container_names.append(name)

        elif(type == "Stack"):
            print("Creating Stack")
            container_names.append(name)
        elif(type == "Queue"):
            print("Creating Queue")
            container_names.append(name)
        elif(type == "Tuple"):
            print("Creating Tuple")
            container_names.append(name)
        elif(type == "Set"):
            print("Creating Set")
            container_names.append(name)
        elif(type == "Dictionary"):
            print("Creating Dictionary")
            container_names.append(name)
        else:
            print("Invalid Response, try again")

    # check if called to manipulate values but no containers exist
    elif(len(containers) == 0):
        if(option != 'c'):
            print("No containers created, please create a container")
            continue
    else:
        print("Invalid response, try again")
        continue