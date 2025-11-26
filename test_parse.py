from extract_text import extract_text
from parser import parse_resume

with open("priyansheeresume.pdf", "rb") as f:
    text = extract_text(f)

parsed = parse_resume(text)
print(parsed)
