import cv2
import face_recognition
from agender import Agender

agender = Agender()

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()
    face_locations = face_recognition.face_locations(frame)

    for (top, right, bottom, left) in face_locations:
        face_image = frame[top:bottom, left:right]
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

        faces = agender.detect_genders_ages(frame)
        if faces:
            age, gender = faces[0]['age'], faces[0]['gender']
        else:
            age, gender = "Unknown", "Unknown"

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, f'Gender: {gender}', (left, bottom + 20), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f'Age: {age}', (left, bottom + 40), font, 0.5, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

