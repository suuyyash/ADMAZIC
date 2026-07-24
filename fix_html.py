import re
import os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace image extensions with .webp
html = re.sub(r'src="([^"]+)\.(png|jpg|jpeg)"', r'src="\1.webp"', html, flags=re.IGNORECASE)

# 2. Add width and height to logo-item imgs
def add_dims(match):
    tag = match.group(0)
    if 'width=' not in tag:
        tag = tag.replace('<img', '<img width="200" height="100"')
    return tag

html = re.sub(r'<img [^>]+alt="[^"]*" loading="lazy" decodings="async">', add_dims, html)
html = re.sub(r'<img [^>]+alt="[^"]* Logo"[^>]*>', add_dims, html)

# 3. Add <main> landmark
# We find the end of <header> and the start of <footer>
if '<main id="main-content">' not in html:
    header_end = html.find('</header>') + len('</header>')
    footer_start = html.find('<footer')
    
    if header_end != -1 and footer_start != -1:
        new_html = html[:header_end] + '\n<main id="main-content">\n' + html[header_end:footer_start] + '\n</main>\n' + html[footer_start:]
        html = new_html

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML fixed.")
