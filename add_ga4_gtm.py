import os
import re

directory = '/Users/sidsmac/Documents/ADMAZIC'

ga4_gtm_head = """
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WGFV5XLJ');</script>
<!-- End Google Tag Manager -->
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-3K4D04T5TE"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-3K4D04T5TE');
</script>"""

gtm_body = """
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WGFV5XLJ"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changed = False
    
    # Check if already installed
    if "GTM-WGFV5XLJ" in content or "G-3K4D04T5TE" in content:
        print(f"Skipping {filepath} (GA4/GTM already exists)")
        return
        
    # Insert in <head>
    # Find <head> tag, which might have attributes like <head lang="en">, though typically just <head>
    # Using regex to replace the first <head> occurrence
    head_pattern = re.compile(r'(<head[^>]*>)', re.IGNORECASE)
    if head_pattern.search(content):
        content = head_pattern.sub(r'\1' + ga4_gtm_head, content, count=1)
        changed = True
    else:
        print(f"Could not find <head> in {filepath}")
        
    # Insert in <body>
    # Find <body> tag, which might have attributes like <body class="premium-funnel">
    body_pattern = re.compile(r'(<body[^>]*>)', re.IGNORECASE)
    if body_pattern.search(content):
        content = body_pattern.sub(r'\1' + gtm_body, content, count=1)
        changed = True
    else:
        print(f"Could not find <body> in {filepath}")
        
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added GA4 and GTM to {filepath}")

for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

