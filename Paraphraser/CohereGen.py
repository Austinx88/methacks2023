import cohere
co = cohere.Client('ihkXSqNDJRtrS3iR9HxDrWGREDDM4XR3YpbfO2gE')

#Feed Pickup Line Dataset

#Test A Prompt From User, Text File
 
file = open("chat.txt", "r")


response = co.generate(
    model = "xlarge",
    prompt = file.readline() + "--",
    max_tokens= 20,
    temperature=0.6,
    k=0,
    p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop_sequences=["--"],
)

print (response)