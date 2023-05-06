import cohere
co = cohere.Client('CwM1JuOz8DleP9dVvjpcwwM6WnkD4uzaZw0QyCOe') # This is your trial API key
prompt1 = input()
toronto = """ create a toronto slang pickup line using the given prompt:
  \nhere are some contraints:
  \n1. respond with one line
  \n2. use atleast 2 toronto slang words
  \n3. only output the conversion and nothing else.
  \n4. use fam, eh ahlie, nyeah eh, wallahi, and other toronto words to spice up the response\nhere is the given prompt, convert it: """ + prompt1
response = co.generate(
  model='d04fb84e-1b92-4f0b-934c-eae87f903142-ft',
  prompt= toronto,
  max_tokens=42,
  temperature=1,
  k=56,
  stop_sequences=[],
  return_likelihoods='NONE')
print((response.generations[0].text))