# My Data Science Journey
*Author: Finnian Logan-Riley*  

This is a backup of all the different (very cool) models I have studied.

* Week 1  
    * Learning data frames and printing basic data.  
* Week 2
    * Scatter plots, filter by postcodes, set values to uppercase, filter by transactions and locate address by coordinates.
* Week 2 - Visual
    * Coordinates of sales and Greenwitch.
* Week 3 - ExtraVisual
    * Using np.linspace to create colour maps.
* Week 3 Visual Extra
   * Sorting stores by premium and non-premium, sales volume represented by size, marketing cost represented by colour, with a custom colour map.
* Week 4
    * Using linear regression (with mean squared error) with inputs 'living_space' 'size_of_property', to predict the price value.
        ```diff
        ->INPUT: 'size_of_property'
        +PREDICT (Linear regression): 'price'
        ```
* Week 4 Extend Train and testing Sep
    * Using polyfit (curvy linear regression!). 
        ```diff
        ->INPUT: 'size_of_property'
        +PREDICT (PolyFit with degree): 'price'  
        ```
* Week 4 Two Var predict  
    * Using multiple variables to predict price.
        ```diff
        ->INPUT: 'living_space'
        ->INPUT: 'size_of_property'
        +PREDICT (Linear regression): 'price'
        ```
* Week 5 KMean
    * Using clustering to find a correlation between meat spending vs premium membership.
    * No correlation found.
    * Then using confusion matrix on KMeans.
* Week 6 KMean3d 
    * Using KMean (clustering) in 3d.
* XgboostClassification
    * Using the classification ability of XGBoost and the true positive/false positive rate.
* XgboostFirst
    * Predict fish weight using XGBoost.
* XgboostModel
    * Using XGBoost to predict tip amount for taxis.