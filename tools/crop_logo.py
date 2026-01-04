from PIL import Image
import os

def crop_logo_text(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    width, height = img.size
    
    # Crop bottom 25% where text usually is
    new_height = int(height * 0.72)
    cropped = img.crop((0, 0, width, new_height))
    
    cropped.save(output_path, "PNG")
    print(f"Cropped logo saved to {output_path} (new size: {cropped.size})")

if __name__ == "__main__":
    logo_path = os.path.join("gui", "assets", "logo.png")
    if os.path.exists(logo_path):
        crop_logo_text(logo_path, logo_path)
    else:
        print("Logo not found.")
