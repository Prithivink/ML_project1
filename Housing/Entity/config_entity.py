from collections import namedtuple


#contains all the information where the data is located
dataingestionconfig = namedtuple("dataingestionconfig",
["download_URL",
"zip_data_dir",
"raw_data_dir",
"train_data_folder",
"test_data_folder"])


#contains all the information where the scheme of data(no of row and columns, datatypes etc..) is located
datavalidationconfig = namedtuple("datavalidationconfig","SchemeFilepath")


#contains all the information where the data with respect to transformed data(pickle files etc..) are loacated
dataTransformationconfig = namedtuple("dataTransformationconfig",["add_bedroom",
"transformedTraindata","transformedTestData","preprocessed_file_path"])


#contains all the information where the data with respect to model(pickle files etc..) are loacated
#base accuracy is the min expectation from our side, below which we reject the trained model
moodelTrainerconfig = namedtuple("moodelTrainerconfig",["trainedmodel_file_path","base_accuracy"])


#contains all info about the production models to compare with the new test models
modelEvaluationconfig = namedtuple("modelEvaluationconfig",["model_evaluation_file_path","time_stamp"])

#contains all info about the production models to compare with the new test models
modelPusherconfig = namedtuple("modelPusherconfig",["export_dir_path"])

