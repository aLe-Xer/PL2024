import re

def md2hmtl(text):
    
    text = re.sub(r'(\n|^)(#+) (.*)', lambda match: f"<h{len(match.group(2))}>{match.group(3)}</h{len(match.group(2))}>", text,flags=re.MULTILINE)

    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)

    text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)

    text = re.sub(r"^[0-9]+\.(.+)$", r"\t<li>\1</li>", text, flags = re.MULTILINE)
    text = re.sub(r"((\t<li>.+</li>\n)+)", r"<ol>\n\1</ol>\n", text, flags = re.MULTILINE)

    text = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', text)

    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

    return text



with open('input.md', 'r') as input_file:
    input_text = input_file.read()
    output_text = md2hmtl(input_text)

with open('output.html', 'w') as output_file:
    output_file.write(output_text)
    