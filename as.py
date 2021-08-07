import os 
import sys
import cv2
from PIL import Image

ASCII_CHARS= [".","#","|","%","?","*","+","O",":",",","-"]


def resized_gray_image(image ,new_width=70):
    width,height = image.size
    aspect_ratio = height / width
    new_height =int( new_width * aspect_ratio)
    resized_gray_image = image.resize((new_width,new_height)).convert('L')
    
    return resized_gray_image


def pix2chars(image):
    pixels = image.getdata()
    characters= "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    
    return characters

def generate_frame(image,new_width=70):
    new_image_data=pix2chars(resized_gray_image(image))
    total_pixels = len(new_image_data)
    ascii_image= "\n".join([new_image_data[index:(index+new_width)] for index in range(0,total_pixels,new_width)])
    

    sys.stdout.write(ascii_image)

    os.system('cls')

video_folder = "video/badapple.mp4"
cap = cv2.VideoCapture(video_folder)

video_name= video_folder.split("/")[1].split(".")[0]

while True:
    ret,frame =cap.read()
    cv2.imshow(video_name,frame) 
    generate_frame(Image.fromarray(frame))
    cv2.waitKey(10)
   
