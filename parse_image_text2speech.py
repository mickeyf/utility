import pyttsx3  #text to speech engine 
from PIL import Image
from pytesseract import image_to_string

def parse_pic(file):
    try:
         processed_image = Image.open(file)  
         saltAndPepper = processed_image.convert('L')       #converts image to black and white      
         text = image_to_string(saltAndPepper)          
    except:
         Exception
         begin()
    inked(str(text))
    text2Speech(text)
    
def text2Speech(text):
    speech_engine = pyttsx3.init()
    speech_engine.say(text)
    speech_engine.runAndWait()    

def inked(text):
    file_name = input('Please enter a file name to write the parsed text to disc: ')
    with open('{}'.format(file_name),'w') as ink:
            ink.write(str(text))
            print(text)
            print("{} has been written to successfully".format(file_name))

def instructions():
    print("This program will attempt to extract text from an image file:\n")

def begin():
    instructions()
    path_to_file = input("Please provide a full path for the image file you wish to parse:\n")
    parse_pic(path_to_file)

if __name__ == '__main__':
    begin()

#In 2018 I learned how to code in python3  Happy New Year's Eve  12-31-18   si3mshady = El AD 
#updated with image rendering and text to speech capability 1-12-19  si3mshady = El AD 