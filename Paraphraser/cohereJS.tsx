import cohere from 'cohere-ai';
cohere.init('CwM1JuOz8DleP9dVvjpcwwM6WnkD4uzaZw0QyCOe'); // This is your trial API key
(async () => {
  const response = await cohere.generate({
    model: 'd04fb84e-1b92-4f0b-934c-eae87f903142-ft',
    prompt: 'convert the given prompt to toronto slang:\nhere are some contraints:\n1. respond with one line\n2. use atleast 2 toronto slang words\n3. you are not responding to the user, only output the conversion and nothing else.\n4. use fam, eh , and other toronto words to spice up the response\nhere is the given prompt, convert it: you\'re cute we should go out sometime',
    max_tokens: 42,
    temperature: 1,
    k: 58,
    stop_sequences: [],
    return_likelihoods: 'NONE'
  });
  console.log(`Prediction: ${response.body.generations[0].text}`);
})();