from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageFont

def add_watermark(image, text="Watermark", position=(0, 0), opacity=128):
    # Make the image editable
    watermark = Image.new("RGBA", image.size)
    # Create a drawing context
    drawing = ImageDraw.Draw(watermark)
    
    # Define the font and size
    font = ImageFont.load_default()
    text_width = drawing.textlength(text, font=font)
    text_height = text_width * 2
    
    # Calculate the position: bottom right corner
    x = image.size[0] - text_width - 10  # 10 pixels from the right edge
    y = image.size[1] - text_height - 10  # 10 pixels from the bottom edge
    
    # Add the text to the watermark layer
    drawing.text((x, y), text, fill=(255, 255, 255, opacity), font=font)
    
    # Combine the watermark with the original image
    return Image.alpha_composite(image.convert("RGBA"), watermark)

def upload_picture():
    # Open file dialog and get the picture file path
    file_path = filedialog.askopenfilename()
    if file_path:  # Check if a file was selected
        # Open the image and apply EXIF transpose
        image = ImageOps.exif_transpose(Image.open(file_path))
        # Resize the image for display (keeping it as RGBA for transparency)
        image = image.resize((250, 250)).convert("RGBA")
        
        # Add watermark
        watermarked_image = add_watermark(image, "Sample Watermark")
        
        # Convert back to PhotoImage for Tkinter compatibility
        photo = ImageTk.PhotoImage(image=watermarked_image.convert("RGB"))
        
        # Display the image in the app
        picture_label.config(image=photo)
        picture_label.image = photo  # Keep a reference

window = Tk()
window.title("Image Watermark")
window.config(padx=50, pady=50)
window.geometry("500x500")

# Upload Button
upload_button = Button(window, text="Upload Picture", command=upload_picture)
upload_button.pack(pady=20)

# Create a label to display the picture
picture_label = Label(window)
picture_label.pack()

window.mainloop()






