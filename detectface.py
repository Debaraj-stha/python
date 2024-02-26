import face_recognition
from PIL import Image
from datetime import datetime

def save_face_images(image_path, output_folder):
    
    image = face_recognition.load_image_file(image_path)

    
    face_locations = face_recognition.face_locations(image)

    
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    
    for i, face_location in enumerate(face_locations):
        
        top, right, bottom, left = face_location

        
        face_image = image[top:bottom, left:right]

        
        face_image = Image.fromarray(face_image)

        
        face_image.save(f"{output_folder}/face_{current_datetime}_{i+1}.jpg")


image_path = "your_file.jpg"
output_folder = "output_faces"
save_face_images(image_path, output_folder)
