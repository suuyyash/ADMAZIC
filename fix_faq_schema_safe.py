import os
import re
import json

def fix_faq_schemas():
    files_to_check = [
        "seo-in-surat.html",
        "seo-in-ahmedabad.html",
        "seo-in-vadodara.html",
        "google-ads-in-surat.html",
        "google-ads-in-ahmedabad.html",
        "google-ads-in-vadodara.html",
        "meta-ads-in-surat.html",
        "meta-ads-in-ahmedabad.html",
        "meta-ads-in-vadodara.html",
        "seo-in-mumbai.html",
        "google-ads-in-mumbai.html",
        "meta-ads-in-mumbai.html",
        "seo-in-bangalore.html",
        "google-ads-in-bangalore.html",
        "meta-ads-in-bangalore.html",
        "seo-in-delhi.html",
        "google-ads-in-delhi.html",
        "meta-ads-in-delhi.html",
        "seo-in-gurgaon.html",
        "google-ads-in-gurgaon.html",
        "meta-ads-in-gurgaon.html"
    ]

    for file_name in files_to_check:
        filepath = os.path.join(".", file_name)
        if not os.path.exists(filepath):
            print(f"File not found: {file_name}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()

        # Extract FAQs from HTML
        faq_questions = re.findall(r'<button class="faq-question">(.*?)<i class=', html, re.DOTALL)
        faq_answers = re.findall(r'<div class="faq-answer"><p>(.*?)</p></div>', html, re.DOTALL)

        if len(faq_questions) != len(faq_answers):
            print(f"Warning: FAQ question count ({len(faq_questions)}) does not match answer count ({len(faq_answers)}) in {file_name}")
            continue

        if len(faq_questions) == 0:
            print(f"No FAQs found in {file_name}")
            continue

        # Construct new schema
        main_entity = []
        for q, a in zip(faq_questions, faq_answers):
            q_clean = re.sub(r'^\d+\.\s*', '', q.strip())
            a_clean = a.strip()

            main_entity.append({
                "@type": "Question",
                "name": q_clean,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": a_clean
                }
            })

        schema_dict = {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": main_entity
        }

        new_schema_script = '<script type="application/ld+json">\n' + json.dumps(schema_dict, indent=2, ensure_ascii=False) + '\n</script>'

        # Using match objects instead of sub to avoid escape sequence issues
        pattern = re.compile(r'<script type="application/ld\+json">.*?FAQPage.*?</script>', re.DOTALL)
        match = pattern.search(html)
        
        if match:
            new_html = html[:match.start()] + new_schema_script + html[match.end():]
            with open(filepath, "w", encoding="utf-8") as fw:
                fw.write(new_html)
            print(f"Updated FAQ schema in {file_name}")
        else:
            print(f"Could not find existing FAQ schema block in {file_name}. Looking for generic ld+json block...")
            pattern_generic = re.compile(r'<script type="application/ld\+json">.*?</script>', re.DOTALL)
            match_generic = pattern_generic.search(html)
            if match_generic:
                new_html = html[:match_generic.start()] + new_schema_script + html[match_generic.end():]
                with open(filepath, "w", encoding="utf-8") as fw:
                    fw.write(new_html)
                print(f"Replaced generic ld+json with FAQ schema in {file_name}")
            else:
                print(f"No ld+json script found in {file_name}. Inserting in <head>...")
                new_html = html.replace('</head>', new_schema_script + '\n</head>')
                with open(filepath, "w", encoding="utf-8") as fw:
                    fw.write(new_html)
                print(f"Inserted FAQ schema in {file_name}")

if __name__ == "__main__":
    fix_faq_schemas()
