from geo_connection import *
from xlrd import open_workbook
import pandas as pd
from geopy.exc import GeocoderTimedOut

class Excel():
    def __init__(self):
        self.addressList = list()
        self.gmaps = get_geo_conn()

    def readDataFromExcel(self ,request_file_location):
        try:
            dataframe = pd.read_excel(request_file_location)
            temp_address_list = []
            temp_lat_list = []
            temp_lng_list = []
            for addres in range(len(dataframe)):
                current_addres = dataframe['Address'][addres]
                temp_lat_lng = self.get_lat_lng(current_addres)
                temp_address_list.append(current_addres)
                temp_lat_list.append(temp_lat_lng['lat'])
                temp_lng_list.append(temp_lat_lng['lng'])
                new_dataframe = pd.DataFrame({'Address': temp_address_list,'Lat':temp_lat_list,'Lng':temp_lng_list})
                new_dataframe.to_excel(request_file_location,index=False)
        except Exception as e:
            print("Error in readDataFromExcel method, Excel Class",e)

    def get_lat_lng(self,addres):
        try:
            print addres
            location = self.gmaps.geocode(addres)
            if location:
                return {'lat':location.latitude, 'lng':location.longitude}
            else:
                return {'lat':'', 'lng':''}
        except GeocoderTimedOut as e:
            print("Error in get_lat_lng method, Excel Class : geocode failed on input %s with message %s"%(addres, e.message))

if __name__ == '__main__':
    exce_obj = Excel()
