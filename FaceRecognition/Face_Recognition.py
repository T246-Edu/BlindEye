import cv2
import os
import face_recognition
from FaceRecognition.DetectKnows import DetecKnows


def detection1():
    video_capture = cv2.VideoCapture(0)
    listKnowns = DetecKnows()
    print(listKnowns)
    knownEncodings = []
    for known in listKnowns:
        known_image = face_recognition.load_image_file(
            "{}\\FaceRecognition\\DetectedFaces\\{}.jpg".format(os.getcwd(), known))
        knownEncodings.append(face_recognition.face_encodings(known_image)[0])
    while True:
        ret, frame = video_capture.read()
        cv2.imwrite(
            "{}//FaceRecognition//data//face.jpg".format(os.getcwd()), frame)
        unknown_image = face_recognition.load_image_file(
            "{}//FaceRecognition//data//face.jpg".format(os.getcwd()))
        unknown_encodings = face_recognition.face_encodings(unknown_image)
        for u_encoding in unknown_encodings:
            results = face_recognition.compare_faces(
                knownEncodings, u_encoding)
            try:
                for x in results:
                    if x ==True:
                        name: str = (listKnowns[results.index(x)])
                        print("I see a person named: {}".format(
                            name.replace(name[len(name)-1], "")))
            except:
                print("Didn't recognize the person")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
