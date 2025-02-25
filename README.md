# Face Recognition Attendance System

## Overview
This project is a Face Recognition-based Attendance System that utilizes OpenCV and face_recognition libraries to mark attendance based on facial recognition. The system detects faces from a live camera feed and matches them against known images stored in a directory. It then logs attendance into an Excel file with timestamps.

## Features
- Live face detection and recognition using OpenCV and face_recognition.
- Stores attendance records in an Excel file.
- Automatically marks individuals as absent if they are not detected.
- Real-time display of detected faces with labeled names.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install opencv-python
pip install face-recognition
pip install pandas
pip install openpyxl
```

## How It Works
1. **Load Known Faces:**
   - The script loads images from the `known-image` directory and extracts facial encodings.
   
2. **Start Camera Capture:**
   - The webcam captures frames and detects faces in real-time.

3. **Face Recognition & Attendance Logging:**
   - The detected faces are compared with stored encodings.
   - If a match is found, the person's name is logged into an Excel file with the current timestamp.
   - If the person is not detected, they are marked as absent.

4. **Exit and Save Attendance:**
   - Press `e` to stop the program and save the attendance log.

## Usage
1. Place images of known individuals inside the `known-image` directory. The filename (without extension) will be used as the person's name.
2. Run the script:
   ```bash
   python face_recognition_attendance.py
   ```
3. Attendance will be saved in an Excel file named `attendanceYYYY-MM-DD.xlsx`.

## File Structure
```
├── known-image/          # Folder containing known images (JPG/PNG)
├── face_recognition_attendance.py  # Main script
└── attendanceYYYY-MM-DD.xlsx  # Auto-generated attendance file
```

## Future Improvements
- Add a GUI for better user interaction.
- Store attendance records in a database instead of Excel.
- Implement multi-camera support.

## License
This project is open-source. Feel free to use and modify it.

