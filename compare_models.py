# compare_models.py  

def compare_files(file1, file2):  
    """Compare two binary files to see if they are identical."""  
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:  
        while True:  
            # Read a chunk of data from both files  
            chunk1 = f1.read(1024)  # Read 1024 bytes at a time  
            chunk2 = f2.read(1024)  

            # If both chunks are empty, we've reached the end of both files  
            if not chunk1 and not chunk2:  
                break  
            
            # If the chunks are not the same, return False  
            if chunk1 != chunk2:  
                return False  

    return True  

# Compare the original and recovered model files  
original_file = 'pytorch_model.bin'  
recovered_file = 'recovered_model.bin'  

if compare_files(original_file, recovered_file):  
    print("The original model and the recovered model are identical.")  
else:  
    print("The original model and the recovered model are different.")