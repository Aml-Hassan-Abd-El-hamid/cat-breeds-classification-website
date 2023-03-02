# Cat breeds classification website

My first attempet to deploy a machine learning model!
The idea of this applicatin is to classify the flower images that the user upload and give the user some info about that flower.

I divided this project into 5 steps:

- Chosing The dataset.<br>
- Training the model.<br>
- deploy the model with Flask.<br>
- Design and Front-end of the application.<br>

### The dataset: 

I used this <a href="https://www.kaggle.com/datasets/denispotapov/cat-breeds-dataset-cleared">dataset </a> on kaggle which is a cleaner version of this <a href="https://www.kaggle.com/datasets/ma7555/cat-breeds-dataset" >dataset</a> **huge thank you for @denred0for his work**, The dataset contains 67 different cat breeds, and even after the cleaning that was done, the dataset still challenging for the follwing reasons: 

- the cat isn't always the only thing in the image or even the center of it.<br> 
- there's a huge variation inside the calss, you can see for example those pictures that comes from the "devon rex" class:

