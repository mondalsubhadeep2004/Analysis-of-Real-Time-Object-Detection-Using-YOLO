from ultralytics import YOLO
import cv2
import time

# Load your trained model
model = YOLO("final_automotive_yolo_best.pt")

# Open laptop webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Camera could not be opened.")
    exit()

print("Camera started.")
print("Press Q to quit.")

while True:

    # Read camera frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to read camera frame.")
        break

    # Start timer
    start_time = time.time()

    # YOLO detection
    results = model(
        frame,
        conf=0.40,
        imgsz=640,
        verbose=False
    )

    # Draw bounding boxes
    annotated_frame = results[0].plot()

    # Calculate FPS
    end_time = time.time()

    fps = 1 / (end_time - start_time)

    # Display FPS
    cv2.putText(
        annotated_frame,
        f"FPS: {fps:.2f}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    # Display camera
    cv2.imshow(
        "Automotive Component Detection",
        annotated_frame
    )

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()