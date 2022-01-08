from pathlib import Path

content = Path("names.txt").read_text().replace('\n', ' ')
print(content)