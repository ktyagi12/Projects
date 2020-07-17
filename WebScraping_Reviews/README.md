**WEB SCRAPING REVIEWS: Data Science with Python**

**TECHNOLOGY USED:** Python

**IDE:** Jupyter Notebook

**AIM:** Scrape consumer reviews from a set of web pages and to evaluate the performance of text classification algorithms on the data. Each review has a star rating. For this assignment, we will assume that 1-star to 3-star reviews are “negative”, and 4-star to 5-star reviews are “positive”.

**TASKS:**

1. Select three review categories of your choice. Scrape all reviews for each category and store them as three separate datasets. For each review, there is a review text and a class label (i.e. “positive” or “negative”).
2. For each of the three category datasets:
  
    a. From the reviews in this category, apply preprocessing steps to create a numeric representation of the data, suitable for classification. A various number of pre-processing steps are performed on the reviews data so that they can take a form easily used to build the model. Steps are as follows:
        
        1. Data Normalisation
        2. Lemmatization
        3. Stop Word removal
        4. TF-IDF Vectorisation
  
    Data cleaning and transformation are methods used to remove outliers and standardize the data so that they take a form that can be easily used to create a model.
  
    ![image](https://user-images.githubusercontent.com/38240162/87516403-3de34800-c675-11ea-8c20-53deda514d5e.png)

    b. Build a classification model to distinguish between “positive” and “negative” reviews using one of the following classifiers:
        
        Naive Bayes, Logistic Regression, Random Forests
  
    c. Test the predictions of the classification model using an appropriate evaluation strategy.
  
3. Evaluate the performance of each of the three classification models when applied to data from the other two selected categories:
  
    a. Train a classification model on the data from “Category A”. Evaluate its performance on data from “Category B” and “Category C”.
    
    ![image](https://user-images.githubusercontent.com/38240162/87516544-7e42c600-c675-11ea-9489-0647ba84e715.png)
  
    b. Train a classification model on the data from “Category B”. Evaluate its performance on data from “Category A” and “Category C”.
  
    ![image](https://user-images.githubusercontent.com/38240162/87516594-8f8bd280-c675-11ea-8d7e-dd10eb97c900.png)

    c. Train a classification model on the data from “Category C”. Evaluate its performance on data from “Category A” and “Category B”.
    
    ![image](https://user-images.githubusercontent.com/38240162/87516657-a4686600-c675-11ea-9320-57cbbfbe3112.png)


**CONCLUSION**

- Large amount of reviews from Fashion, Gyms and Hair_salon are scraped with the help of BeautifulSoup.
- Initially, all the main links are fetched using the fetch_all functionality of the scraper and out of which the 3 selected category links are stored in a list for further reference.
- For every main category, requests.get() function fetches the links through 'a' tag. Further contents of href tags are fetched.
- Further for every category, all the contents are scraped using the BeautifulSoup() and reviews are extracted from it using the 'p' tags.
- Based on the number of ratings, target class is decided for every review and every review along with its target class is saved in a comma separated file.
- Further a number of pre-processing steps are performed over text reviews:
      
      1. Data Normalization in order to transform the text into a single canonical form.
      2. Lemmatization in order to group the various inflected terms together so as to analyse them as a single term considering the context.
      3. Stopwords removal so as to provide more importance to the actual words instead of low meaning conveying terms.
      4. Term Frequency Inverse Document Vectorisation.

 - Following which Logistic Regression model is built for every category (Fashion, Gyms, Hair_Salon) and evaluating the performance of each category through Confusion matrix and depicting the misclassified reviews.
 - Next, Training the model with every category acting as training dataset and testing its performance over other two categories is evaluated.
 - Accuracy while model trained on Fashion dataset and Gyms dataset and testing on Gyms and Hair_Salon dataset comes to be the maximum counting to approximately 87 % and 92.5 %.
 - Logistic Regression classification model proves to be most efficient among the three classification models.
 - The performance of every model is evaluated using a number of techniques:

      1. Confusion Matrix
      2. K Fold Cross Validation
      3. Repeated Fold Cross Validation
      4. Misclassifications

[Click here for the Workbook](https://github.com/ktyagi12/Projects/tree/master/WebScraping_Reviews/code)

[Click here for the Input](https://github.com/ktyagi12/Projects/tree/master/WebScraping_Reviews/input)
