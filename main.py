import cv2
import argparse  #인자 파싱 모듈

parser=argparse.ArgumentParser()
parser.add_argument('--image')

args=parser.parse_args()

#.pbtxt:TensorFlow 파일
#얼굴 감지 파일
faceProto="opencv_face_detector.pbtxt"
faceModel="opencv_face_detector_uint8.pb"
#성별 감지 파일
genderProto="gender_deploy.prototxt"
genderModel="gender_net.caffemodel"
#연령 감지 파일
ageProto="age_deploy.prototxt"
ageModel="age_net.caffemodel"

MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
genderList=['Male','Female']

faceNet=cv2.dnn.readNet(faceModel,faceProto)
ageNet=cv2.dnn.readNet(ageModel,ageProto)
genderNet=cv2.dnn.readNet(genderModel,genderProto)