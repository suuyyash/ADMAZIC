import os
try:
    from PIL import Image
    logo_path = '/Users/sidsmac/Documents/ADMAZIC/assets/images/logo_cropped.png'
    out_path = '/Users/sidsmac/Documents/ADMAZIC/assets/images/favicon.png'
    
    with Image.open(logo_path) as img:
        # Create a square version for favicon
        size = min(img.size)
        
        # We can just resize it if we want, or crop the center
        # Since it's a text logo mostly, let's just make it a square with transparency
        # Actually, let's just resize it directly or crop the first letter
        
        # Let's crop the left-most square (which usually contains the icon mark if any, or the first letter)
        width, height = img.size
        # Crop a square from the left
        if width > height:
            img = img.crop((0, 0, height, height))
        
        img = img.resize((32, 32), Image.LANCZOS)
        img.save(out_path, format="PNG")
        print("Created favicon.png successfully.")
except Exception as e:
    print("Error:", e)
