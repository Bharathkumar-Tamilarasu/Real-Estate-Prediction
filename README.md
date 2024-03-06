# **RealEstate Valuation System**

![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![Google Colab](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c.svg?style=for-the-badge&logo=plotly&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-7db0bc.svg?style=for-the-badge&logo=pypi&logoColor=white)
![Regex](https://img.shields.io/badge/Regex-64029a.svg?style=for-the-badge&logo=python&logoColor=white)

**Author**: Bharathkumar Tamilarasu <br />
**Email**: bharathkumar.t.17@gmail.com <br />
**Website**: https://bharathkumart17.wixsite.com/portfolio <br />
**LinkedIn**: https://www.linkedin.com/in/bharathkumar-tamilarasu-218429222/  <br />

##

![Valuation Pic 2](https://github.com/Bharathkumar-Tamilarasu/RealEstate-Valuation-System/blob/main/Valuation%20Pic%202.jpg)

# **Table of Contents**
  
- Introduction
- Objective
- Data Collection
- About the Dataset
- Python libraries used
- Project Work flow
  1. Data Exploration
  2. Data Wrangling
  3. Feature Engineering
  4. Outliers Removal
  5. Model Building
  6. Prediction
- Limitations
- Conclusion

## **Introduction**

* In the world of real estate, accurately valuing properties is crucial for smart decision-making by buyers, sellers, and investors. 
* This project, the "Real Estate Valuation System," uses machine learning and Python to predict house prices in Bangalore. 
* Our goal is to create a strong model considering key factors like the number of bathrooms, bedrooms (BHKs), square footage, and location.
* Using a dataset of past real estate transactions, our machine learning model learns patterns to make accurate house price predictions.
* Bangalore, known for its vibrant culture and rapid growth, is our focus. Its real estate market is diverse, reflecting many factors affecting property values.
* We apply advanced algorithms and techniques to capture these details, providing a tool for stakeholders to estimate property values accurately.

## **Objective** 

* The primary objective of the Real Estate Valuation System is to develop a robust and efficient machine learning model using Python, capable of predicting house prices in Bangalore.

## **Data Collection**

The data for this project was collected from Kaggle, a popular platform for data science competitions and datasets.

* Check out the dataset [here](https://github.com/Bharathkumar-Tamilarasu/RealEstate-Valuation-System/blob/main/bengaluru_house_prices.csv)

## **About the Dataset**

### Dataset Information:

* The dataset contains details about real estate properties in Bangalore, India. 
* It provides a comprehensive view of each property, encompassing attributes related to type, availability, location, size, amenities, and pricing.
* Including a variety of property types such as apartments, houses, and plots, the dataset offers insights into the diverse real estate landscape in Bangalore.
* This dataset serves as a valuable resource for analyzing and predicting property prices based on key factors.
* It is beneficial for both buyers and sellers, offering valuable insights into the dynamic real estate market of Bangalore.

### Attribute Information:

* Area Type: The type of area the property belongs to (e.g., Super built-up Area, Plot Area, Built-up Area).
* Availability: The status of the property's availability (e.g., Ready To Move, specific month and year).
* Location: The locality or neighborhood where the property is situated.
* Size: The size configuration of the property, specifying the number of bedrooms and BHK (e.g., 2 BHK, 4 Bedroom).
* Society: The name of the housing society or community, if applicable.
* Total Sqft: The total area of the property in square feet.
* Bath: The number of bathrooms in the property.
* Balcony: The number of balconies in the property.
* Price: The listed price of the property.

## **Libraries Used:**

Employed the following libraries for comprehensive data analysis:

* **Pandas** for versatile data manipulation.
* **NumPy** for efficient numerical operations.
* Leveraged **Scikit-Learn** for machine learning tasks and predictive modeling.
* Utilized **Matplotlib.Pyplot** and **Seaborn** for creating insightful visualizations.
* Integrated **Regex** for advanced text pattern matching.

## **Project Work flow**

**1. Data Exploration**
  - Immerse into a comprehensive exploration of the dataset, uncovering its characteristics, patterns, and potential challenges.

**2. Data Wrangling**
  - Systematically clean and preprocess the data, addressing missing values, inconsistencies, and preparing it for further analysis.

**3. Feature Engineering**
  - Creatively enhance the dataset by crafting new features or transforming existing ones to improve model performance.

**4. Outliers Removal**
  - Identify and handle outliers to ensure a more robust and accurate modeling process.

**5. Model Building**
  - Develop and train models based on the refined dataset, employing techniques that align with the project's objectives.

**6. Prediction**
  - Utilize the trained models to make predictions on new data, assessing their accuracy and reliability.


## Limitations
* Potential presence of duplicate values in the training data due to identical configurations of bathrooms, bedrooms (BHKs), and square footage for the same location.
* Exclusion of key features such as 'area_type,' 'availability,' 'society,' and 'balcony' from consideration.
* Elimination of rows with null values in 'size' and 'bath,' considering their critical importance.
* Adoption of a categorization strategy where locations with fewer than 10 data points are grouped under the label "Others," resulting in a substantial reduction in the number of categories from the initial 1287 unique locations.
* Addressing anomalies where 3 BHK houses exhibit lower prices than 2 BHK houses with similar area sizes in the same locations. While some entries were removed, complete elimination was not enforced.
* Handling outliers by setting a minimum threshold of 300 sqft per BHK.
* Removal of data points where the number of bathrooms exceeds the sum of bedrooms and 2.

## **Conclusion**

* In conclusion, this project represents a significant step forward in providing a comprehensive and reliable solution for property valuation.
* The successful development of a high-accuracy machine learning model, considering crucial features such as location, BHK, number of bathrooms, and area in sqft, establishes a solid foundation for accurate predictions.
* Throughout the project, we encountered challenges related to BHK and Price Outliers removal. Overcoming these challenges has not only strengthened the robustness of the system but also provided valuable insights for future enhancements.
* Overall, this project has not only delivered a functional Real Estate Valuation System but has also provided valuable lessons and opportunities for further innovation.
* As the real estate market continues to evolve, this system stands poised to make a meaningful impact by empowering users with accurate and transparent property valuations.

### **Ready to forecast housing prices? Click [here](https://realestate-valuation-system-fqcq.onrender.com/) to use our RealEstate Valuation System.**
### **Your time and interest in viewing my project are greatly appreciated. Thank you. 😃!**
