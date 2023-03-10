import torch
import io
#import torch.nn as nn
#import torchvision.transforms as transforms
#from torchvision import models
from PIL import Image
from torchvision.models import  ResNet50_Weights
import random
import numpy as np
class_names= {'Abyssinian': 0,
 'American Bobtail': 1,
 'American Curl': 2,
 'American Shorthair': 3,
 'American Wirehair': 4,
 'Applehead Siamese': 5,
 'Balinese': 6,
 'Bengal': 7,
 'Birman': 8,
 'Bombay': 9,
 'British Shorthair': 10,
 'Burmese': 11,
 'Burmilla': 12,
 'Chartreux': 13,
 'Chausie': 14,
 'Chinchilla': 15,
 'Cornish Rex': 16,
 'Cymric': 17,
 'Devon Rex': 18,
 'Egyptian Mau': 19,
 'Exotic Shorthair': 20,
 'Extra-Toes Cat - Hemingway Polydactyl': 21,
 'Havana': 22,
 'Himalayan': 23,
 'Japanese Bobtail': 24,
 'Javanese': 25,
 'Korat': 26,
 'LaPerm': 27,
 'Maine Coon': 28,
 'Manx': 29,
 'Munchkin': 30,
 'Nebelung': 31,
 'Norwegian Forest Cat': 32,
 'Ocicat': 33,
 'Oriental Long Hair': 34,
 'Oriental Short Hair': 35,
 'Oriental Tabby': 36,
 'Persian': 37,
 'Pixiebob': 38,
 'Ragamuffin': 39,
 'Ragdoll': 40,
 'Russian Blue': 41,
 'Scottish Fold': 42,
 'Selkirk Rex': 43,
 'Siamese': 44,
 'Siberian': 45,
 'Singapura': 46,
 'Snowshoe': 47,
 'Somali': 48,
 'Sphynx - Hairless Cat': 49,
 'Tonkinese': 50,
 'Toyger tiger cat': 51,
 'Turkish Angora': 52,
 'Turkish Van': 53,
 'York Chocolate': 54}

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


