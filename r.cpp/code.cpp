#include <iostream>  
#include <fstream>  
#include <string>  
#include <cstdlib> // For exit function  
#include <vector>  

unsigned char reverseBits(unsigned char byte) {
    unsigned char reversed = 0;
    for (int i = 0; i < 8; ++i) {
        // Shift the bit from the byte to the reversed byte  
        reversed <<= 1; // Shift reversed byte left by 1  
        reversed |= (byte & 1); // Get the last bit of byte and add to reversed  
        byte >>= 1; // Shift byte right by 1  
    }
    return reversed;
}

void bitReverseFile(const std::string& inputFileName, const std::string& outputFileName, int n) {
    // Open the input file  
    std::ifstream inputFile(inputFileName, std::ios::binary);
    if (!inputFile) {
        std::cerr << "Error opening input file: " << inputFileName << std::endl;
        exit(EXIT_FAILURE);
    }

    // Read the contents of the file into a vector  
    std::vector<unsigned char> content((std::istreambuf_iterator<char>(inputFile)),
        std::istreambuf_iterator<char>());
    inputFile.close(); // Close the input file  

    // Check if n is bigger than the file size  
    if (n > content.size()) {
        n = content.size(); // Adjust n to the file size if it is larger  
    }

    // Bit reverse the first n bytes  
    for (int i = 0; i < n; ++i) {
        content[i] = reverseBits(content[i]);
    }

    // Write the modified content to the output file  
    std::ofstream outputFile(outputFileName, std::ios::binary);
    if (!outputFile) {
        std::cerr << "Error opening output file: " << outputFileName << std::endl;
        exit(EXIT_FAILURE);
    }

    // Write entire content back to output file  
    outputFile.write(reinterpret_cast<const char*>(content.data()), content.size());
    outputFile.close(); // Close the output file  
    std::cout << "File processed and saved as: " << outputFileName << std::endl;
}

int main() {
    while (true)
    {
        std::string inputFileName, outputFileName;
        int n;

        // Get the input file name  
        std::cout << "\nEnter the input file name: ";
        std::getline(std::cin, inputFileName);

        // Get the number of bytes to reverse  
        std::cout << "Enter the number of bytes to reverse: ";
        std::cin >> n;

        // Get the output file name  
        std::cout << "Enter the output file name: ";
        std::cin.ignore(); // To clear the newline left in the buffer  
        std::getline(std::cin, outputFileName);

        // Process the file for bit reversal  
        bitReverseFile(inputFileName, outputFileName, n);
    }

    return 0;
}