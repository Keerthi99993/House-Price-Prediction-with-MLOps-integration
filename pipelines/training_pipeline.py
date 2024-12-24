from steps.data_splitter_step import data_splitter_step
from steps.model_building_step import model_building_step
from steps.model_evaluator_step import model_evaluator_step
from steps.outlier_detection_step import outlier_detection_step
from steps.data_ingestion_step import data_ingestion_step
from steps.handle_missing_values_step import handle_missing_values_step
from steps.feature_engineering_step import feature_engineering_step
from zenml import Model,pipeline,step


@pipeline(
    model=Model(
        #the name uniquely identifies this model
        name="prices_predictor"
    ),
)

def ml_pipeline():
    '''define an end to end machine learning pipeline'''

    #data ingestion step
    raw_data=data_ingestion_step(
        file_path="C:/Users/Keerthi/Documents/AiMlasingh/data/archive.zip"
    )

    #handling missing values step
    filled_data=handle_missing_values_step(raw_data)

    #feature engineering step
    engineered_data=feature_engineering_step(
    filled_data,strategy="log",features=["Gr Liv Area", "SalePrice"]
    )

    #outlier detection step
    clean_data=outlier_detection_step(engineered_data,column_name="SalePrice")

    #Data splitting step
    X_train,X_test,y_train,y_test=data_splitter_step(clean_data, target_column="SalePrice")

    #model building step
    model=model_building_step(X_train=X_train,y_train=y_train)

    #model evaluation step
    evaluation_metrics,mse=model_evaluator_step(
        trained_model=model,X_test=X_test,y_test=y_test
    )
    return model


if __name__=="__main__":
    #running the pipeline
    run=ml_pipeline()