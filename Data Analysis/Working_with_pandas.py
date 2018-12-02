import pandas as pd


'''The below code is used to work with a comma separated values(csv) file'''
#the below variable stores the location of the working file
csv_file_path = 'directory/filename.csv'

#df : dataframe, is the part of the datafile that we are working with
#read_csv() is an inbuilt function in pandas
df = pd.read_csv(csv_file_path)

#head() displays the first 5 rows of the dataframe
df.head()



'''The below code is used for working with an excel file'''
#We might need to do this first: pip install xlrd
xlsx_path = 'filename.xlsx'
df = pd.read_excel(xlsx_path)
df.head()



'''Creating a dataframe using a dictionary'''
#Dataframe can be visualized as a table
#Keys corresponds to the column labels
#Values corresponds to the rows
songs = {'Album': ['Thriller', 'Back in Black', 'The Dark side of the Moon', \
                   'The Bodyguard', 'Bat Out of Hell'], \
         'Released': [1982, 1980, 1973, 1992, 1977], \
         'Length' : ['42:19', '42:11', '42:49', '57:44', '46:33']}

#DataFrame() is an in-built pandas function used for creating dataframes
songs_df = pd.DataFrame(songs)
df=pd.DataFrame({'a':[11,21,31],'b':[21,22,23]})



'''Accessing data from dataframe'''
#ix will be deprecated, use iloc for integer indexes
songs_df.ix[0,0]  #Accessing the first row and first column
songs_df.iloc[0,2]  #Accessing the first row and third column
songs_df.ix[0,'Artist']   #Accessing the first row from the Artist column
songs_df.iloc[1, 'Length']   #Accessing the second row from the Length column

#Finding All unique element from a particular column
songs_df['Released'].unique()
#Keep in mind this is same as distinct in SQL



'''To find all the rows that are 'Released' after 1970's'''
required_data = songs_df['Released']>=1980
#The above results in a column of boolean true false values according to the condition
rel_after_1970s = songs_df[required_data]
#The above only assigns the values to the LHS variable for the true boolean values
#The whole thing can be written in a single line of code as:
rel_after_1970s = songs_df[songs_df >= 1980]




'''Creating a new dataframe from the existing dataframe'''
#Slicing Dataframes
df1 = df.ix[0:2, 0:3]   #Slicing the first 2 rows and first three columns and assigning it to the df1
df2 = df.ix[0:3, 'Artist'.'Released']  #Slices the 1st 3 rows of Artist and Released columns and assigns it to df2

#Here df1 is a new dataframe with just the 2 columns from the preexisting dataframe
df3 = songs_df[['Album', 'Length']]



'''Saving a dataframe in a csv file'''
songs_df.to_csv('filename.csv')
#The above function is used only for csv files. Their are other functions for other formats.
#Make sure to include the .csv extension with the filename
