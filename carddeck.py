import json
import random
import textwrap

def get_random_value_from_json(json_file_path):

    with open(json_file_path) as file:
        data = json.load(file)
        
    random_deck = random.choice(data['decks'])
    
    random_value = random.choice(random_deck['cards'])
    
    return random_deck['title'], random_deck['instructions'], random_value['content']
    
def indent(text, amount, ch=' '):
    return textwrap.indent(text, amount * ch)
    
json_file_path = 'carddeck.json'
title, instructions, content = get_random_value_from_json(json_file_path)

print(title)

text = textwrap.fill(instructions, initial_indent="    ", subsequent_indent="    ")

print(text)
print(content)
