**PNEUMONIA DETECTION**

**AIM:** Detect the pneumonia using the CNN based detectors from Chest X-Ray images.

![image](https://user-images.githubusercontent.com/38240162/87241592-ab486c00-c41c-11ea-86d9-8dea1dcb0b55.png)

**TECHNOLOGY STACK USED:** Python, Deep Learning: CNN, LeNet5, VGG16

**IDE:** Jupyter Notebook

**TASKS:**

1. Load the chest x-ray dataset and become familiar with its contents. 

![image](https://user-images.githubusercontent.com/38240162/87242256-e64d9e00-c422-11ea-9dc2-e165f3c4edf0.png)

2. As a simple baseline train a logistic regression model to perform the classification task.
    Note: You will need to convert images into a vector representation to allow this. We suggest converting the images to greyscale and resizing them (perhaps to 162*128).

3. Train a convolutional neural network model to recognise pneumonia in these images.

![image](https://user-images.githubusercontent.com/38240162/87241701-aa640a00-c41d-11ea-90b8-a7878e0d4699.png)

    Note: Consider the following:
    
    • Try the classic LeNet-5 model architecture.
    
    • Consider converting the images to greyscale.
    
    • Consider shrinking the images (perhaps to 162*128).
    
    • Perform a suitable evaluation experiment to determine how effective the model trained is.
    
    • Consider using approaches to handle the class imbalance in the dataset.

4. Use data augmentation techniques (for example image rotations or slight colour changes) to increase the size of the training dataset. Use the augmented dataset to train a model with the same model architecture that you used earlier.    
    Note: Select the transformations carefully (for example flipping images horizontally or vertically is not appropriate as x-ray images have a fixed frame of reference).

![image](https://user-images.githubusercontent.com/38240162/87242043-02504000-c421-11ea-9a8a-c63700907957.png)


5. Change your model so that it uses a pre-trained VGG16 model (trained on the ImageNet dataset) that is fine tuned to the pneumonia detection problem.  
    Note: Consider unfreezing one of the convoluito0onal layers in the network as well as the dense layers.
    
 ![image](https://user-images.githubusercontent.com/38240162/87242180-51e33b80-c422-11ea-9181-e9f4de497ac6.png)
    
    
**CONCLUSION:**    

![image](https://user-images.githubusercontent.com/38240162/87241639-05493180-c41d-11ea-8bbf-54f3ad1a88e3.png)

    
![image](https://user-images.githubusercontent.com/38240162/87241650-1d20b580-c41d-11ea-9d4b-11751ce3db96.png)

**1. Logistic Regression:**

    1. As a base model, we used Logistic Regression model to determine whether or not a given X-ray has pneumonia or not. It is relatively an easy model to implement as we treat each pixel as distinct feature.

    2. We have also converted the images to grayscale as color images have 3 channels which increases the model complexity (Number of features) and doesn't improve the predictive power. Also the images were reshaped to the desired size of (162, 128).

    3. The Logistic Regression classifier gives 100% accuracy on training data set while it could only give 81.45% on the testing dataset. Since the dataset is highly imbalanced and majority class is of pnueumonia we are getting higher accuracy. The model got overfitted.
    
![image](https://user-images.githubusercontent.com/38240162/87241686-8274a680-c41d-11ea-9a3e-eadc67165998.png)

    
**2. LeNet5 CNN:**

    a. LeNet-5 is one of the simplest architectures. It has 2 convolutional and 3 fully-connected layers.
    b. We selected 'adam' as the optimizer with learning rate of 0.0001. The sub-sampling layer used is average-pooling with trainable weights.
    
    Unbalanced Dataset:😢
        1. Initially we trained the model on the unbalanced dataset. The model has an accuracy of 95.02% on training data set and 74.19% on testing dataset.
        2. Even though the overall accuracy is lower than that of the Logistic Regression, it was capable of classifying the patients more accurately based on their chest X-ray images. True Negatives are also clearly visible through the confusion matrix to a certain extent.

    Balanced Dataset:😀
        1. The class_weights are set to 'balanced' in order to sample the data. Here, the model accuracy decreases to 64% in case of test dataset. This was an unsual behaviour, because mostly after balancing the dataset we should intuitively get more accurates results due to low bias.
        2. This model performed well in comparison to Logistic Regression model but not as good as LeNet 5 model which when trained on unbalanced dataset. However there was a significant difference of 10% in accuracy in terms of performance on test dataset.

![image](https://user-images.githubusercontent.com/38240162/87241710-ba7be980-c41d-11ea-83f2-f240bde4b6ca.png)

    
    
**3. LeNet5 Data Augmentation:**

    1. This model performs best in terms of accuracy when tested on test dataset. The target classes are clearly distinguished, clearly visible from Confusion Matrix.
    2. In order to increase the size of the training dataset, number of Augmentation transformations are applied on the dataset.
    3. The ModelCheckpoints helped us to save the model by monitoring a specific parameter (val_loss, accuracy) of the model.
    4. Initially the model was converging to a certain value (74.29). But after introducing the learning rate and dense layer, the accuracy got boosted. The following transformations have been applied on the dataset.
        a. Rotation: A rotation augmentation randomly rotates the image clockwise by a given number of degrees(15).
        b. Width shift: Moving pixel horizontally while keeping the image dimension same.
        c. Height shift: Moving pixel vertically while keeping the image dimension same.
        d. Zoom: A zoom augmentation randomly zooms the image in and either adds new pixel values around the image or interpolates pixel values respectively.
        e. Fill mode: Points outside the boundaries of the input are filled according to the given mode.
    5. We even tried with Brightness but it degraded the accuracy badly, as X-ray images are very sensitive to saturation level.
    6. The overall accuracy on the training dataset comes out to be 85.52% and 76.61% on testing data with Augmented data.
    7. The most useful thing about ImageDatagenerator class is i,t doesn’t affect the data stored on the disk. It simply alters the data on the go while passing it to the model.
    8. Data augumentation enhances the training of CNN model. The model gets multiple variant of a single training data due to which it learns the main features. Networks trained with just data augmentation more easily adapt to different architectures and amount of training data, as opposed to weight decay and dropout, which require specific fine-tuning of their hyperparameters.

![image](https://user-images.githubusercontent.com/38240162/87242055-1c8a1e00-c421-11ea-88b6-2d1caa211bf5.png)

**4. VGG-16**

    1. The most unique aspect about VGG16 is that instead of making a huge number of hyper-parameters, it concentrated on providing 3x3 convolution layers with a stride 1 filter and only using the same padding and maxpool layer with a 2x2 stride 2 filter.
    2. Since we have less data available with us to train the model, we used VGG as a transfer learning platform. This allow us to just add the final fully connected layers and test the model on the testing data.
    3. Here, We achieved the accuracy of 72.58% on testing and 98.89% on training dataset. The model was capable of finding few of True Negatives as well.
    4. VGG has very high memory consumption and takes maximum time to train the model but since we are only using the last few layers of VGG16, It proves to be less computationally expensive.

![image](https://user-images.githubusercontent.com/38240162/87242194-658ea200-c422-11ea-8d2c-cdb2116db195.png)


[Click here for the Code](https://github.com/ktyagi12/Projects/new/master/PneumoniaDetection/code)

[Click here for the Input](https://github.com/ktyagi12/Projects/new/master/PneumoniaDetection/input)

[Click here for the Output](https://github.com/ktyagi12/Projects/new/master/PneumoniaDetection/output)


**REFERENCES**

[1] Cs229.stanford.edu. 2020. [online] Available at: http://cs229.stanford.edu/proj2017/final-reports/5231221.pdf [Accessed 1 May 2020].

[2] Ieeexplore.ieee.org. 2020. Pneumonia Detection Using CNN Based Feature Extraction - IEEE Conference Publication. [online] Available at: https://ieeexplore.ieee.org/document/8869364 [Accessed 1 May 2020].
