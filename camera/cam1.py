import cv2
import numpy as np

def draw_dog_face(frame, face_cascade):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Calculate the center of the face
        center_x = x + w // 2
        center_y = y + h // 2

        # Draw basic dog face features
        # Draw head (circle)
        cv2.circle(frame, (center_x, center_y), h // 2, (0, 0, 0), -1)

        # Draw ears (triangles)
        ear_size = w // 4
        ear_points = np.array([(center_x - ear_size, y),
                               (center_x + ear_size, y),
                               (center_x, y - ear_size)], np.int32)
        cv2.fillPoly(frame, [ear_points], (0, 0, 0))

        # Draw outline for ears
        cv2.polylines(frame, [ear_points], isClosed=True, color=(255, 255, 255), thickness=2)

        # Draw eyes (circles)
        eye_size = w // 10
        cv2.circle(frame, (center_x - eye_size - 15, center_y - h // 4), eye_size, (255, 255, 255), -1)
        cv2.circle(frame, (center_x + eye_size + 15, center_y - h // 4), eye_size, (255, 255, 255), -1)

    return frame

def main():
    # Load the pre-trained face cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the default camera (camera index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Draw basic dog face features
        frame_with_dog_face = draw_dog_face(frame, face_cascade)

        # Display the result
        cv2.imshow('Dog Face', frame_with_dog_face)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
