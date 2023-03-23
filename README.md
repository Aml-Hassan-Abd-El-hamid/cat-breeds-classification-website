# Cat breeds classification website

My first attempt to deploy a machine-learning model!<br> So I will really appreciate your feedback on the discussion section.

The idea of this application is to classify the cat images that the user uploads and give the user the cat's breed.

I divided this project into 3 main stages:

- Handling The dataset.<br>
- Modeling.<br>
- Building the website.<br>

## The dataset

I used this <a href="https://www.kaggle.com/datasets/denispotapov/cat-breeds-dataset-cleared">dataset </a> on Kaggle which is a cleaner version of this <a href="https://www.kaggle.com/datasets/ma7555/cat-breeds-dataset" >dataset</a> ,**huge thank you for @denred0 for his work**, The dataset contains 67 different cat breeds, and even after the cleaning that was done, the dataset still challenging for the following reasons: 

- the cat isn't always the only thing in the image or even the center of it.<br> 

- there's a huge variation inside the class, you can see for example those pictures that come from the "devon rex" class:

<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/184devon%20rex328.jpg" width="140" height="140" ><img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/21devon%20rex6.jpg" width="140" height="140" >
<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/2devon%20rex2.jpg" width="140" height="140" >
<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/devon%20rex15.jpg" width="140" height="140" >
<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/devon%20rex29.jpg" width="140" height="140" >

- Some classes have very few images, for example, the "York Chocolate" cat got only one image and the "Chinchilla" cat got 2 images, So I collected extra images for those classes from the web.

- The 3 folders: "Domestic Short Hair", "Domestic Medium Hair" and "Domestic Long Hair" aren't really cat breeds, that kinds of cats have a blended ancestry and that's why they could be really confusing to any model to recognize them, and the "Domestic Short Hair" folder got about 49,900 images alone - the dataset has about 118,000 images in total - so it created a highly imbalanced dataset, I dealt with that problem by removing those classes from the dataset.

- The folder "Canadian Hairless" contained only 4 images and non of them were hairless! was really suspicious so after failing to find any websites that talk about "Canadian Hairless", I also used google lense to look up those images and was
able to get nothing useful so given that fact + the fact that I wasn't able to collect any more images of the "Canadian Hairless" I decided to ignore that class for now.

- Also I found that "Tortoiseshell", "Tabby",  "Torbie", "Dilute Tortoiseshell", "Calico", and "Tuxedo".  are not really breeds according to those articles:<br> https://petventuresbook.com/blogs/blog/differences-between-tabby-torbie-and-tortoise-shell-cats <br> https://betterwithcats.net/dilute-tortoiseshell-cat/ <br> https://www.ivankhristravels.com/2021/11/dilute-calico-cats.html <br> https://www.cattownoakland.org/cat-town-blog/2021/04/calico-cat-facts-to-know <br> https://rawznaturalpetfood.com/tuxedo-cats/. So I ignored those classes.

- Also according to my search there's no breed that's called "Silver", So I ignored this class.

- The class that was named: "Tiger" in the folders doesn't really contain tiger images instead it contains images of a breed that's called "Toyger", so I renamed this folder to "Toyger tiger cat" to remove the confusion.

**In the end, I was left with a total of 37,234 images in the dataset and 55 cat breeds, instead of 118,775 images and 67 cat breeds.**

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
- Try to clean the data more.
- Gather more data fro the classes with less images.
- Try different modells: 
a - Transformers?
b - Try creating 2 different models: one to detect the cat in the image and the other to classify it.

2 - upgrade the website:
- Add a database to provide info about the cat in interest
