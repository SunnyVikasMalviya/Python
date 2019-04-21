import pandas as pd

file = "automobile.csv"
df = pd.read_csv(file)

#BASIC INSIGHTS OF THE DATASET

print(df.dtypes)   #Returns the datatype of each column present in the dataframe...not a calable function
'''
Why Check Datatype?
Pandas automatically assigns types to the columns in the table by looking at the data
But this automatic type assigning is not accurate at times.
1. Potential info and type mismatch.

To gain the knowledge of the ability to apply the functions at hand to a particular column.
You wouldn't want to waste time passing car_company as a parameter to a method that sums car prices.
2.Compatibility with python methods
'''


print(df.describe())    #Returns the statistical summary of each column present in the dataframe
#Things like mean, min, max,std, count etc. of the data present in each column is returned.
#Help learn data deviations
#Columns that donot have numerical data are automatically skipped


#Below line doesn't work
#df.describe(inlcude="all")  #Returns full summary of all the columns
#unique is the number of distinct objects in the column
#top is the object with the maximum frequency in the dataframe
#freq is the frequency of the top object


print(df.info())    #Returns top and bottom 30 rows to provide a concise summary of the dataframe


"""
Types
Pandas Type                    Native Python Type
object                         string
int64                          int
float64                        float
datetime64, timedelta[ns]      N/A (datetime module is available)
"""

#OUTPUT
"""
RESTART: C:/MvikBack/Python/ToUpload/Data Analysis/Course 2/Analyzing_Input_Dataframe.py 
Unnamed: 0             int64
symboling              int64
normalized-losses     object
make                  object
fuel-type             object
aspiration            object
num-of-doors          object
body-style            object
drive-wheels          object
engine-location       object
wheel-base           float64
length               float64
width                float64
height               float64
curb-weight            int64
engine-type           object
num-of-cylinders      object
engine-size            int64
fuel-system           object
bore                  object
stroke                object
compression-ratio    float64
horsepower            object
peak-rpm              object
city-mpg               int64
highway-mpg            int64
price                 object
dtype: object
       Unnamed: 0   symboling  ...    city-mpg  highway-mpg
count  205.000000  205.000000  ...  205.000000   205.000000
mean   102.000000    0.834146  ...   25.219512    30.751220
std     59.322565    1.245307  ...    6.542142     6.886443
min      0.000000   -2.000000  ...   13.000000    16.000000
25%     51.000000    0.000000  ...   19.000000    25.000000
50%    102.000000    1.000000  ...   24.000000    30.000000
75%    153.000000    2.000000  ...   30.000000    34.000000
max    204.000000    3.000000  ...   49.000000    54.000000

[8 rows x 11 columns]
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 205 entries, 0 to 204
Data columns (total 27 columns):
Unnamed: 0           205 non-null int64
symboling            205 non-null int64
normalized-losses    205 non-null object
make                 205 non-null object
fuel-type            205 non-null object
aspiration           205 non-null object
num-of-doors         205 non-null object
body-style           205 non-null object
drive-wheels         205 non-null object
engine-location      205 non-null object
wheel-base           205 non-null float64
length               205 non-null float64
width                205 non-null float64
height               205 non-null float64
curb-weight          205 non-null int64
engine-type          205 non-null object
num-of-cylinders     205 non-null object
engine-size          205 non-null int64
fuel-system          205 non-null object
bore                 205 non-null object
stroke               205 non-null object
compression-ratio    205 non-null float64
horsepower           205 non-null object
peak-rpm             205 non-null object
city-mpg             205 non-null int64
highway-mpg          205 non-null int64
price                205 non-null object
dtypes: float64(5), int64(6), object(16)
memory usage: 43.3+ KB
None
>>> 

"""
