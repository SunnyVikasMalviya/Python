#Preprocessing data in python
'''
Identify and handle the missing values
Data Formatting, Standardization of the data, converting everything into same units
Data Normalization (Scaling and Centering)
Data Binning
Turning Categorical values into numeric values for easy statistical analysis
'''

#Altering values in a particular columns
df["column_name"] = df["column_name"] + 1

#Dealing with missing values
'''
1. Check with the data collection source
2. Drop the missing values
    2.1. Drop the entire variable
    2.2. Drop the particular data entry
3. Replace the missing values
    3.1. Replace with average of that variable for numerical data
    3.2. Replace with the maximum occuring object for string data
    3.3. Replace based on other function
4. Leave it as missing data

? or NaN represent missing data
'''
#Dropping missing values
#dataframe.dropna() removes all the NaN elements from a particular row or column
#axis = 0 : drops the entire row
#axis = 1 : drops the entire column
df.dropna(subset = ["price"], axis = 0, inplace = True)
                    #or
df = df.dropna(subset = ["price"], axis = 0)
#The above line drops all the rows containing NaNs in their price column
#Setting inplace parameter to true allows the changes made to dataframe directly
#without the inplace parameter, the dataframe remains the same and the function doesn't really do anything

#Replacing missing values
#dataframe.replace(missing_value, new_value) replaces the missing values in all the rows in a particular column
mean = df["column_name"].mean()
df["column_name"].replace(np.nan, mean)


#Data Formatting
'''
Bringing all the data into a common standard of expression to allow users to make comparisons
1. The columns are assigned incorrect datatype
2. The data is in different unit or convention than required
'''
#Changing the unit or convention
df["city-mpg"] = 235/df["city-mpg"]
df.rename(columns = {"city-mpg": "city-L/100km"}, inplace = True)

#Changing the datatype of a column to correct datatype
#dataframe["column_name"].dtypes() checks the datatype of the column_name
#dataframe["column_name"].astype("required_datatype") changes the datatype of the column
df["price"] = df["price"].astype("int")


#Data Normalization
'''
Data with high values or range of values tend to impact the results more as compared to low valued or small ranged data
Normalization is done to bring the datas to the same impact level or to make the datas consistent
Normalization allows a fair comparison between the features making sure they have the same impact
Few approaches towards normalization
1. Simple Feature Scaling
    X_new = X_old/X_max
2. Min-Max
    X_new = (X_old - X_min) / (X_max - X_min)
3. Z-score
    X_new = (X_old - X_mean) / X_std

Normalized data ranges between -3 to +3, however it can be larger
'''
#Simple Featuring Scaling
df["length"] = df["length"]/df["length"].max()

#Min-Max
df["length"] = (df["length"] - df["length"].min)/(df["length"].max() - df["length"].min)

#Z-score
df["length"] = (df["length"] - df["length"].mean())/df["length"].std()


#Binning
'''
Grouping values together into bins or categories for better representation or understanding
'''
bins = np.linspace(min(df["price"]), max(df["price"]), 4)
group_names = ["Low", "Medium", "High"]
df["priced_bins"] = pd.cut(df["price"], bins, labels = group_names, include_lowest = True)
#Histograms can be used to visualize the number of datas in each bin


#Turning categorical data into quantitative variables
'''
Statistical models only work with numerical data and string are not useful with these models
So categorical strings or objects are converted to numerical data
Add dummy variables for each unique category and assign 0 or 1 in each category
This is called One-Hot Encoding
'''
pd.dummies(df["fuel"])
#The dummies function automatically generates a list of numbers each on \
#corresponding to a unique category in the parent column














