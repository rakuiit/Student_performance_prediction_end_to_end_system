import sys
import os
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")



class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
         This fucntion is doing data transformation for cat and num variable 
        '''
        try:
            numerical_features =['reading_score', 'writing_score']
            categorical_features = ['gender', 'race_ethnicity', 'parental_level_of_education', 
                                    'lunch', 'test_preparation_course']
            
            ## make numerical pipeline 
            num_pipeline=Pipeline(steps=
                                  [("imputer",SimpleImputer(strategy='median')),
                                   ("scaler",StandardScaler())
                                   ]
                                   )
            cat_pipeline=Pipeline(steps=
                                  [("imputer",SimpleImputer(strategy='most_frequent')),
                                   ("one_hot_encoder",OneHotEncoder())
                                  ])
            logging.info("num and cat variable standard scaling completed")

            ### apply on data frame

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_features),
                    ("cat_pipeline",cat_pipeline,categorical_features)

                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(sys,e)
        

    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            print(train_df.head())
            print(test_df.head())
            
            logging.info("Read train and test data completed")

            target_column_name="math_score"

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            
            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("applying preprocessing object on training and testing dataframe")

            preprocessing_obj=self.get_data_transformer_object()
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)


            train_arr=np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr=np.c_[input_feature_test_arr,np.array(target_feature_test_df)]

            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,
                        obj=preprocessing_obj)

            return (train_arr,
                    test_arr,
                    self.data_transformation_config.preprocessor_obj_file_path)
                    

        except Exception as e:
            raise CustomException(e,sys)






