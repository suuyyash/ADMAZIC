import os
import re

def fix_vadodara_pages():
    files = ["seo-in-vadodara.html", "google-ads-in-vadodara.html", "meta-ads-in-vadodara.html"]
    
    cta_1 = """      <div class="reveal" style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%;">
        <a href="free-audit" class="btn btn-secondary" style="padding: 15px 35px; display: inline-block;"><i class="fas fa-rocket"></i> Scale Your Vadodara Business Today</a>
      </div>
    </div>
  </section>"""
  
    cta_2 = """      <div class="reveal" style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%;">
        <a href="free-audit" class="btn btn-primary" style="padding: 15px 35px; background: var(--accent-blue); display: inline-block;">Target Your Exact Audience <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>"""
  
    cta_3 = """      <div class="reveal" style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%;">
        <a href="free-audit" class="btn btn-primary glow-btn" style="padding: 15px 35px; background: #DC2626; display: inline-block;">Discover Your Market Opportunity <i class="fas fa-arrow-right"></i></a>
      </div>
    </div>
  </section>"""
  
    for f in files:
        if not os.path.exists(f): continue
        with open(f, "r", encoding="utf-8") as file:
            html = file.read()
            
        # Insert CTA 1 at end of Section 2
        html = re.sub(r'(\s*</div>\s*</div>\s*</section>\s*<!-- Section 3)', lambda m: cta_1.replace("    </div>\n  </section>", m.group(1)), html)
        
        # Insert CTA 2 at end of Section 4
        html = re.sub(r'(\s*</div>\s*</div>\s*</section>\s*<!-- Section 5)', lambda m: cta_2.replace("    </div>\n  </section>", m.group(1)), html)
        
        # Insert CTA 3 at end of Section 6
        html = re.sub(r'(\s*</div>\s*</div>\s*</section>\s*<!-- Section 7)', lambda m: cta_3.replace("    </div>\n  </section>", m.group(1)), html)
        
        # Fix bottom CTA button
        html = html.replace(
            '<a href="contact" class="btn btn-secondary" style="padding: 18px 40px; font-size: 1.1rem; display: inline-block;">Speak With Our Strategists</a>',
            '<a href="contact" class="btn" style="padding: 18px 40px; font-size: 1.1rem; border: 1px solid rgba(255,255,255,0.3); color: #fff; border-radius: 8px; transition: all 0.3s ease; text-decoration: none; display: inline-flex; align-items: center; justify-content: center;" onmouseover="this.style.background=\'rgba(255,255,255,0.1)\'; this.style.borderColor=\'#fff\';" onmouseout="this.style.background=\'transparent\'; this.style.borderColor=\'rgba(255,255,255,0.3)\';">Speak With Our Experts</a>'
        )
        html = html.replace(
            '<a href="contact" class="btn btn-secondary" style="padding: 18px 40px; font-size: 1.1rem; display: inline-block;">Speak With Our Ads Experts</a>',
            '<a href="contact" class="btn" style="padding: 18px 40px; font-size: 1.1rem; border: 1px solid rgba(255,255,255,0.3); color: #fff; border-radius: 8px; transition: all 0.3s ease; text-decoration: none; display: inline-flex; align-items: center; justify-content: center;" onmouseover="this.style.background=\'rgba(255,255,255,0.1)\'; this.style.borderColor=\'#fff\';" onmouseout="this.style.background=\'transparent\'; this.style.borderColor=\'rgba(255,255,255,0.3)\';">Speak With Our Experts</a>'
        )
        html = html.replace(
            '<a href="contact" class="btn btn-secondary" style="padding: 18px 40px; font-size: 1.1rem;"><i class="fas fa-chart-line"></i> Speak to a Google Ads Expert</a>',
            '<a href="contact" class="btn btn-secondary" style="padding: 18px 40px; font-size: 1.1rem; display: inline-flex; align-items: center; justify-content: center;"><i class="fas fa-chart-line" style="margin-right: 8px;"></i> Speak to a Google Ads Expert</a>'
        )
        
        with open(f, "w", encoding="utf-8") as file:
            file.write(html)
        print(f"Fixed CTAs in {f}")

if __name__ == "__main__":
    fix_vadodara_pages()
