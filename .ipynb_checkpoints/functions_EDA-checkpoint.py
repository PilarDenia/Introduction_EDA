import numpy as np
import pandas as pd 


#Function explores number of Nan-Null values ​​in each Dataframe column
def number_nan_columns(df):
    print(('number null/Nan_values of columns Dataframe:\n').upper())
    for i in range(len(df.columns)):
        print(i,df.columns[i],':',df.iloc[:,i][df.iloc[:,i].isnull()].shape[0])


#Function explores percentage of Nan-Null values ​​in each Dataframe column
def percentage_nan_columns(df):
    lenght_col = df.shape[0]
    print(('Percentage nan_values of columns Dataframe:\n').upper())
    for i in range(len(df.columns)):
        num_nan_col = df.iloc[:,i][df.iloc[:,i].isnull()].shape[0]
        print(str(i)+'.-',df.columns[i],':',round((num_nan_col/lenght_col)*100,4),'%\n')



#Function explores percentage of Zero values in each Dataframe column
def percentage_zeros_columns(df):
    ar_num_zero = np.count_nonzero(df, axis=0)
    lenght_col = df.shape[0]
    print(('Percentage zero_values of columns Dataframe:\n').upper())
    for i in range(len(df.columns)):
        print(str(i)+'.-',df.columns[i],':',
                round(((lenght_col-ar_num_zero[i])/lenght_col)*100,3),'%\n')
        
        
#Function drop outlayers_maximum and outlayers_minimum of DataFrame
#return df
def drop_outlayers_df(df,column):
    #get 1est quartile and 3er quartile 
    q1 = df[column].quantile(q=0.25)
    q3 = df[column].quantile(q=0.75)
    #inter quartile range
    iqr = q3 - q1
    
    #get maximun
    maximum = q3 + (1.5*iqr)
    
    #get minimum
    minimum = q1 - (1.5*iqr)
    
    #get indexes row outlayers, max and min
    idx_maximum = df[df[column] > maximum].index
    idx_minimum = df[df[column] < minimum].index
    
    #drop rox outlayers
    df.drop(idx_maximum, axis = 0, inplace = True)
    df.drop(idx_minimum, axis = 0, inplace = True)
    
    return df


#function drop outlayers_maximum and outlayers_minimum of DataFrame
#return df
def drop_outlayers_df2(df,column):
    #get 1est quartile and 3er quartile 
    q1 = df[column].quantile(q=0.25)
    q3 = df[column].quantile(q=0.75)
    #inter quartile range
    iqr = q3 - q1
    
    #get maximun
    maximum = q3 + (1.5*iqr)
    
    #get minimum
    minimum = q1 - (1.5*iqr)
    
    #get indexes row outlayers, max and min
    idx_maximum = df[df[column] > maximum].index
    idx_minimum = df[df[column] < minimum].index
    
    #drop row outlayers
    if ((idx_maximum.shape[0]) != 0):
        print('maximum',maximum)
        #print(type(idx_maximum))
        
        for index, val in enumerate(list(idx_maximum)):
            #print(index)
            #print (val)
            df_equal_ids = df.loc[val,:]
            #print(type(df_equal_ids))
            
                    
            for id, row in df_equal_ids.loc[val].iterrows():        
                #print(id)
                #print(row)
                df_equal_ids = df.loc[id,:]
                #print(df_equal_ids)
                df_equal_ids_2 = df_equal_ids[df_equal_ids[column] > maximum]
                #print(df_equal_ids_2)
                df_equal_ids = df_equal_ids_2.reset_index(drop=True)
                break
                
    if ((idx_minimum.shape[0]) != 0):
        print('minimum',minimum)
        print(type(idx_minimum))
        
        for index, val in enumerate(list(idx_minimum)):
            print(index)
            print (val)
            df_equal_ids = df.loc[val,:]
            print(type(df_equal_ids))
            
                    
            for id, row in df_equal_ids.loc[val].iterrows():        
                print(id)
                #print(row)
                df_equal_ids = df.loc[id,:]
                #print(df_equal_ids)
                df_equal_ids_2 = df_equal_ids[df_equal_ids[column] > maximum]
                print(df_equal_ids_2)
                df_equal_ids = df_equal_ids_2.reset_index(drop=True)
                break
       
    return df






