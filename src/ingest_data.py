import os
import zipfile
from abc import ABC,abstractmethod
import pandas as pd


#define an abstract class for data ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self,file_path:str)-> pd.DataFrame:
        '''Abstract method to ingest data from a given file.'''
        pass


class ZipDataIngestor(DataIngestor):
    def ingest(self,file_path:str) -> pd.DataFrame:
        '''Extracts a .zip file and returns the content as a pandas data frame.'''
        #ensure the file is a .zip
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file.")


        #extract the zip file
        with zipfile.ZipFile(file_path,"r")as zip_ref:
            zip_ref.extractall("extracted_data")

        #find the extracted csv file (assuming there is one csv file inside the zip.)
        extracted_files=os.listdir("extracted_data")
        csv_files=[f for f in extracted_files if f.endswith(".csv")]

        if len(csv_files)==0:
            raise FileNotFoundError("No CSV file found in the extracted data")
        if len(csv_files)>1:
            raise ValueError("Multiple CSV files found,Please specify which one to use.")

        #Read the csv into a data frame
        csv_file_path=os.path.join("extracted_data",csv_files[0])
        df=pd.read_csv(csv_file_path)

        #return the dataframe
        return df

    
#implement a Facotry to create Dataingestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension:str)-> DataIngestor:
        '''returns the appropriate DataIngestor bsed on file extension.'''
        if file_extension==".zip":
            return ZipDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")



#example usage
if __name__=="__main__":
    ##specify the file path
    #filepath="C:\Users\Keerthi\Documents\AiMlasingh\extracted_data/AmesHousing.csv"

    #determine the file extension
    #file_extension=os.path.splitext(file_path)[1]

    ##ger the appropriarte DataIngestor
    #data_ingestor=DataIngestorFactory.get_Data_ingestor(file_Extension)

    ##ingest the data and load it into a dataframe
    #df=data_ingestor.ingest(file_path)

    ##now df contains the dataframe from the extracted CSV
    #print(df.head())   #dispaly the forst few rows of the dataframe

    pass


