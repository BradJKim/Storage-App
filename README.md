# Storage-App

Python storage app that is able to store multiple python data structures into one application / class.
Stores data structures in "containers" which is stored in 'containers' variable.
Access functions to create and delete containers, get, add, and delete values in one function that encompasses multiple data structures.
Overall goal of project was to be familiarized with python data structures and python class declaration.

Post-Thoughts:

Hypothetical idea that I wanted to try where you could have one object/instance containing all of your data structure values and make using data structures even easier.
I thought that it would be a good way for learn how to use python data structures while also applying an idea I had for a long time.
After finishing the main features, I realized that this was mostly pointless in real world applications and only complicates matters,
rather than providing a simpler feature for handling multiple data structures. 
That said, it was interesting to be able to manipulate data structures as needed with the command line and have values be added and deleted automatically, based on the type of data structure.

There are many issues when using the containers, such as needing to specify the type of data structures and having to error check based on the type as well. 
The containers are stored using a key value dictionary that holds the name for the key and an array which itself stores the data structure type as a string, and the actual data structure.
Accessing the stored values is not pretty as it uses the index 0 for the data structure type and index 1 for the data, within the array. 
While programming, I realized that I was calling the same functions used by data structures based on the type of container or data structure,
and that I was creating code that didn't inherently create any new features or functionalities, other than storing and accessing data from a single dictionary variable,
which itself turned out not super unique or very useful. 

In the end, although it was a great opportunity for practicing python data structures, 
all these features can be directly implemented with the data structure and there is no necessary need to further simply pre-existing data structures with easier functionalities.
