import pandas as pd
import glob

params = ['CD3','CD19','HLA-DR','CD14','CD56','CD16','CD4','CD8','CD66b','CD27']

def process_data(df1, study):
    print('   processing: '+study)
    origdf = df1
    import ast
    '''process new datasets to prepare for classification'''
    try:
        df1=df1[params] # attempt to extract features

    except KeyError as e: # catch errors for missing features
        arg = e.args[0][0:-13] #the key for the missing marker
        arg = ast.literal_eval(arg) # convert the string of markers into list

        for x in arg:
            print('      '+x+' is missing - replaced with 0')
            df1[x] = [0] * len(df1) # replace missing values with zero
        df1=df1[params]
        
    proc_df = df1[params]
    proc_df['study'] = [study]*len(proc_df)
    proc_df['file'] = list(origdf.file)
    
    return proc_df

def combined_frame(path_to_files, dataset_names): 
    '''provide the path to the cytometry studies and add the name of each dataset for reference'''
    print('(1) importing files ...')
    full_path = path_to_files+'*.csv'
    files = glob.glob(full_path)
    print(list(files))
    print('files imported!')
    print('\n')
    
    li = [] # new list to concatenate dataframes
    print('(2) combining files ...')
    for f,name in zip(files, dataset_names):
        df_tmp = pd.read_csv(f).rename(columns={"sample": "file"})
        df = process_data(df_tmp, name)
        li.append(df)
    
    frame = pd.concat(li, axis=0, ignore_index=True)
    print('files combined!')
    return frame