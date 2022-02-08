import ast
import numpy as np 
def predict_cells(frame,model):
    '''run single cell prediction of immune cells'''
    li = []; y_pred = [] #empty lists
    studies = list(frame.study.unique()) #studies in the dataframe
    print(studies)
    c=0
    for f in studies:
        c=c+1
        print('Predicting: ', f, '|',c,' out of ', len(studies))
        params = ['CD3','CD19','HLA-DR','CD14','CD56','CD16','CD4','CD8','CD66b','CD27']
        temp = frame[frame.study == f] #extract features
        try:
            temp = temp[params] # attempt to extract features

        except KeyError as e: # catch errors for missing features
            arg = e.args[0][0:-13] #the key for the missing marker
            arg = ast.literal_eval(arg) # convert the string of markers into list

            for x in arg:
                print('      '+x+' is missing - replaced with 0')
                temp[x] = [0] * len(temp) # replace missing values with zero
            temp=temp[params]
        print('number of cells in training:', temp.shape[0])
        
        pred = model.predict(temp, verbose=1) #run prediction
        y_pred.append(pred)
        temp['overall_pred']=[x+1 for x in pred.argmax(axis=1)] #
        #temp['score']
        
        li.append(temp)
        print('      done.')
        print('\n')
        
    final_pred = np.concatenate(y_pred)
    print('Cells successfully predicted!')
    return final_pred