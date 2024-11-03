import sys
import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import logging

# Set up logging for debugging
logging.basicConfig(
    filename="image_resizer_debug.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def upscale_pixel_art(input_image, output_directory, scale_factor):
    try:
        # Calculate new size based on the scale factor
        new_size = (int(input_image.width * scale_factor), int(input_image.height * scale_factor))
        logging.debug(f"Resizing image to new size: {new_size}")

        resized_image = input_image.resize(new_size, Image.NEAREST)  # NEAREST resampling preserves pixelation

        # Save the resized image
        filename = os.path.basename(input_image.filename)
        output_image_path = os.path.join(output_directory, filename)
        resized_image.save(output_image_path)

        logging.info(f"Image saved to {output_image_path}")
        return output_image_path

    except Exception as e:
        logging.error(f"Error during upscaling: {str(e)}")
        raise

def select_input_image():
    try:
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if file_path:
            input_image_path.set(file_path)
            logging.debug(f"Selected input image: {file_path}")
    except Exception as e:
        logging.error(f"Error selecting input image: {str(e)}")
        messagebox.showerror("Error", f"Error selecting input image: {str(e)}")

def select_output_directory():
    try:
        directory = filedialog.askdirectory(title="Select Output Directory")
        if directory:
            output_directory.set(directory)
            logging.debug(f"Selected output directory: {directory}")
    except Exception as e:
        logging.error(f"Error selecting output directory: {str(e)}")
        messagebox.showerror("Error", f"Error selecting output directory: {str(e)}")

def start_upscaling():
    try:
        input_path = input_image_path.get()
        output_dir = output_directory.get()
        scale_factor = float(scale_factor_entry.get())

        logging.debug(f"Starting upscaling with input image: {input_path}, output directory: {output_dir}, scale factor: {scale_factor}")

        if not input_path or not os.path.exists(input_path):
            logging.warning(f"Invalid input image path: {input_path}")
            messagebox.showerror("Input Error", "Please select a valid input image.")
            return
        if not output_dir or not os.path.exists(output_dir):
            logging.warning(f"Invalid output directory: {output_dir}")
            messagebox.showerror("Output Error", "Please select a valid output directory.")
            return

        output_image_path = upscale_pixel_art(Image.open(input_path), output_dir, scale_factor)
        messagebox.showinfo("Success", f"Upscaling complete. Resized image saved to: {output_image_path}")
    except ValueError:
        logging.error("Invalid scale factor entered.")
        messagebox.showerror("Invalid Scale Factor", "Please enter a valid number for the scale factor.")
    except Exception as e:
        logging.error(f"Error during upscaling process: {str(e)}")
        messagebox.showerror("Error", f"An error occurred during upscaling: {str(e)}")

# Initialize the GUI
root = tk.Tk()
root.title("Image Resizer")

# Variables to hold file paths
input_image_path = tk.StringVar()
output_directory = tk.StringVar()

# Input image selection
tk.Label(root, text="Input Image:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_image_path, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_input_image).grid(row=0, column=2, padx=10, pady=10)

# Output directory selection
tk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_directory, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_directory).grid(row=1, column=2, padx=10, pady=10)

# Scale factor entry
tk.Label(root, text="Scale Factor:").grid(row=2, column=0, padx=10, pady=10)
scale_factor_entry = tk.Entry(root)
scale_factor_entry.grid(row=2, column=1, padx=10, pady=10)
scale_factor_entry.insert(0, "2.0")  # Default scale factor is 2.0

# Start button
tk.Button(root, text="Start Upscaling", command=start_upscaling).grid(row=3, column=1, pady=20)

root.mainloop()
