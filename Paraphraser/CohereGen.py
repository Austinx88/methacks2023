import cohere
co = cohere.Client('CwM1JuOz8DleP9dVvjpcwwM6WnkD4uzaZw0QyCOe') # This is your trial API key
filei = open("input.txt", "r")
response = co.generate(model='d04fb84e-1b92-4f0b-934c-eae87f903142-ft', prompt=filei.readline())
print('Prediction: {}'.format(response.generations[0].text))
filei.close()