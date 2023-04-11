import joblib

def predict(data, model):
    if model == 'Support Vector Machine':
        model = joblib.load('model_svm.pkl')
        pipeline = joblib.load('pipeline_svm.pkl')
    elif model == 'Random Forest Classifier':
        model = joblib.load('model_rf.pkl')
        pipeline = joblib.load('pipeline_trees.pkl')
    elif model == 'Extra Trees Classifier':
        model = joblib.load('model_et.pkl')
        pipeline = joblib.load('pipeline_trees.pkl')

    data = pipeline.transform(data)
    return model.predict(data)