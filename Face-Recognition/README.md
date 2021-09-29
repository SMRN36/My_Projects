
# Face recognition system

This is a supervised machine learning model using opencv python

### Prject Flow:
* Detect whether image has face or not
* Label the training images
* Train the model and predict faces

First, we give the image and our model will detect the face in the image and return an array value of the location of the face in that image. This can be done with the help of HaarCascade file, it is an xml file which consists of features for faces. The haar classifier is used to detect some objects, these are pre trained models which are encoded in xml files. 

Then label the training images. It gives the label by extracting the names from the root folder and gives the label for that image by specifying that folder. It fetches the image path and loads the images one by one to give labels by using basename.

Then trained the model to predict the images using LBPH algorithm (Local Binary Pattern Histogram), is a face recognition algorithm which is used to detect the face, it analyzes pixels and returns the histogram values. After training the images, create a bounding box (rectangle) around the face and write the name of the person in the image. 
