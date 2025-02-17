import tkinter as tk  
from tkinter import filedialog, messagebox  
import os  

def reverse_bits_in_bytes(content, n):  
    """Reverse the bits within the first n bytes."""  
    n = min(n, len(content))  # If n exceeds the file size, use the file size  

    # Create a copy of the content to modify  
    new_content = bytearray(content)  

    for byte_index in range(n):  
        byte = content[byte_index]  
        # Reverse the bits in the byte  
        reversed_byte = 0  
        for bit_index in range(8):  
            if (byte >> bit_index) & 1:  # Check if the bit is set  
                reversed_byte |= (1 << (7 - bit_index))  # Set the reversed bit  

        new_content[byte_index] = reversed_byte  # Save the reversed byte  

    return new_content  

def reverse_first_n_bytes(file_path, n):  
    """Reverse the bits of the first n bytes of the file, keeping the remaining bytes unchanged."""  
    with open(file_path, 'rb') as file:  
        content = bytearray(file.read())  

    # Reverse bits in the first n bytes  
    new_content = reverse_bits_in_bytes(content, n)  

    # Create a new filename using the original filename and n  
    original_filename = os.path.basename(file_path)  
    new_filename = f"reverse-{n}-{original_filename}"  

    # Save the result to the new filename  
    with open(new_filename, 'wb') as file:  
        file.write(new_content)  

    return new_filename  

def select_file():  
    """Open a file dialog and insert the file path into the entry."""  
    file_path = filedialog.askopenfilename()  
    file_entry.delete(0, tk.END)  
    file_entry.insert(0, file_path)  

def process_file():  
    """Process the selected file to reverse the first n bytes."""  
    file_path = file_entry.get()  
    try:  
        n = int(bit_count_entry.get())  
        if not os.path.isfile(file_path):  
            raise ValueError("File does not exist.")  
        new_filename = reverse_first_n_bytes(file_path, n)  
        messagebox.showinfo("Success", f"Reversed the first {n} bytes of '{file_path}' and saved as '{new_filename}'")  
    except ValueError as e:  
        messagebox.showerror("Error", f"Invalid input: {e}")  

# Create the main window  
root = tk.Tk()  
root.title("Reverse Bytes Utility")  

# Create and place labels and entries  
tk.Label(root, text="Select File:").grid(row=0, column=0, padx=10, pady=10)  
file_entry = tk.Entry(root, width=50)  
file_entry.grid(row=0, column=1, padx=10, pady=10)  
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)  

tk.Label(root, text="Number of Bytes to Reverse:").grid(row=1, column=0, padx=10, pady=10)  
bit_count_entry = tk.Entry(root, width=10)  
bit_count_entry.grid(row=1, column=1, padx=10, pady=10)  

# Process button  
process_button = tk.Button(root, text="Reverse", command=process_file)  
process_button.grid(row=2, column=1, pady=20)  

# Run the app  
root.mainloop()