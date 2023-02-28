import base64
import json
import os

def extract_embedded_file(nft_file_path):
    # Load the NFT file
    with open(nft_file_path, 'r') as f:
        nft_data = json.load(f)

    # Get the data encoded in base64 format
    data_encoded = nft_data['data']['image'].split(',')[1]

    # Decode the base64 data
    data_decoded = base64.b64decode(data_encoded)

    # Locate the start and end of the embedded file
    start_index = data_decoded.find(b'\xff\xd8')
    end_index = data_decoded.find(b'\xff\xd9')

    # Extract the JPEG image that contains the embedded file
    image_data = data_decoded[start_index:end_index+2]
    image_filename = os.path.splitext(nft_file_path)[0] + '_image.jpg'
    with open(image_filename, 'wb') as f:
        f.write(image_data)

    # Use a steganography tool to extract the embedded file from the JPEG image
    # Replace 'steghide' and 'password' with the appropriate tool and password for your case
    os.system(f'steghide extract -sf {image_filename} -p password -xf embedded_file.mp4')

    # Display the extracted file
    filename = os.path.splitext(nft_file_path)[0] + '_embedded.mp4'
    os.startfile(filename)

# Example usage
nft_file_path = 'example_nft.json'
extract_embedded_file(nft_file_path)
