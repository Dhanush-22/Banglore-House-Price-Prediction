import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bath,balcony,bhk):
    try:
        loc_index = __data_columns.index(location.lower())
        x = np.zeros(len(__data_columns))

        x[0],x[1],x[2],x[3] = sqft,bath,balcony,bhk
        if(loc_index >=0 ):
            x[loc_index] = 1
        return str(round(__model.predict([x])[0],2)) + "lakh"

    except :
        print("Runtime exception has occured.")
        return None


def get_location_names():
    load_saved_artifacts()
    return __locations


def load_saved_artifacts():
    print("Loading artifacts......")
    global __data_columns
    global __locations
    global __model
    with open('./artifacts/columns.json','rb') as f:
        __data_columns = json.load(f)['data_columns']
    with open('./artifacts/bglr_house_price_prediction','rb') as f:
        __model = pickle.load(f)
    __locations= __data_columns[4:]

    # locat = "1st Phase JP Nagar"
    # loc_index = __data_columns.index(locat.lower())
    # x=np.zeros(len(__data_columns))
    # x[0],x[1],x[2],x[3]=1000.0, 2.0, 1.0, 2
    # if(loc_index>=0):
    #     x[loc_index] = 1
    #     print(__model.predict([x]))
    # else:
    #     print("loc_index is not found.")
    print("Loaded Successfully.")



if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price("1st Phase JP Nagar",1000.0,2.0,1.0,2))