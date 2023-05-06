import cohere
co = cohere.Client('yourkeyhere')


#Test A Prompt From User, Text File
 
file = open("input.txt", "r")


response = co.generate(
    model = "yourmodelhere",
    prompt = file.readline(),
 
)

print (response)