import numpy as np
import pandas as pd
import numpy
import datetime

# check the input type
def check_input_type(data):
    return type(data)

# check the lenght of dataframe
def check_input_lenght(data):
    return len(data)


# convert the dictionary into dataframe
def dic_dataframe(data):
    return pd.DataFrame(data)
    
# convert unicode array into object
def convert_unicode_type_into_object(data):
    # check type of array
    type(data)
    if type(data)==list :
        print('List type object is not defined')
    elif type(data)==tuple:
        print('tuple type object is not defined')
    elif type(data)==dict:
        print('dict type object is not defined')
    else:
        np.unicode_ = numpy.ndarray
        if type(data) == np.unicode_ :
            return data.astype('O')
        else :
            print('convert into unicode type')

# calculate the next date 
def calculate_next_date(date_str):
    try :
       date_str=datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
       print(date_str)
    except :
        try : 
            date_str=datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
        except :
            date_str=datetime.datetime.strptime(date_str, '%m/%d/%Y').date()
    date_str=date_str + datetime.timedelta(days=1)
    print('Next Day date=' , date_str)

# calculate the prev date 
def calculate_prev_date(date_str):
    try :
       date_str=datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
       print(date_str)
    except :
        try : 
            date_str=datetime.datetime.strptime(date_str, '%d-%m-%Y').date()
        except :
            date_str=datetime.datetime.strptime(date_str, '%m/%d/%Y').date()
    date_str=date_str - datetime.timedelta(days=1)
    print('Next Day date=' , date_str)

# Reshape the Array 
def reshape_array(arr , r, c):
    arr=arr.reshape(r,c)
    print(arr)


# Check the Shape of Array
def check_shape_array(arr):
    arr=arr.shape
    print(arr)



