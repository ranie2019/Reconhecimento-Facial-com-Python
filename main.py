import cv2
import mediapipe as mp

# inicializar o opencv e a mediapipe
webcam = cv2.VideoCapture(0)
solucao_reconhecimento_rosto = mp.solutions.face_detection
reconhedor_rostos = solucao_reconhecimento_rosto.FaceDetection()
desenho = mp.solutions.drawing_utils

while True:
    # ler as informacoes da webcam
    verificador, frame = webcam.read()

    if not verificador:
        break
    # reconhecer os rostos que tem ali dentro
    lista_rostos = reconhedor_rostos.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            # desenhar os rostos na imagem
            desenho.draw_detection(frame, rosto)

    cv2.imshow("rostos na Webcam", frame)

    # quando aperta esc, para o loop
    if cv2.waitKey(5) == 27:
        break
webcam.release()
cv2.destroyWindow()
