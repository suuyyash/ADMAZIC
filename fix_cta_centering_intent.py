import os
import re

def process_file(filename, intents):
    if not os.path.exists(filename):
        print(f"{filename} not found.")
        return
        
    with open(filename, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Fix the grid-column issue for centering
    html = html.replace(
        'style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%;"',
        'style="margin-top: 50px; text-align: center; display: flex; justify-content: center; width: 100%; grid-column: 1 / -1;"'
    )
    
    # 2. Fix the CTA text based on intents
    # We know the current text in the 3 sections is:
    # CTA 1: "Scale Your Vadodara Business Today"
    # CTA 2: "Target Your Exact Audience"
    # CTA 3: "Discover Your Market Opportunity"
    
    html = html.replace("Scale Your Vadodara Business Today", intents[0])
    html = html.replace("Target Your Exact Audience", intents[1])
    html = html.replace("Discover Your Market Opportunity", intents[2])
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
        
    print(f"Fixed {filename}")

if __name__ == "__main__":
    seo_intents = [
        "Scale Your Vadodara SEO Today",
        "Dominate Local Search Today",
        "Request Your Free SEO Blueprint"
    ]
    google_intents = [
        "Launch Your Vadodara Ads Campaign",
        "Capture High-Intent Buyers Now",
        "Audit Your Current Ads Campaigns"
    ]
    meta_intents = [
        "Ignite Your Meta Ads ROI",
        "Engage Your Ideal Audience on Social",
        "Get Your Meta Ads Strategy"
    ]
    
    process_file("seo-in-vadodara.html", seo_intents)
    process_file("google-ads-in-vadodara.html", google_intents)
    process_file("meta-ads-in-vadodara.html", meta_intents)
