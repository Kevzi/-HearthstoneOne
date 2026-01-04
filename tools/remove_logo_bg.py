from PIL import Image, ImageOps
import os

def remove_background(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    datas = img.getdata()

    new_data = []
    for item in datas:
        # If the pixel is very dark (black circuit background), make it transparent
        # We use a threshold to handle slight variations in black
        if item[0] < 40 and item[1] < 40 and item[2] < 40:
            new_data.append((0, 0, 0, 0))
        else:
            new_data.append(item)

    img.putdata(new_data)
    
    # Trim empty space
    bbox = img.getbbox()
    if bbox:
        img = img.crop(bbox)
        
    img.save(output_path, "PNG")
    print(f"Processed logo saved to {output_path}")

if __name__ == "__main__":
    logo_path = os.path.join("gui", "assets", "logo.png")
    if os.path.exists(logo_path):
        remove_background(logo_path, logo_path)
    else:
        print("Logo not found.")
