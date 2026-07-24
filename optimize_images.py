import os
from PIL import Image

def optimize_dir(directory, max_width=None, is_logo=False):
    if not os.path.exists(directory): return
    for f in os.listdir(directory):
        if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg'):
            path = os.path.join(directory, f)
            try:
                img = Image.open(path)
                
                # Resize if needed
                if max_width and img.width > max_width:
                    ratio = max_width / img.width
                    new_h = int(img.height * ratio)
                    img = img.resize((max_width, new_h), Image.Resampling.LANCZOS)
                
                # Save as WebP
                webp_path = os.path.splitext(path)[0] + '.webp'
                img.save(webp_path, 'WEBP', quality=85)
                
                print(f"Optimized {f} -> {os.path.basename(webp_path)}")
            except Exception as e:
                print(f"Failed to optimize {f}: {e}")

# Logos are small
optimize_dir('Logos', max_width=400, is_logo=True)
optimize_dir('assets/Logos', max_width=400, is_logo=True)
# Main images
optimize_dir('assets/images', max_width=1600)

