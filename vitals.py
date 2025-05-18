import cv2
import mediapipe as mp

def get_vitals():
    cap = cv2.VideoCapture(0)
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()

    vitals_data = {}

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb_frame)

        if results.multi_face_landmarks:
            # Simulate vitals for now
            vitals_data = {
                "Heart Rate": "78 bpm",
                "Stress Level": "Normal",
                "BP Estimate": "120/80"
            }
            break

    cap.release()
    cv2.destroyAllWindows()
    return vitals_data