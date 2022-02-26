import cv2
import face_recognition

img = cv2.imread("Test/0.jpg")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

for i in range (12):
    S=f"Test/{i}.jpg"
    img1 = cv2.imread(S)
    rgb_img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img_encoding1 = face_recognition.face_encodings(rgb_img1)[0]


    result = face_recognition.compare_faces([img_encoding], img_encoding1)
    print("Result "+str((i+1))+":" , result)
    
    cv2.imshow("Img "+str(i), img1)

cv2.waitKey(0)