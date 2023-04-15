import face_recognition
from PIL import Image, ImageDraw

# Charger l'image de la première personne et apprendre au système à la reconnaître
person1_image = face_recognition.load_image_file('D:\\Projects\\traitement-images\\ziyech.jpg')
person1_face_signature = face_recognition.face_encodings(person1_image)[0]

# Charger l'image de la deuxième personne et apprendre au système à la reconnaître
person2_image = face_recognition.load_image_file('D:\\Projects\\traitement-images\\ounahi.jpg')
person2_face_signature = face_recognition.face_encodings(person2_image)[0]

# Créer un tableau des signatures de visages associées aux noms de personnes
reconnu_face_signatures = [
    person1_face_signature,
    person2_face_signature
]
reconnu_face_noms = [
    "Ziyech",
    "Ounahi"
]

# Charger l'image avec les visages non reconnus
non_reconnu_image = face_recognition.load_image_file('D:\\Projects\\traitement-images\\maroc.jpeg')

# Trouver tous les visages et leurs signatures dans une image source
visage_locations = face_recognition.face_locations(non_reconnu_image)
visage_signatures = face_recognition.face_encodings(non_reconnu_image, visage_locations)

# Convertir l'image en format PIL pour qu'on puisse dessiner avec la librairie Pillow
# Regarder http://pillow.readthedocs.io/ pour plus d'informations sur PIL/Pillow
pil_image = Image.fromarray(non_reconnu_image)

# Créer une instance de Pillow ImageDraw pour dessiner sur l'image
img_dessin = ImageDraw.Draw(pil_image)

# Boucler sur les visages trouvés dans l'image à reconnaître
for (top, right, bottom, left), visage_signature in zip(visage_locations, visage_signatures):
    # Voir si le visage extrait correspond à un(des) visage(s) reconnu(s)
    matches = face_recognition.compare_faces(reconnu_face_signatures, visage_signature)

    nom_personne = "non_reconnu"

    # Si une correspondance est retrouvée dans les reconnu_face_signatures, seulement prendre le premier !
    if True in matches:
        first_match_index = matches.index(True)
        nom_personne = reconnu_face_noms[first_match_index]

    # Dessiner un rectangle autour du visage utilisant les modules de Pillow
    img_dessin.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Dessiner un label avec le texte du nom de visage reconnu
    text_width, text_height = img_dessin.textsize(nom_personne)
    img_dessin.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 255, 0), outline=(0, 0, 255))
    img_dessin.text((left + 6, bottom - text_height - 5), nom_personne, fill=(255, 0, 0, 255))


# Supprimer l'instance de dessin de la mémoire
del img_dessin

# Afficher l'image résultante
pil_image.show()

# Enregistrer l'image résultante
pil_image.save('D:\\Projects\\traitement-images\\maroc_resultat.jpeg')
