import torch
import io
#import torch.nn as nn
#import torchvision.transforms as transforms
#from torchvision import models
from PIL import Image
from torchvision.models import  ResNet50_Weights
import random
import numpy as np
model_path="model.pt"
class_names = {  0: 'Abyssinian',
		 1: 'American Curl',
		 2: 'American Shorthair',
		 3: 'Balinese',
		 4: 'Bengal',
		 5: 'Birman',
		 6: 'Bombay',
		 7: 'British Shorthair',
		 8: 'Burmese',
		 9: 'Cornish Rex',
		 10: 'Devon Rex',
		 11: 'Egyptian Mau',
		 12: 'Exotic Shorthair',
		 13: 'Extra-Toes Cat - Hemingway Polydactyl',
		 14: 'Havana',
		 15: 'Himalayan',
		 16: 'Japanese Bobtail',
		 17: 'Korat',
		 18: 'Maine Coon',
		 19: 'Manx',
		 20: 'Nebelung',
		 21: 'Norwegian Forest Cat',
		 22: 'Oriental Short Hair',
		 23: 'Persian',
		 24: 'Ragdoll',
		 25: 'Russian Blue',
		 26: 'Scottish Fold',
		 27: 'Selkirk Rex',
		 28: 'Siamese',
		 29: 'Siberian',
		 30: 'Snowshoe',
		 31: 'Sphynx',
		 32: 'Tonkinese',
		 33: 'Toyger tiger cat',
		 34: 'Turkish Angora'}
def get_cat_breed(img):
        random_seed = 2023
        np.random.seed(random_seed)
        torch.manual_seed(random_seed)
        random.seed(random_seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        dev = "cuda" if torch.cuda.is_available() else "cpu"
        model = torch.load(model_path,map_location=torch.device(dev))
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


