from container import Container

myContainers = Container()

myContainers.create_container("apple","List")

print(myContainers.containers)

myContainers.delete_container("apple")

print(myContainers.containers)