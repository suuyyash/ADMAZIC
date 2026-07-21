import re

def fix_meta_tags():
    files = {
        "seo-in-ahmedabad.html": {
            "title": "<title>SEO Services in Ahmedabad | Premium SEO Agency | ADMAZIC</title>",
            "desc": "Scale your Ahmedabad business with ADMAZIC's premium local SEO services. We help manufacturing, real estate, and local businesses dominate Google search."
        },
        "google-ads-in-ahmedabad.html": {
            "title": "<title>Google Ads Services in Ahmedabad | PPC & SEM Agency | ADMAZIC</title>",
            "desc": "Dominate search intent in Ahmedabad with ADMAZIC. We engineer highly profitable Google Ads campaigns for Ahmedabad's B2B manufacturers, real estate developers, and local service brands."
        }
    }

    for fname, tags in files.items():
        with open(fname, "r", encoding="utf-8") as f:
            html = f.read()

        html = re.sub(r'<title>.*?</title>', tags["title"], html)
        html = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{tags["desc"]}">', html)
        html = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{tags["title"].replace("<title>", "").replace("</title>", "")}">', html)
        
        url_tag = fname.replace(".html", "")
        html = re.sub(r'<meta property="og:url" content=".*?">', f'<meta property="og:url" content="https://admazic.com/{url_tag}">', html)

        with open(fname, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Fixed tags in {fname}")

if __name__ == "__main__":
    fix_meta_tags()
