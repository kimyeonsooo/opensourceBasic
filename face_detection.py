import cv2

MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
age = ['(0-2)', '(4-6)', '(8-12)', '(15-20)',
            '(25-32)', '(38-43)', '(48-53)', '(60-100)']
gender = ['Male', 'Female']

def highlight(net, frame, conf_threshold=0.7):
    frame_opencv_dnn = frame.copy()

def process(face_net, age_net, gender_net, frame, padding=20):
    result_img, face_boxes = highlight(face_net, frame)
    data = []
