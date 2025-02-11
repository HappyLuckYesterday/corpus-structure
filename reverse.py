def reverse_bits_in_file(input_file_path, output_file_path):  
    """  
    Reverses the bits of each byte in a file and saves the result to a new file.  

    Args:  
        input_file_path (str): The path to the input file.  
        output_file_path (str): The path to the output file.  
    """  

    try:  
        with open(input_file_path, 'rb') as infile, open(output_file_path, 'wb') as outfile:  
            while True:  
                byte = infile.read(1)  # Read one byte at a time  
                if not byte:  
                    break  # End of file  

                # Reverse the bits in the byte  
                reversed_byte = reverse_bits(byte[0])  # byte is a bytes object, so we take the first element  

                # Write the reversed byte to the output file  
                outfile.write(bytes([reversed_byte]))  # Convert back to bytes object for writing  

    except FileNotFoundError:  
        print(f"Error: Input file '{input_file_path}' not found.")  
    except Exception as e:  
        print(f"An error occurred: {e}")  


def reverse_bits(byte):  
    """Reverses the bits in a single byte (0-255)."""  
    reversed_byte = 0  
    for i in range(8):  
        if (byte >> i) & 1:  
            reversed_byte |= 1 << (7 - i)  
    return reversed_byte  


# Example usage:  
input_file = 'input'  # Replace with your input file  
output_file = 'output'  # Replace with your desired output file  
reverse_bits_in_file(input_file, output_file)  
print(f"Bits reversed and saved to {output_file}")