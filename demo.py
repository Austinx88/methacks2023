import cohere
co = cohere.Client('ihkXSqNDJRtrS3iR9HxDrWGREDDM4XR3YpbfO2gE') # This is your trial API key
while True:
    prompt = input('Enter a prompt: ')
    response = co.generate(
    model='2d60718a-6428-4d76-bdfa-e7ab09df9ae6-ft',
    prompt=prompt,
    max_tokens=300,
    temperature=0.9,
    k=0,
    stop_sequences=[],
    return_likelihoods='NONE')
    print('Prediction: {}'.format(response.generations[0].text))