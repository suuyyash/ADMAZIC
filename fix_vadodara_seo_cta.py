import os

def fix_vadodara_seo_cta():
    f = "seo-in-vadodara.html"
    if not os.path.exists(f): return
    with open(f, "r", encoding="utf-8") as file:
        html = file.read()
        
    html = html.replace(
        '<a href="contact" class="btn btn-secondary" style="padding: 18px 40px; font-size: 1.1rem; display: inline-block;">Speak With Our SEO Experts</a>',
        '<a href="contact" class="btn" style="padding: 18px 40px; font-size: 1.1rem; border: 1px solid rgba(255,255,255,0.3); color: #fff; border-radius: 8px; transition: all 0.3s ease; text-decoration: none; display: inline-flex; align-items: center; justify-content: center;" onmouseover="this.style.background=\'rgba(255,255,255,0.1)\'; this.style.borderColor=\'#fff\';" onmouseout="this.style.background=\'transparent\'; this.style.borderColor=\'rgba(255,255,255,0.3)\';">Speak With Our Experts</a>'
    )
    
    with open(f, "w", encoding="utf-8") as file:
        file.write(html)
    print(f"Fixed SEO CTA in {f}")

if __name__ == "__main__":
    fix_vadodara_seo_cta()
