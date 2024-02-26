
import face_recognition as fr
import numpy as np

rajesh = "image/image1.jpeg"
pradip = "image/image3.jpeg"
shrinkhala = "image/image4.jpeg"
images = [rajesh, pradip]

names = ["rajesh", "pradip"]


def getFaces():
    encoding = {}
    for image, name in zip(images, names):
        face = fr.load_image_file(image)
        encodeFace = fr.face_encodings(face)
        if len(encodeFace) > 0:
            encoding[name] = encodeFace[0]
    return encoding


def classifyFace(img):
    faces = getFaces()
    known_face_names = list(faces.keys())
    img = fr.load_image_file(img)

    try:
        face_locations = fr.face_locations(img)
        unknown_face_encodings = fr.face_encodings(img, face_locations)
        face_names = []

        for face_encoding in unknown_face_encodings:
            matches = fr.compare_faces(list(faces.values()), face_encoding)
            if True in matches:
                best_match_index = np.argmin(fr.face_distance(list(faces.values()), face_encoding))
                name = known_face_names[best_match_index]
            else:
                name = "Unknown"
            face_names.append(name)
        return face_names
    except Exception as e:
        print(f"Exception {e}")
        return False


if __name__ == "__main__":
    res = classifyFace(shrinkhala)
    print(res)
