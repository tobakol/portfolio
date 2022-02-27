from array import array
from statistics import median_low
import numpy as np
import pandas as pd
from pandas import DataFrame, Series


pointer = input('WHere to start?  ')

if pointer == '1':
    array = np.array([1,4,5,8],float)
    print (array)
    print ("")
    array = np.array([[1,2,3], [4,5,6]] , float)
    print(array)

if pointer == '2':
    #list indexing, slicing and manipulations
    array = np.array([1,4,5,8], float)
    print (array[1])
    acer = input('Slice?(Y/N)  ')
    if acer == 'Y':
        print(array[:2])
    else:
        array[1] = 5.0
        print(array[1])

if pointer == '3':
    #matrix indexing and slicing
    two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)
    print (two_D_array)
    
    print (two_D_array[1][1])
    #multiplies specified list elements of the array elements
 
    print (two_D_array[1, :])
    #displays the enumerated array element i.e list
    print (two_D_array[:, 2])
    #displays  the specified elements of the array elements

if pointer == '4':
    # matrix aritmetics array arithmetics
    array_1 = np.array([[1, 2], [3, 4]], float)
    array_2 = np.array([[5, 6], [7, 8]], float)
    print (array_1 + array_2)
    
    print (array_1 - array_2)
    
    print (array_1 * array_2)

if pointer == '5':
    #mean, dot product
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([[6], [7], [8]], float)
    #all the lists in the array must have the same number of elements for mean/median
    #to work
    print (np.mean(array_1))
    print (np.mean(array_2))
    
    print (np.dot(array_1, array_2))
    #dot product

if pointer == '6':
        #The following code is to help you play with the concept of Series in Pandas.

        #You can think of Series as an one-dimensional object that is similar to
        #an array, list, or column in a database. By default, it will assign an
        #index label to each item in the Series ranging from 0 to N, where N is
        #the number of items in the Series minus one.

    #       Please feel free to play around with the concept of Series and see what it does

        #*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
        #http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structure

    ##create a Series object
    #Dataframe is usually how pandas store data
    series = pd.Series(['Dave', 'Cheng-Han', 'Udacity', 42, -1789710578])
    print (series)

if pointer == '7':
    #custom indexing
    series = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print (series)

if pointer == '8':
    ##Series indexing
    serie = pd.Series(['Dave', 'Cheng-Han', 359, 9001],
                       index=['Instructor', 'Curriculum Manager',
                              'Course Number', 'Power Level'])
    print (serie['Instructor'])
    print ("")
    print (serie[['Instructor', 'Curriculum Manager', 'Course Number']])


if  pointer == '9':
    ##boolean indexing
    ##series end
    cuteness = pd.Series([1, 2, 3, 4, 5], index=['Cockroach', 'Fish', 'Mini Pig',
                                                 'Puppy', 'Kitten'])
    print( cuteness > 3)
    print ("")
    print (cuteness[cuteness > 3])

if pointer == '10':
    ##Dataframes in action
    #To create a dataframe, you can pass a dictionary of lists to the Dataframe
    #constructor, or use the method in 9 above

    #1) The key of the dictionary will be the column name
    #2) The associating list will be the values within that column.
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print (football)

if pointer == '11':
    ##Dataframe functions
    #Pandas also has various functions that will help you understand some basic
    #information about your data frame. Some of these functions are:
    #1) dtypes: to get the datatype for each column
    #2) describe: useful for seeing basic statistics of the dataframe's numerical
   #  columns
    #3) head: displays the first five rows of the dataset
    #4) tail: displays the last five rows of the dataset
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print (football.dtypes)
    print ("")
    print (football.describe())
    print ("")
    print (football.head())
    print ("")
    print (football.tail())


if pointer == '12':
    ##Dataframe exercise
    def create_dataframe():
        countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

        gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
        bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
        olympics = {'country_name': countries, 'gold': gold, 'silver' : silver, 'bronze': bronze }
        olympic_medal_counts_df = pd.DataFrame(olympics)
        print(olympic_medal_counts_df)

    create_dataframe()



        
if pointer == '13':
    #You can think of a DataFrame as a group of Series that share an index.
    #This makes it easy to select specific columns that you want from the DataFrame. 

    ##Selecting COLUMNSfrom Dataframes
    #1) Selecting a single column from the DataFrame will return a Series
    #2) Selecting multiple columns from the DataFrame will return a DataFrame
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print (football['year'])
    print ('')
    print (football.year)  
    # shorthand for football['year']
    print ('')
    print (football[['year', 'wins', 'losses']])

if pointer == '14':
    #boolean indexing in action
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print (football.iloc[[0]])
    print ("")
    print (football.loc[[0]])
    #same with above
    print ("")
    print (football[3:5])
    print ("")
    print (football[football.wins > 10])
    #WORKS REGARDLESS OF STRING ANNOTATION I.E WINS
    print ("")
    print (football[(football.wins > 10) & (football.team == "Packers")])
    #IMPORTANT note, the use of and and normal brackets


if pointer == '15':

    #when you use apply  method, the result is itself a dataframe
    #applymap works on the entire dataframe, map is for a single column
    # (check e.g using lambda x: x>= 1)
    
    #As a refresher on lambda, lambda functions are small inline functions that 
    #are defined on-the-fly in Python. lambda x: x>= 1 
    #will take an input x and return x>=1, or a boolean that equals True or False.
    def avg_medal_count():
    
    
        countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

        gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
        bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    
        olympic_medal_counts = {'country_name':countries,
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}    
        ast = pd.DataFrame(olympic_medal_counts)

        irg = ast[ast['gold'] > 0]
        print(np.mean(irg['gold']))

        irs = ast[ast['silver'] > 0]
        print(np.mean(irs['silver']))

        irb = ast[ast['bronze'] > 0]
        print(np.mean(irb['bronze']))
    
    # YOUR CODE HERE
    
    avg_medal_count()

if pointer == '15a':
#same as 15, but using map methods
#What does applymap differ from map on?
    def avg_medal_count():
    
    
        countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

        gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
        bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    
        olympic_medal_counts = {'country_name':countries,
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}    
        ast = DataFrame(olympic_medal_counts)

        irg = ast[['gold', 'silver', 'bronze']].apply(np.mean)
        print(irg)

    avg_medal_count()
        
if pointer == '15b':
#same as 15, but using map methods
#What does applymap differ from map on?
    def avg_medal_count():
    
    
        countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

        gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
        bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
    
        olympic_medal_counts = {'country_name':countries,
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}    
        ast = DataFrame(olympic_medal_counts)

        irg = pd.Series[ast.gold[ast.gold> 0], ast.silver[ast.silver> 0], ast.bronze[ast.bronze> 0]].apply(np.mean)
        print(irg)

        
    
    # YOUR CODE HERE
    
    avg_medal_count()

if pointer == '16':
    ##cross product method1
    def points():
        countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea', 
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

        gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
        bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]
        olympic_medal_counts = {'country_name':countries,
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}    
        ast = DataFrame(olympic_medal_counts)
        medal_count = ast[['gold', 'silver', 'bronze']] 
        points = [4,2,1]
        olympic_points_count = (np.dot(medal_count, points))
        olympic_points_df = DataFrame ({'country_name': Series(countries), 'points' : Series(olympic_points_count)})
        #The point of the 'Series' prefix is to enter the lists as a single entry to 
        #allow Dataframe to read the list.
        print(olympic_points_df)
    points()



    

