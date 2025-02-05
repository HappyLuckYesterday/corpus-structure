# bit_reverse_header.py  

def reverse_bits(byte):  
    """Reverse the bits of a single byte."""  
    return int('{:08b}'.format(byte)[::-1], 2)  

# Open the original model file  
with open('pytorch_model.bin', 'rb') as file:  
    # Read the first 64 bytes (the header)  
    header = file.read(64)  
    # Read the rest of the file  
    rest_of_file = file.read()  

# Reverse the bits of each byte in the header  
reversed_header = bytearray(reverse_bits(byte) for byte in header)  

# Create a new file with the modified header and the unmodified rest  
with open('modified_model.bin', 'wb') as modified_file:  
    modified_file.write(reversed_header)  # Write the reversed header  
    modified_file.write(rest_of_file)     # Write the rest of the file  

print("Header bit reversal complete. Saved to 'modified_model.bin'.")