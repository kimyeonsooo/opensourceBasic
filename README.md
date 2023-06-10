# 👧나이 성별 예측 프로그램👨

<h3>사진, 비디오에서 얼굴을 감지하고 분석하는 애플리케이션으로</h3>
<p>실시간 비디오 스트림에서 얼굴을 감지하고 해당 얼굴의 성별과 나이를 분석하며, 분석 결과를 저장하는 스냅샷 기능을 제공합니다.</p>

## 팀 구성
- 팀원: 김연수, 손지연, 안유진

## 구현 기능
- 얼굴 감지: OpenCV의 DNN(Dependency Neural Network) 모듈을 사용하여 얼굴을 감지합니다.
- 성별 분석: 사전 훈련된 `gender_net.caffemodel` 모델을 사용하여 얼굴의 성별을 분석합니다.
- 나이 추정: 사전 훈련된 `age_net.caffemodel` 모델을 사용하여 얼굴의 나이를 추정합니다.
- 결과 표시: 감지된 얼굴 주변에 사각형 박스를 그리고, 해당 얼굴의 성별과 나이를 텍스트로 표시합니다.
- 스냅샷 저장: 스냅샷 버튼을 클릭하여 현재 프레임을 이미지 파일로 저장하고, 얼굴 분석 결과를 CSV 파일로 저장합니다.

## 사용 기술 및 환경
- 언어: Python
- 컴퓨터 비전 라이브러리: OpenCV
- 딥러닝 프레임워크: Caffe
- 모델: `opencv_face_detector`, `age_net`, `gender_net`
- 의존성 관리: pip
- 운영 체제: Windows, macOS

## 설치 방법
- OpenCV 설치: pip install opencv-python
- argparse 설치: pip install argparse

## 의존성
- OpenCv
- 추가 예정

## 사용 방법
- 웹캠:
python <실행 파일명>
`python main.py`
- 사진:
`python <실행 파일명> --image <이미지 파일>`
`python main.py --image girl1.jpg`
중단 방법: `Ctrl + C`

## 사용 예제
- ![image](https://github.com/kimyeonsooo/opensourceBasic/assets/82308315/495cdefa-3138-4879-af90-e1a040055bb1)
- ![image](https://github.com/kimyeonsooo/opensourceBasic/assets/82308315/cc79c42f-e9d1-4a94-aea8-6e8e2e366ad6)


## 라이선스 및 연락처
### 라이선스
MIT License

### 연락처
- 손지연(2020039104), 김연수(2020039097)
- 이메일: sjy7392@naver.com, yeonkiiim@gmail.com
