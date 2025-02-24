import cv2
import os

img = cv2.imread("bat.jpg")  # Replace with the correct image path

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(255)}

n, m, z = 0, 0, 0

for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3  # Cycle through RGB channels

cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg")  # Open the image on Windows

with open("password.txt", "w") as f:
    f.write(password)  # Store password in a file

print("Encryption complete. Encrypted image saved as 'encryptedImage.jpg'.")
