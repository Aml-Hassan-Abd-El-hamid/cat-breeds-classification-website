import torch
import io
#import torch.nn as nn
#import torchvision.transforms as transforms
#from torchvision import models
from PIL import Image
from torchvision.models import  ResNet50_Weights
import random
import numpy as np
model_path="resnet50_30epochs_65%_tr_accuracy_57%_test_accuracy.pt"
class_names = { 'Abyssinian': 0,
                'American Bobtail': 1,
                'American Curl': 2,
                'American Shorthair': 3,
                'Applehead Siamese': 4,
                'Balinese': 5,
                'Bengal': 6,
                'Birman': 7,
                'Bombay': 8,
                'British Shorthair': 9,
                'Burmese': 10,
                'Chartreux': 11,
                'Cornish Rex': 12,
                'Devon Rex': 13,
                'Egyptian Mau': 14,
                'Exotic Shorthair': 15,
                'Extra-Toes Cat - Hemingway Polydactyl': 16,
                'Havana': 17,
                'Himalayan': 18,
                'Japanese Bobtail': 19,
                'Korat': 20,
                'Maine Coon': 21,
                'Manx': 22,
                'Munchkin': 23,
                'Nebelung': 24,
                'Norwegian Forest Cat': 25,
                'Ocicat': 26,
                'Oriental Short Hair': 27,
                'Oriental Tabby': 28,
                'Persian': 29,
                'Ragamuffin': 30,
                'Ragdoll': 31,
                'Russian Blue': 32,
                'Scottish Fold': 33,
                'Selkirk Rex': 34,
                'Siamese': 35,
                'Siberian': 36,
                'Snowshoe': 37,
                'Sphynx': 38,
                'Tonkinese': 39,
                'Toyger tiger cat': 40,
                'Turkish Angora': 41}
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


