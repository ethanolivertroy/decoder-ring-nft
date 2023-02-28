# decoder-ring-nft

In this script, the extract_embedded_file() function first loads the NFT file and extracts the base64-encoded data from the image field. The function then decodes the data and locates the start and end of the embedded file, which is a JPEG image that contains the actual embedded file.

To extract the embedded file from the JPEG image, the function uses a steganography tool (in this example, steghide) and a password to extract the embedded file to a new file with the extension .mp4. Finally, the function displays the extracted file using the default application for opening MP4 files on the user's operating system.

Note that this script assumes that the steganography tool steghide is installed on the user's system and that the password used to embed the file is known. If a different steganography tool was used or if the password is unknown, the script will need to be modified accordingly.