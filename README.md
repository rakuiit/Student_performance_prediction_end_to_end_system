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

Link : [EDA Notebook](./src/components/data_ingestion.py)







### Data Transformation


### Model Training Component



### Model Evaluating Component



### Create Prediction Pipeline Using Flask Web APP



### Deploy in Production on AWS Cloud Using Docker,CI CD Pipeline


### AWS Deployment Link :


### Screenshot of UI