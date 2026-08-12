from skimage.feature import graycomatrix, graycoprops
from mahotas.features import haralick
from BiT import bio_taxo
import cv2
import numpy as np

def glcm_rgb(chemin):
    data=cv2.imread(chemin)
    img_rgb=cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
    list_carac=[]
    canals=['R','G','B']
    for i, canal in enumerate(canals):
        image=img_rgb[:,:,i]
        co_matrice=graycomatrix(image,[1],[np.pi/2],None,symmetric=True,normed=False)
        contrast=float(graycoprops(co_matrice,'contrast')[0,0])
        dissimilarity=float(graycoprops(co_matrice,'dissimilarity')[0,0])
        homogeneity=float(graycoprops(co_matrice,'homogeneity')[0,0])
        correlation=float(graycoprops(co_matrice,'correlation')[0,0])
        ASM=float(graycoprops(co_matrice,'ASM')[0,0])
        energy=float(graycoprops(co_matrice,'energy')[0,0])
        list_carac.extend([contrast,dissimilarity,homogeneity,correlation,ASM,energy])
    return list_carac
   
def haralick_feat_rgb(chemin):
    data=cv2.imread(chemin)
    img_rgb=cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
    list_carac=[]
    canals=['R','G','B']
    for i, canal in enumerate(canals):
        image=img_rgb[:,:,i]
        features=haralick(image).mean(0).tolist()
        features=[float(x) for x in features]
        list_carac.extend(features)
    return list_carac
 
def bitdesc_rgb(chemin):
    data=cv2.imread(chemin)
    img_rgb=cv2.cvtColor(data,cv2.COLOR_BGR2RGB)
    list_carac=[]
    canals=['R','G','B']
    for i, canal in enumerate(canals):
        image=img_rgb[:,:,i]
        features=bio_taxo(image)
        features=[float(x) for x in features]
        list_carac.extend(features)
    return list_carac
 
def concatenation_rgb(chemin):
    return glcm_rgb(chemin)+haralick_feat_rgb(chemin)+bitdesc_rgb(chemin)