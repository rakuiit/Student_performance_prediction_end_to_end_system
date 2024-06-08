# Student performance Prediction End to END project 

##### Main purpose of this project to showcase End to End machine learning deployment.For that i used python,flask,docker,aws etc


## Approache for Project:

### Github And Code Set Up
    -Setup github repo 
    -Create env 
          conda create -p venv python==3.8 -y
          conda activate venv/


### Project Structure, Logging And Exception Handling:



### Project Problem Statement 

- This project understands how the student's performance (test scores) is affected by other       variables such as Gender, Ethnicity, Parental level of education, Lunch and Test preparation course.
    
- Dataset Source :
[https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977)

- The data consists of 8 column and 1000 rows.



### Data collection and Exploratory Data Analysis

#### Steps
1. Data collection
2. Variable Identification 
3. Bi-variate Analysis
4. Missing values treatment
5. Outlier treatment
6. Variable transformation
7. Variable creation

Link : [EDA Notebook](./notebook/Basic_EDA.ipynb)


### Data Ingestion

#### steps
1. Reading Data
2. Preparing Data
3. Storing Data

Link : [Data Ingestion](./src/components/data_ingestion.py)


### Data Transformation

The purpose of pipeline automate the preprocessing of raw data into a format that is ready for machine learning. This includes handling missing values, scaling numerical data, and encoding categorical data. By saving the preprocessing pipeline, it ensures consistency in how data is transformed during both training and inference phases of the machine learning lifecycle.

Link : [Data Transformation](./src/components/data_transformation.py)


### Model Training Component

The purpose of this module is to automate the process of training and evaluating multiple regression models to identify the best one. It involves splitting the data, training various models, evaluating their performance, selecting the best model, and saving it for future use. The process ensures that the chosen model is the most suitable for the given data based on its performance metrics.

Link : [Model Training](./src/components/model_trainer.py)


### Create Prediction Pipeline Using Flask Web APP

The purpose of this module is to create a web interface for users to input data, process the data through a machine learning pipeline, and display the prediction results. The application allows users to interact with the machine learning model through a web browser, making it accessible and user-friendly.

Link : [Flask Web Code](./app.py)


### Deploy in Production on AWS Cloud Using Docker,CI CD Pipeline


### AWS Deployment Link :


### Screenshot of UI