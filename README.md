# Cat breeds classification website

My first attempet to deploy a machine learning model!
The idea of this applicatin is to classify the flower images that the user upload and give the user some info about that flower.

I divided this project into 5 steps:

- Chosing The dataset.<br>
- Training the model.<br>
- deploy the model with Flask.<br>
- Design and Front-end of the application.<br>

### The dataset: 

I used this <a href="https://www.kaggle.com/datasets/denispotapov/cat-breeds-dataset-cleared">dataset </a> on kaggle which is a cleaner version of this <a href="https://www.kaggle.com/datasets/ma7555/cat-breeds-dataset" >dataset</a> ,**huge thank you for @denred0 for his work**, The dataset contains 67 different cat breeds, and even after the cleaning that was done, the dataset still challenging for the follwing reasons: 

- the cat isn't always the only thing in the image or even the center of it.<br> 
- there's a huge variation inside the calss, you can see for example those pictures that comes from the "devon rex" class:

<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/184devon%20rex328.jpg" width="140" height="140" ><img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/21devon%20rex6.jpg" width="140" height="140" >
<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/2devon%20rex2.jpg" width="140" height="140" >
<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/devon%20rex15.jpg" width="140" height="140" >
<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/devon%20rex29.jpg" width="140" height="140" >

- Some classes have very few images, for example: "York Choclete" cat got only one image and "Chinchilla" cat got 2 images, So I collected extra images for those classes from the web.
- The 3 folders: "Domestic Short Hair", "Domestic Medium Hair" and "Domestic Long Hair" aren't really cat breeds, that kinds of cats have a blended ancestry and that's why they could be really confusing to any model to recognize them, and the "Domestic Short Hair" folder got about 49,900 images alone - the dataset has about 118,000 images in total - so it created a highly imbalanced dataset, I dealt with that problem by removing those classes from the dataset. 
- The folder "Canadian Hairless" contained only 4 images and non of them were hairless! was really suspicious so after failing to find any websites that talk about "Canadian Hairless", I used google lense to look up those images one of the images -which is shown bellow - was so close to the Calico cat breed so given that fact + the fact that I wasn't able to collect any more images of the "Canadian Hairless" I decided to ignore that class. 
<img src="https://github.com/Aml-Hassan-Abd-El-hamid/cat-breeds-classification-website/blob/main/readme_images/34851962_6.jpg" width="140" height="140" >

- Also I found that "Tortoiseshell", "Tabby",  "Torbie" , "Dilute Tortoiseshell", "Calico", "Tuxedo".  are not really breeds accourding to those articles: https://petventuresbook.com/blogs/blog/differences-between-tabby-torbie-and-tortoise-shell-cats , https://betterwithcats.net/dilute-tortoiseshell-cat/ , https://www.ivankhristravels.com/2021/11/dilute-calico-cats.html , https://www.cattownoakland.org/cat-town-blog/2021/04/calico-cat-facts-to-know , https://rawznaturalpetfood.com/tuxedo-cats/. So I ignored those classes.

- Also accourding to my search there's no breed that's called "Silver", So I ignored this class.

- The class that was named : "Tiger" in the folders doesn't really contains tigers images insted it contains images of a breed that's called "Toyger", so I renamed this folder to be "Toyger tiger cat" to remove the confusion.

