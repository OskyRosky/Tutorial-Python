#############################################
# Intro Python: como utlizariamos un .py    #
#############################################

#################
#     Modulos   #
#################

import pandas as pd
import numpy as np
import os

###############################
#   Set a working  directory  #
###############################


# Get the current working directory  : os.getcwd()
cwd = os.getcwd()
cwd

# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Let's set the directory 

path = 'C:\\Users\\oscar\\Desktop\\Test TEAM\\team_test'

os.chdir(path)


# Print the current working directory
print("Current working directory: {0}".format(cwd))


############################
#            Read Files    #
############################


employee = pd.read_excel('testData.xlsx', sheet_name= 'employee')
workday = pd.read_excel('testData.xlsx', sheet_name= 'workday')


################################################################################################################################################################################################################################
# During this section, you'll need to address different questions using mostly pandas and numpy to address the following questions (Feel free to use also visualization tools such as matplotlib, seaborn or plotly):
#
# 1. Join the two datasets to build a new pandas dataframe called "database". This one will be used to create a machine learning model.
# 2. Which employee has more absences? (Do it in pandas and show in a string which would be the SQL syntax)
# 3. Are there any correlated columns among the "database" data frame?
# 4. Determine which are the top ten reasons and transportation methods for absence at work. (Do it in pandas and show in a string which would be the SQL syntax)
# 5. Create two KPIs that can be a clear target in assessing absences in the company (feel free to create plots using any plotting library)
################################################################################################################################################################################################################################


# 1. Join the two datasets to build a new pandas dataframe called "database". This one will be used to create a machine learning model.


database = pd.merge(employee, workday, on=['employee_id','employee_id'], how='left')

# 2. Which employee has more absences? (Do it in pandas and show in a string which would be the SQL syntax)

more_absences = database.groupby(['employee_id'])

print(database.groupby(['employee_id']))

more_absences = more_absences.min

### etc...