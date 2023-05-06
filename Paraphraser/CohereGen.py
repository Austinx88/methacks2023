import cohere
co = cohere.Client('CwM1JuOz8DleP9dVvjpcwwM6WnkD4uzaZw0QyCOe') # This is your trial API key
file = open("input.txt", "r")
prompt1 = file.readline()
file.close()
response = co.generate(
  model='d04fb84e-1b92-4f0b-934c-eae87f903142-ft',
  prompt="rephrase the given prompt using toronto slang:\nHere are some constraints:\n1. respond with a one line rephrasement, do not use explicit language \n2. use atleast 2 words of toronto slang\n3. you are not responding to the given prompt\n4. make sure your response is something a torontonian would say\nhere is the given prompt: " + prompt1,
  max_tokens=300,
  temperature=1,
  k=126,
  stop_sequences=[],
  return_likelihoods='GENERATION')
print('Prediction: {}'.format(response.generations[0].text))