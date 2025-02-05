# recover_original_header.py  

def reverse_bits(byte):  
    """Reverse the bits of a single byte."""  
    return int('{:08b}'.format(byte)[::-1], 2)  

# Open the modified model file  
with open('modified_model.bin', 'rb') as file:  
    # Read the first 64 bytes (the modified header)  
    modified_header = file.read(64)  
    # Read the rest of the file  
    rest_of_file = file.read()  

# Reverse the bits of each byte in the modified header to recover the original  
recovered_header = bytearray(reverse_bits(byte) for byte in modified_header)  

# Create a new file with the original header and the unmodified rest  
with open('recovered_model.bin', 'wb') as original_file:  
    original_file.write(recovered_header)   # Write the recovered header  
    original_file.write(rest_of_file)       # Write the rest of the file  

print("Header recovery complete. Saved to 'recovered_model.bin'.")