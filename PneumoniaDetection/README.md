**PNEUMONIA DETECTION: Deep Learning: CNN**

**TECHNOLOGY USED:** Python, CNN, LeNet5, VGG16

**IDE:** Jupyter Notebook

**AIM:** Detect the pneumonia using the CNN based detectors from Chest X-Ray images. 

**TASKS:**

1. Load the chest x-ray dataset and become familiar with its contents. 
2. As a simple baseline train a logistic regression model to perform the classification task.
    Note: You will need to convert images into a vector representation to allow this. We suggest converting the images to greyscale and resizing them (perhaps to 162*128).
3. Train a convolutional neural network model to recognise pneumonia in these images.
    Note: Consider the following:
    • Try the classic LeNet-5 model architecture.
    • Consider converting the images to greyscale.
    • Consider shrinking the images (perhaps to 162*128).
    • Perform a suitable evaluation experiment to determine how effective the model trained is.
    • Consider using approaches to handle the class imbalance in the dataset.
4. Use data augmentation techniques (for example image rotations or slight colour changes) to increase the size of the training dataset. Use the augmented dataset to train a model with the same model architecture that you used in Part
    Note: Select the transformations carefully (for example flipping images horizontally or vertically is not appropriate as x-ray images have a fixed frame of reference).
5. Change your model so that it uses a pre-trained VGG16 model (trained on the ImageNet dataset) that is fine tuned to the pneumonia detection problem.
    Note: Consider unfreezing one of the convoluito0onal layers in the network as well as the dense layers.

[Click here for the Code](https://github.com/ktyagi12/Projects/new/master/PneumoniaDetection/code)

[Click here for the Input](https://github.com/ktyagi12/Projects/new/master/PneumoniaDetection/input)

[Click here for the Output](https://github.com/ktyagi12/Projects/new/master/PneumoniaDetection/output)
