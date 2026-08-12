import os
import cv2
import numpy as np
from descripteur import concatenation_rgb as concatenation
from descripteur import glcm_rgb as glcm
from descripteur import haralick_feat_rgb as haralick_features
from descripteur import bitdesc_rgb as bitdesc




def extraction_signatures_concatenation_RGB(chemin_repertoire):
    list_caracteristiques=[]
    for root,_,files in os.walk(chemin_repertoire):
        for file in files:
            if file.lower().endswith(('.png','.jpg', '.jpeg')):
                # Lire l'image
                chemin_image = os.path.relpath(os.path.join(root, file),chemin_repertoire)
                path = os.path.join(root, file)
                caracteristiques = concatenation(path)
                # print(caracteristiques)
                class_name=os.path.dirname(chemin_image)
                list_caracteristiques.append(caracteristiques+[class_name,chemin_image])
                # la classe c'est le nom du contient qui contient l'image
    
    signatures=np.array(list_caracteristiques)
    np.save("signaturesConcatenationRGB.npy",signatures)
    
def extraction_signatures_GLCM_RGB(chemin_repertoire):
    list_caracteristiques=[]
    for root,_,files in os.walk(chemin_repertoire):
        for file in files:
            if file.lower().endswith(('.png','.jpg', '.jpeg')):
                # Lire l'image
                chemin_image = os.path.relpath(os.path.join(root, file),chemin_repertoire)
                path = os.path.join(root, file)
                caracteristiques = glcm(path)
                # print(caracteristiques)
                class_name=os.path.dirname(chemin_image)
                list_caracteristiques.append(caracteristiques+[class_name,chemin_image])
                # la classe c'est le nom du contient qui contient l'image
    
    signatures=np.array(list_caracteristiques)
    np.save("signaturesGLCMRGB.npy",signatures)


def extraction_signatures_haralick_RGB(chemin_repertoire):
    list_caracteristiques=[]
    for root,_,files in os.walk(chemin_repertoire):
        for file in files:
            if file.lower().endswith(('.png','.jpg', '.jpeg')):
                # Lire l'image
                chemin_image = os.path.relpath(os.path.join(root, file),chemin_repertoire)
                path = os.path.join(root, file)
                caracteristiques = haralick_features(path)
                # print(caracteristiques)
                class_name=os.path.dirname(chemin_image)
                list_caracteristiques.append(caracteristiques+[class_name,chemin_image])
                # la classe c'est le nom du contient qui contient l'image
    
    signatures=np.array(list_caracteristiques)
    np.save("signaturesHaralickRGB.npy",signatures)
    
def extraction_signatures_bitdesk_RGB(chemin_repertoire):
    list_caracteristiques=[]
    for root,_,files in os.walk(chemin_repertoire):
        for file in files:
            if file.lower().endswith(('.png','.jpg', '.jpeg')):
                # Lire l'image
                chemin_image = os.path.relpath(os.path.join(root, file),chemin_repertoire)
                path = os.path.join(root, file)
                caracteristiques = bitdesc(path)
                # print(caracteristiques)
                class_name=os.path.dirname(chemin_image)
                list_caracteristiques.append(caracteristiques+[class_name,chemin_image])
                # la classe c'est le nom du contient qui contient l'image
    
    signatures=np.array(list_caracteristiques)
    np.save("signaturesBitdeskRGB.npy",signatures)

    
    
def main():
    print("Début extraction Concatenation")
    extraction_signatures_concatenation_RGB("./dataset/")
    print("Fin extraction Concatenation")
    
    print("Début extraction GLCM")
    extraction_signatures_GLCM_RGB("./dataset/")
    print("Fin extraction GLCM")

    print("Début extraction Haralick")
    extraction_signatures_haralick_RGB("./dataset/")
    print("Fin extraction Haralick")

    print("Début extraction Bitdesk")
    extraction_signatures_bitdesk_RGB("./dataset/")
    print("Fin extraction Bitdesk")
    
if __name__ == "__main__":
    main()
    
    
