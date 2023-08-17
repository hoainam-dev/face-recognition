import cv2
import numpy as np
import os
from PIL import Image

#neu bi loi => mo cmd(run as adm): pip uninstall opencv-contrib-python => pip install opencv-contrib-python
recognizer = cv2.face.LBPHFaceRecognizer_create()

path = 'dataSet'

def getImageWithId(path):
  #truy cap vao tat ca cac file trong thu muc dataSet
  imagePaths = [os.path.join(path, f) for f in os.listdir(path)]


  faces = []
  IDs = []

  for imagePath in imagePaths:

    faceImg = Image.open(imagePath).convert('L')

    faceNp = np.array(faceImg, 'uint8')

    Id = int(imagePath.split('.')[1])

    faces.append(faceNp)
    IDs.append(Id)

    cv2.imshow('Traning', faceNp)
    cv2.waitKey(10)
    
  return faces, IDs

faces, Ids = getImageWithId(path)

recognizer.train(faces, np.array(Ids))

if not os.path.exists('recognizer'):
  os.makedirs('recognizer')

recognizer.save('recognizer/trainingData.yml')

cv2.destroyAllWindows()
