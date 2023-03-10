import torch
import io
#import torch.nn as nn
#import torchvision.transforms as transforms
#from torchvision import models
from PIL import Image
from torchvision.models import  ResNet50_Weights
import random
import numpy as np
class_names={0: 'Abyssinian',
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
              13: 'Chartreux',
              14: 'Chausie',
              15: 'Chinchilla',
              16: 'Cornish Rex',
              17: 'Cymric',
              18: 'Devon Rex',
              19: 'Egyptian Mau', 
              20: 'Exotic Shorthair',
              21: 'Extra-Toes Cat - Hemingway Polydactyl',
              22: 'Havana', 23: 'Himalayan',
              24: 'Japanese Bobtail',
              25: 'Javanese', 
              26: 'Korat',
              27: 'LaPerm',
              28: 'Maine Coon',
              29: 'Manx', 
              30: 'Munchkin',
              31: 'Nebelung', 
              32: 'Norwegian Forest Cat',
              33: 'Ocicat',
              34: 'Oriental Long Hair',
              35: 'Oriental Short Hair',
              36: 'Oriental Tabby', 
              37: 'Persian', 
              38: 'Pixiebob', 
              39: 'Ragamuffin',
              40: 'Ragdoll', 
              41: 'Russian Blue',
              42: 'Scottish Fold',
              43: 'Selkirk Rex', 
              44: 'Siamese', 
              45: 'Siberian',
              46: 'Singapura',
              47: 'Snowshoe',
              48: 'Somali', 
              49: 'Sphynx - Hairless Cat',
              50: 'Tonkinese',
              51: 'Toyger tiger cat', 
              52: 'Turkish Angora',
              53: 'Turkish Van', 
              54: 'York Chocolate'}
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


