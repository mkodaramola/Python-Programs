# Manual base64 encoding map
base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def image_to_base64(image_path):
    # Read the image as binary data
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()

    encoded_string = ""
    padding = ""
    # Process the binary data in chunks of 3 bytes (24 bits)
    for i in range(0, len(binary_data), 3):
        # Get 3 bytes (24 bits)
        chunk = binary_data[i:i+3]
        
        # Add padding if the chunk is less than 3 bytes
        if len(chunk) == 1:
            chunk += b'\x00\x00'
            padding = '=='
        elif len(chunk) == 2:
            chunk += b'\x00'
            padding = '='   

        # Convert the 3-byte chunk into 24 bits
        bits = (chunk[0] << 16) + (chunk[1] << 8) + chunk[2]
        
        # Extract 4 groups of 6 bits each from the 24-bit value
        encoded_string += base64_chars[(bits >> 18) & 0x3F]
        encoded_string += base64_chars[(bits >> 12) & 0x3F]
        encoded_string += base64_chars[(bits >> 6) & 0x3F]
        encoded_string += base64_chars[bits & 0x3F]

    # Adjust for padding
    if padding:
        encoded_string = encoded_string[:-len(padding)] + padding

    return encoded_string

# Example usage
image_path = "img.png"  # Replace with the path to your image
base64_string = image_to_base64(image_path)
print(base64_string)