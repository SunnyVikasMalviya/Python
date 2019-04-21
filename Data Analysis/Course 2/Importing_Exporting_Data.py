import pandas as pd

#READING DATA FROM FILE
file = "imports-85.data" #The file containing the cars dataset
df = pd.read_csv(file, header = None)

#No header is present in the dataset, hence it is necessary to set header parameter to none \
#while calling read_csv()
#Pandas automatically sets the header to all the columns in the dataset as integers if no \
#header is present in the dataset


#CHECKING DATAFORMAT
print(df.head(5))  #Shows the first 5 lines of the dataframe
print(df.tail(7))  #Shows the last 7 lines of the dataframe

#ASSIGNING COLUMN NAMES
headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", \
           "body-style", "drive-wheels", "engine-location", "wheel-base" ,"length", "width", \
           "height", "curb-weight", "engine-type", "num-of-cylinders", "engine-size", \
           "fuel-system", "bore", "stroke", "compression-ratio", "horsepower", "peak-rpm", \
           "city-mpg", "highway-mpg", "price"]
df.columns = headers
print(df.head(3))


#SAVING DATAFRAME TO CSV FILE
path = "automobile.csv"
df.to_csv(path)





"""
Exporting to different formats in Python

Data Format        Read                Save
csv                pd.read_csv()       df.to_csv()
json               pd.read_json()      df.to_csv()
excel              pd.read_excel()     df.to_excel()
sql                pd.read_sql()       df.to_sql()
"""




#OUTPUT
"""
RESTART: C:/MvikBack/Python/ToUpload/Data Analysis/Course 2/Importing_Exporting_Data.py 
   0    1            2    3    4     5   ...    20   21    22  23  24     25
0   3    ?  alfa-romero  gas  std   two  ...   9.0  111  5000  21  27  13495
1   3    ?  alfa-romero  gas  std   two  ...   9.0  111  5000  21  27  16500
2   1    ?  alfa-romero  gas  std   two  ...   9.0  154  5000  19  26  16500
3   2  164         audi  gas  std  four  ...  10.0  102  5500  24  30  13950
4   2  164         audi  gas  std  four  ...   8.0  115  5500  18  22  17450

[5 rows x 26 columns]
     0    1      2       3      4     5   ...    20   21    22  23  24     25
198  -2  103  volvo     gas  turbo  four  ...   7.5  162  5100  17  22  18420
199  -1   74  volvo     gas  turbo  four  ...   7.5  162  5100  17  22  18950
200  -1   95  volvo     gas    std  four  ...   9.5  114  5400  23  28  16845
201  -1   95  volvo     gas  turbo  four  ...   8.7  160  5300  19  25  19045
202  -1   95  volvo     gas    std  four  ...   8.8  134  5500  18  23  21485
203  -1   95  volvo  diesel  turbo  four  ...  23.0  106  4800  26  27  22470
204  -1   95  volvo     gas  turbo  four  ...   9.5  114  5400  19  25  22625

[7 rows x 26 columns]
   symboling normalized-losses         make  ... city-mpg highway-mpg  price
0          3                 ?  alfa-romero  ...       21          27  13495
1          3                 ?  alfa-romero  ...       21          27  16500
2          1                 ?  alfa-romero  ...       19          26  16500

[3 rows x 26 columns]

"""
