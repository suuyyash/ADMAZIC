import re

with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Darken --text-muted for contrast
css = css.replace('--text-muted: #64748B;', '--text-muted: #475569;')

# Minify CSS
# Remove comments
css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
# Remove extra whitespace
css = re.sub(r'\s+', ' ', css)
# Remove spaces around brackets and colons
css = re.sub(r'\s*([\{\}:;,])\s*', r'\1', css)

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css.strip())

print("CSS Minified.")
