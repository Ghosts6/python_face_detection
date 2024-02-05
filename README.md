![baner](https://github.com/Ghosts6/Local-website/blob/main/img/Baner.png)
# 👨🏻‍💻Face detection:

Here we have source code of two python program that i write to detect faces with help of webcam 

<img width="1470" alt="Screenshot 2024-02-05 at 8 53 47 PM" src="https://github.com/Ghosts6/python_face_detection/assets/95994481/47c35091-c986-413e-91fe-68d6335dc4e0">



# bash file:

in this repo i also provide a bash script to help you with requirement you can use it on macos and linux to install model you need to run program but first you need to make the file excuteable:

```bash
1chmod +x Requirement.sh
2./Requirement.sh
```

Requirement.sh
```bash
#!/bin/bash

# macOS
if [ "$(uname)" == "Darwin" ]; then
    if ! command -v brew &> /dev/null; then
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    fi
    brew install openblas
    brew install opencv
    brew install cmake
# linux
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    sudo apt-get update
    sudo apt-get install -y libopencv-dev
    sudo apt-get install -y cmake
else
    echo "Unsupported operating system"
    exit 1
fi
pip install numpy && pip install numpy===1.21.2
pip install py-agender face_recognition
```

# face_v1:

on first program we have simple code that work with models like cv2 and sys which you can access them with installing opencv and updated version of python,this program only can detect face and mark it.

```python
import cv2
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <path_to_haarcascade.xml>")
    sys.exit(1)

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)

while True:

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw frame faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object
video_capture.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()
```

# face_v2:

unlike first program which you could only detect faces on this one we add some other feature like detect gender and age so for accessing this features we need others model like agender and face_recognition by installing py-agender,numpy and numpy 1.21.2 version 

```python
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
```

