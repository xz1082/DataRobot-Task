import argparse, sys
from apiclient import discovery, sample_tools

project_id = '751162525330'
model_id = 'car evaluation'
  

def main():
    
    try:
        get_predictions()
    except:
        print('An unexpected error has occurred')

        
def model_training():
    '''
    create a new classification model
    '''
    api = get_api(sys.argv)
    
    print('Training model')
                  
    api.trainedmodels.insert(project=project_id, body={'id': model_id, 'storageDataLocation': 'carevaluation/car_data.csv', 'modelType': 'classification'}).execute()
           

def get_predictions():
    '''
    use trained model to generate new predictions
    '''
    api = get_api(sys.argv)
    
    #check if model training is completed
    model = api.trainedmodels().get(project=project_id, id=model_id).execute()
    if model.get('trainingStatus') != 'DONE':
        print('Model is still training.')
        exit()

    #read input data to make predictions                                
    with open('test.csv') as f:
        instance = f.readline().split(',')

    print('Making predictions')

    prediction = api.trainedmodels().predict(project=project_id, id=model_id, body={'input': {'csvInstance': instance}, }).execute()
                                    
    label = prediction.get('outputLabel')
    stat  = prediction.get('outputMulti')
                 
    print 'This car is currently ' + str(label)
    print(stat)

    
def get_api(argv):
    '''
    get access to the Prediction API on commandline
    '''
    argparser = argparse.ArgumentParser()
    argparser.add_argument('storage_path', help='full google storage path of csv data')
    argparser.add_argument('model_id', help='model id of the trained model')
    
    api, flags = sample_tools.init(argv, 'prediction', 'v1.6', __doc__, __file__, parents=[argparser], scope='https://www.googleapis.com/auth/prediction')

    return api


if __name__ == '__main__':
    main()
