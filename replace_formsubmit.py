import os

directory = '/Users/sidsmac/Documents/ADMAZIC'
target_email = 'nasrinjariwala176@gmail.com'
replacement_hash = '0268ba27ded67a4b85be605b435c44a2'

files_to_check = [
    'contact.html',
    'careers.html',
    'free-audit.html',
    'assets/js/main.js',
    'assets/js/strategy-premium.js'
]

for filename in files_to_check:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target_email in content:
            new_content = content.replace(target_email, replacement_hash)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Replaced in {filename}")
        else:
            print(f"Email not found in {filename}")
    else:
        print(f"File {filename} not found")

