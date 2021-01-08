# Machine Learning and Statistics Project

This repository contains my code for the Machine Learning ans Statistics project, the instructions for which can be found [here](https://learnonline.gmit.ie/mod/url/view.php?id=104063). 

## Contents of Repository
 - Jupyter Notebook containing examination of dataset, split dataset for for training, and training of model in keras.
 - CSV containing the data examined in Jupyter Notebook.
 - Machine Learning model named "model.h5" exported from Jupyter Notebook.
 - Flask server named "server.py" which contains function for making predictions based on input and routes for web server.
 - Templates folder containing index.html, a front end for the web server.
 - Dockerfile, .dockerignore, and requirements.txt required for creating Docker Container.
 
 ## How to Run App from Docker Container
 - Clone this repository by running the following command on your command line.\
 ``` git clone https://github.com/ANihill/MLProject.git```
 - Navigate to repository.\
 ```cd MLProject```
 - Run the follwoing commands.\
 ```docker build . -t predict-image```\
 ```docker run --name predict-container -d -p 5000:5000 predict-image```
 
 ### Potential Issues
 Dockerfile contains the following code in the first line.\
 ```FROM python:3.8```\
 Python version was set to 3.8 as it would not build the container on my machine, as it was unable to find tensorflow with python set to 3.
