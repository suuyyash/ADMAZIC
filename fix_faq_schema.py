import os
import re
import json

def fix_faq_schemas():
    files_to_check = [
        "seo-in-surat.html",
        "seo-in-ahmedabad.html",
        "google-ads-in-surat.html",
        "google-ads-in-ahmedabad.html",
        "meta-ads-in-surat.html",
        "meta-ads-in-ahmedabad.html"
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
            # Clean up the question text (remove numbering if present, e.g., "1. ")
            # Wait, the numbering is in the text, let's keep it as is, or strip it?
            # Usually schema is better without numbers, let's strip leading numbers and dots.
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

        new_schema_script = '<script type="application/ld+json">\n' + json.dumps(schema_dict, indent=2) + '\n</script>'

        # Replace existing schema
        # We need to find the existing <script type="application/ld+json">...</script>
        # Note: There might be multiple ld+json scripts (e.g. for Organization or LocalBusiness).
        # We should only replace the FAQPage one.
        
        # Let's find the FAQ schema specifically
        pattern = re.compile(r'<script type="application/ld\+json">.*?FAQPage.*?</script>', re.DOTALL)
        
        if pattern.search(html):
            new_html = pattern.sub(new_schema_script, html)
            with open(filepath, "w", encoding="utf-8") as fw:
                fw.write(new_html)
            print(f"Updated FAQ schema in {file_name}")
        else:
            print(f"Could not find existing FAQ schema block in {file_name}. Looking for generic ld+json block...")
            # If no FAQPage is found, maybe it's just a script tag with ld+json
            pattern_generic = re.compile(r'<script type="application/ld\+json">.*?</script>', re.DOTALL)
            if pattern_generic.search(html):
                new_html = pattern_generic.sub(new_schema_script, html)
                with open(filepath, "w", encoding="utf-8") as fw:
                    fw.write(new_html)
                print(f"Replaced generic ld+json with FAQ schema in {file_name}")
            else:
                print(f"No ld+json script found in {file_name}. Inserting in <head>...")
                # Insert right before </head>
                new_html = html.replace('</head>', new_schema_script + '\n</head>')
                with open(filepath, "w", encoding="utf-8") as fw:
                    fw.write(new_html)
                print(f"Inserted FAQ schema in {file_name}")

if __name__ == "__main__":
    fix_faq_schemas()
