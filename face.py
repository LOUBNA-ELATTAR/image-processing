from PIL import Image
import face_recognition
import numpy as np
import argparse
import cv2

#passage des arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help =  "D:\\Projects\\traitement-images\\people4.jpg")
args = vars(ap.parse_args())

# charger et convertir une image dans une table numpy 
image = cv2.imread(args["image"])

# trouver tout les fisage et constituer une liste
visages_positions = face_recognition.face_locations(image)

# afficher le nombre de visage detécter 
print("J'ai trouvé  {} visage(s) dans cette photo".format(len(visages_positions)))

for visage_position in visages_positions:

	#Afficher la position de chaque visage trouvé dans l'image
	haut, droit, bas, gauche = visage_position
	print("un visage est detecter a la position: haut{}, gauche: {}, bas: {}, droit: {}".format(haut,  bas, gauche, droit))
	#accéder, afficher et enregistrer chaque visage trouvé dans l'image
	image_visage = image[haut:bas, gauche:droit]
	cv2.imshow("Visage detecte",image_visage)
	cv2.imwrite("visage -{}-{}-{}-{}.jpg".format(haut,  bas, gauche, droit),image_visage)
	cv2.waitKey(0) 