import cv2

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
age_list = ['(0-2)', '(4-6)', '(8-12)', '(15-20)',
            '(25-32)', '(38-43)', '(48-53)', '(60-100)']
gender_list = ['Male', 'Female']


def highlight_face(net, frame, conf_threshold=0.7):
    frame_opencv_dnn = frame.copy()
    frame_height = frame_opencv_dnn.shape[0]
    frame_width = frame_opencv_dnn.shape[1]
    blob = cv2.dnn.blobFromImage(frame_opencv_dnn, 1.0, (300, 300), [
                                 104, 117, 123], True, False)
    net.setInput(blob)
    detections = net.forward()
    face_boxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3]*frame_width)
            y1 = int(detections[0, 0, i, 4]*frame_height)
            x2 = int(detections[0, 0, i, 5]*frame_width)
            y2 = int(detections[0, 0, i, 6]*frame_height)
            face_boxes.append([x1, y1, x2, y2])
            cv2.rectangle(frame_opencv_dnn, (x1, y1), (x2, y2),
                          (0, 255, 0), int(round(frame_height/150)), 8)
            return frame_opencv_dnn

def process_frame(face_net, age_net, gender_net, frame, padding=20):
    result_img, face_boxes = highlight_face(face_net, frame)
    data = []

    if not face_boxes:
        print("No face detected")