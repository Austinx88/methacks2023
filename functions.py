import cohere
co = cohere.Client('ihkXSqNDJRtrS3iR9HxDrWGREDDM4XR3YpbfO2gE') # This is your trial API key

def drake_generate(prompt):
    response = co.generate(
    model='2d60718a-6428-4d76-bdfa-e7ab09df9ae6-ft',
    prompt="respond to this as the popular toronto rapper, drake, would. use toronto slang such as these; wagwan=whats up, fam=family/friend, yo, yute=youth, 6ix=toronto. this is the prompt:" + prompt,
    max_tokens=300,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    return response.generations[0].text
    
