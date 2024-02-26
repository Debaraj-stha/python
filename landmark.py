import face_recognition as fr
from PIL import Image, ImageDraw
import os

def drawLandMark(imagePath, folder):
    if os.path.exists(folder):
        print("Folder already exists.")
    else:
        os.mkdir(folder)
        print("Folder created.")
    
    image = fr.load_image_file(imagePath)
    landmarks = fr.face_landmarks(image)
    
    for face_landmarks in landmarks:
        pil_image = Image.fromarray(image)
        d = ImageDraw.Draw(pil_image)
        
        
        for facial_feature in face_landmarks.keys():
            d.line(face_landmarks[facial_feature], width=5)
        
        
        pil_image.save(os.path.join(folder, os.path.basename(imagePath)))

if __name__ == "__main__":
    image = "image/image3.jpeg"
    folder = "landmark"
    drawLandMark(image, folder)
