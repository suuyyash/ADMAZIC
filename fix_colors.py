with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace light grey text with darker grey for contrast
html = html.replace('#64748B', '#475569')
html = html.replace('#DC2626', '#B91C1C') # Darken red slightly
html = html.replace('rgba(255,255,255,0.7)', 'rgba(255,255,255,0.9)') # Darken footer text on dark bg

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Colors fixed.")
