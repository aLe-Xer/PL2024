import re

def on_off(text):
    active = True
    total = 0

    p =re.compile(r'(?:On|Off|(\+|-)?\d+|=)', re.IGNORECASE) 

    for match in p.finditer(text):
        token = match.group()
        if token.lower() == 'on':
            active = True
        elif token.lower() == 'off':
            active = False
        elif token.isdigit() or (token.startswith('+') and token[1:].isdigit()) or (token.startswith('-') and token[1:].isdigit()):
            if active:
                total += int(token)
        elif token == '=':
            print('Current result = ' + str(total))

    print('Final result = ' + str(total))





with open('input.txt', 'r') as input_file:
    input_text = input_file.read()
    output_text = on_off(input_text)

