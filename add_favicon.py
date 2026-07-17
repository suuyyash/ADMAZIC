import os

directory = '/Users/sidsmac/Documents/ADMAZIC'
favicon_tag = '<link rel="icon" type="image/png" href="assets/images/favicon.png">\n</head>'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "favicon.png" in content or "rel=\"icon\"" in content:
        print(f"Skipping {filepath} (Favicon already exists)")
        return
        
    if "</head>" in content:
        content = content.replace("</head>", favicon_tag)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added favicon to {filepath}")
    else:
        print(f"Could not find </head> in {filepath}")

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

