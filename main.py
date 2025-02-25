import os
from datetime import datetime

import face_recognition
import cv2
import pandas as pd

known_encodings = []
known_names = []

directory_path = "known-image"  # Path to the directory containing the images

for filename in os.listdir(directory_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(directory_path, filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)

        if len(encoding) > 0:
            known_encodings.append(encoding[0])
            known_names.append(os.path.splitext(filename)[0])  # Use filename as the label (removing the extension)

video_capture = cv2.VideoCapture(0)
current_date = datetime.now().strftime('%Y-%m-%d')
excel_file = "attendance{0}.xlsx".format(current_date)

try:
    df=pd.read_excel(excel_file)
except FileNotFoundError:
    data= {"Name":[],"Presence":[]}
    df= pd.DataFrame(data)

while True:
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_names[first_match_index]

        if name != "Unknown":
            if name in known_names and name not in df["Name"].values:
                current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                df= df._append({"Name":name,"Presence":current_time}, ignore_index = True)


        face_names.append(name)

    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)

    cv2.imshow('Focus', frame)
    #

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

video_capture.release()
cv2.destroyAllWindows()

for name in known_names:
    if name not in df['Name'].values:
        # current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        absent = "Absent"
        df = df._append({'Name': name, 'Presence': absent}, ignore_index=True)

df.to_excel(excel_file, index=False)
