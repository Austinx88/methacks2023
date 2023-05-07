import cohere
co = cohere.Client('ihkXSqNDJRtrS3iR9HxDrWGREDDM4XR3YpbfO2gE') # This is your trial API key

# generate a response from drake himself, based on words/phrases given
def drake_generate(prompt, slangstr):
    response = co.generate(
    model='2d60718a-6428-4d76-bdfa-e7ab09df9ae6-ft',
    prompt="respond to this as the popular toronto rapper, drake, would. DO NOT JUST FINISH THE GIVEN SENTANCE, instead reply to it. use toronto slang such as these (seperated by |); "+ slangstr +" . this is the question:" + prompt,
    max_tokens=300,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    output = response.generations[0].text.replace('\n', "") if len(response.generations[0].text) != 0 else "drake is thinking right now, try again later"
    if output == "drake is thinking right now, try again later":
        print("API KEY RATE LIMITED!!!")
    return output

# gets replies from file, stores in str
def get_slangstr():
    slangstr = ""
    with open('assets\slangset.txt', 'r') as f:
        for line in f.readlines():
            slangstr += line.replace("\n", " | ")
    return slangstr

# writes slang = plain text from both toronto set and plain set, into slangset.txt
def __write_slangset():
    slangset = []
    with open('assets\\torontoset.txt', 'r') as f1:
        with open('assets\\plainset.txt', 'r') as f2:
            for i in range(0, 118):
                slangset.append(f1.readline().replace('\n', "") + "=" + f2.readline().replace('\n', "")) 
            
    with open('assets\\slangset.txt', 'a') as f:
        for item in slangset:
            f.write("%s\n" % item)
    