import os
import glob

pixel_code = """
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '2241092950059385');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=2241092950059385&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
</head>"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "2241092950059385" in content:
        print(f"Skipping {filepath} (Pixel already exists)")
        return
        
    if "</head>" in content:
        content = content.replace("</head>", pixel_code)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added pixel to {filepath}")
    else:
        print(f"Could not find </head> in {filepath}")

for root, _, files in os.walk('/Users/sidsmac/Documents/ADMAZIC'):
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))

