import torch
import io
#import torch.nn as nn
#import torchvision.transforms as transforms
#from torchvision import models
from PIL import Image
from torchvision.models import  ResNet50_Weights
import random
import numpy as np
class_names= {
    0: 'Abyssinian',
    1: 'American Bobtail',
    2: 'American Curl',
    3: 'American Shorthair',
    4: 'American Wirehair',
    5: 'Applehead Siamese',
    6: 'Balinese',
    7: 'Bengal',
    8: 'Birman',
    9: 'Bombay',
    10: 'British Shorthair',
    11: 'Burmese',
    12: 'Burmilla',
    13: 'Calico',
    14: 'Canadian Hairless',
    15: 'Chartreux',
    16: 'Chausie',
    17: 'Chinchilla',
    18: 'Cornish Rex',
    19: 'Cymric',
    20: 'Devon Rex',
    21: 'Dilute Calico',
    22: 'Dilute Tortoiseshell',
    23: 'Domestic Long Hair',
    24: 'Domestic Medium Hair',
    25: 'Domestic Short Hair',
    26: 'Egyptian Mau',
    27: 'Exotic Shorthair',
    28: 'Extra-Toes Cat - Hemingway Polydactyl',
    29: 'Havana',
    30: 'Himalayan',
    31: 'Japanese Bobtail',
    32: 'Javanese',
    33: 'Korat',
    34: 'LaPerm',
    35: 'Maine Coon',
    36: 'Manx',
    37: 'Munchkin',
    38: 'Nebelung',
    39: 'Norwegian Forest Cat',
    40: 'Ocicat',
    41: 'Oriental Long Hair',
    42: 'Oriental Short Hair',
    43: 'Oriental Tabby',
    44: 'Persian',
    45: 'Pixiebob',
    46: 'Ragamuffin',
    47: 'Ragdoll',
    48: 'Russian Blue',
    49: 'Scottish Fold',
    50: 'Selkirk Rex',
    51: 'Siamese',
    52: 'Siberian',
    53: 'Silver',
    54: 'Singapura',
    55: 'Snowshoe',
    56: 'Somali',
    57: 'Sphynx - Hairless Cat',
    58: 'Tabby',
    59: 'Tiger',
    60: 'Tonkinese',
    61: 'Torbie',
    62: 'Tortoiseshell',
    63: 'Turkish Angora',
    64: 'Turkish Van',
    65: 'Tuxedo',
    66: 'York Chocolate'}

def get_cat_breed(img):
        random_seed = 2023
        np.random.seed(random_seed)
        torch.manual_seed(random_seed)
        random.seed(random_seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        dev = "cuda" if torch.cuda.is_available() else "cpu"
        model = torch.load("5tensor(0.5101, device='cuda_0', dtype=torch.float64)resnet34.pt",map_location=torch.device(dev))
        model.eval()
        tensor=transform_image(img) 
        outputs=model.forward(tensor)
        i, prediction = torch.max(outputs, 1)
	
        return class_names[int(prediction.item())]
      
def transform_image(im):  
        weights = ResNet50_Weights.DEFAULT
        preprocess=weights.transforms()
        image = Image.open(io.BytesIO(im))
        return preprocess(image).unsqueeze(0)


