from dataclasses import dataclass

#contains the outputs of the different stages of the pipeline
@dataclass
class DataIngestionArtifact:
    trained_file_path:str
    test_file_path:str

# Stores validation results
@dataclass
class DataValidationArtifact:
    validation_status: bool
    valid_train_file_path: str
    valid_test_file_path: str
    invalid_train_file_path: str
    invalid_test_file_path: str
    drift_report_file_path: str

#Contains paths to transformed datasets
@dataclass
class DataTransformationArtifact:
    transformed_object_file_path: str
    transformed_train_file_path: str
    transformed_test_file_path: str

@dataclass
class ClassificationMetricArtifact:
    f1_score: float
    precision_score: float
    recall_score: float

#Stores trained model file paths & performance metrics.   
@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
    train_metric_artifact: ClassificationMetricArtifact #the above class is referred here so train metric will have all details
    test_metric_artifact: ClassificationMetricArtifact
