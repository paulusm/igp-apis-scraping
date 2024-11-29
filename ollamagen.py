from ollama import generate
import json

def startupGenerator(industryType):
    prompt = f'Generate the name and a very short description of a UK startup in the {industryType} industry. Respond using JSON with the keys: name, description'
    llamagen = generate(model='tinyllama', prompt=prompt, format='json')
    return (json.loads(llamagen.response))

# print(startupGenerator('Healthcare'))