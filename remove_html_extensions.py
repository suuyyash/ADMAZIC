import os
import re

directory = '/Users/sidsmac/Documents/ADMAZIC'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Regex to find href="something.html" or href="something.html#hash"
    # We want to ignore external links starting with http:// or https://
    # and we want to ignore things like .html inside JS strings if possible, 
    # but targeting href="..." is safest.
    
    # Matches href=" (not http) (anything) .html (optional #hash) "
    # Regex breakdown:
    # href="            : exact string
    # (?!https?://)     : negative lookahead to prevent matching external URLs
    # ([^"]+?)          : group 1, non-greedy match for the path up to .html
    # \.html            : exact string .html
    # (#[^"]*)?         : group 2, optional hash fragment
    # "                 : exact closing quote
    
    pattern = re.compile(r'href="(?!https?://)([^"]+?)\.html(#[^"]*)?"')
    
    # Replacement function
    def replacer(match):
        path = match.group(1)
        hash_frag = match.group(2) or ''
        
        # If it's index.html, we might want to resolve it to just the directory, 
        # but leaving it as 'index' or '/' depends on depth. 
        # For simplicity and server-agnostic clean URLs, 'about.html' -> 'about'
        # 'index.html' -> '/' is tricky with relative paths like '../../index.html'.
        # Changing '../../index.html' to '../../' is technically most correct.
        
        if path.endswith('/index') or path == 'index':
            if path == 'index':
                new_path = '/'
            else:
                new_path = path[:-5] # remove 'index'
        else:
            new_path = path
            
        return f'href="{new_path}{hash_frag}"'
    
    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated links in {filepath}")

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

