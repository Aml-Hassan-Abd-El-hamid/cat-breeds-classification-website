# Cat breeds classification website

The idea of this application is to classify the cat images that the user uploads and give the user the cat's breed.

I divided this project into 3 main stages:

- The dataset.<br>
- Modeling.<br>
- Building the website.<br>

## The dataset

I first started by using  this <a href="https://www.kaggle.com/datasets/denispotapov/cat-breeds-dataset-cleared">dataset </a> on Kaggle But the dataset was really dirty, and there were a lot of problems with that dataset:
- A lot of pictures were wrong, I even found bunny pictures instead of cat pictures in the Havana class folder! 
- The folders:  "Tortoiseshell", "Tabby", "Torbie", "Dilute Tortoiseshell", "Calico",  "Tuxedo",  "Silver", "Domestic Short Hair", "Domestic Medium Hair" and "Domestic Long Hair" aren't really cat breeds, that kind of cats have a blended ancestry and that's why they could be really confusing to any model to recognize them, and the "Domestic Short Hair" folder got about 49,900 images alone - the dataset has about 118,000 images in total - so it created a highly imbalanced dataset.
- There were a number of classes with very few images in them,  some folders got only 4 images!

So I started building a better dataset. <br>
I used 3 different cat breed datasets to construct this dataset along with Google images.<br>
I used all the classes from the Gano Cat Breed Image Collection except for the "Tuxedo" which isn't technically a breed, that was 14 classes. <br>
I used the Scottish fold class from the Cat Breed dataset. <br>
The rest of the 27 classes came from the Cat Breeds Dataset (Cleared), those 27 classes contained a lot of bad images - misclassified and low quality - and I cleaned them as much as I could manually, also I collected more data for the Selkirk Rex, Korat, and Chartreux classes from Google images to make them at least 100 images.<br>
After that I split the dataset into train and test, the test folders contain about 25% of the original dataset, and the train folders contain about 75% of the dataset.

You can find the new dataset on that repo: https://github.com/Aml-Hassan-Abd-El-hamid/datasets

Even after Building a new dataset dealing with this task was extremly hard for the follwing reasons:

- The cat isn't always the only thing in the image or even the center of it and the lighting and the quilty vary from one image to anther one.<br> 

- There's a huge variation inside the class, you can see for example those pictures that come from the "Abyssinian" class:

<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/Abyssinian_109.jpg" width="140" height="140" ><img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/Abyssinian_110.jpg" width="140" height="140" ><img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/Abyssinian_113.jpg" width="140" height="140" ><img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/Abyssinian_112.jpg" width="140" height="140" ><img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/Abyssinian_118.jpg" width="140" height="140" >

- There are a lot of similer cat breeds that are really hard to differentiate from each others:

for example, the image on the left is from the "Siamese" class and the one in the right is from "Burmese" class:<br>
<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/Siamese_207.jpg" width="140" height="140" ><img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/29875697_665.jpg" width="140" height="140" > 

anther example, the image on the left is from the "Bengal" class and the one in the right is from "Egyptian Mau" class:<br>
<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/Bengal_119.jpg" width="140" height="140" ><img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/Egyptian_Mau-19074223_1010.jpg" width="140" height="140" > 

## Modling

I used Transfer learning to help with modeling this dataset, that was my first time using transfer learning and those 2 tutorials were really useful:<br>
https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html <br>
https://www.learnpytorch.io/06_pytorch_transfer_learning/ <br>
<br>I started by using smaller networks and I was freezing the feature extractor layers and only put the fully connected layer into training: ResNet18 it didn't give me a good performance, I trained it with almost 50 epochs and the best accuracy that I manage to get was 51% training and 25% testing, I made an assumption that given the complexity of the images and the variation inside the classes, I need to use a more complex network, and I tried ResNet50, it gives me 70% training accuracy and 20% validation accuracy which was so bad overfitting. For my last network -last for now :) - I changed my technique a little bit and stopped freezing the feature extractor part, I still initialized the network as pre-trained but instead of only modifying the fully connected layer, I was modifying the whole network, I used ResNet34 architecture, trained it with a decaying learning rate for 15 epochs and got 65% training accuracy and 51% testing accuracy.<br>

## Building the website

As someone who has never dealt with backend or machine learning deployment before this project, I wanted this project to be a gentle and nice start for me, I used Flask for the backend and Bootstrap 5 for the front-end, I found a couple of good tutorials that I would like to share: <br>
https://towardsdatascience.com/build-a-web-application-for-predicting-apple-leaf-diseases-using-pytorch-and-flask-413f9fa9276a <br>
https://www.w3schools.com/bootstrap5/


## Preview : 






https://user-images.githubusercontent.com/66205928/223043414-f518582c-b21b-47f0-a500-3c9c03e67ae4.mp4


### To do next:

1 - upgrade the preformance:
- Try to clean the data more.  ✅
- Gather more data fro the classes with less images.✅
- Try different modells: 
a - Transformers?
b - Try creating 2 different models: one to detect the cat in the image and the other to classify it.

2 - upgrade the website:
- Add a database to provide info about the cat in interest
