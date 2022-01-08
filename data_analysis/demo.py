import pandas as pd
import matplotlib.pyplot as plt
import seaborn
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder

data_set = pd.read_csv('employee_data.csv')

# number_projects = data_set.groupby('number_project').count()
# print(number_projects)
#
# plt.bar(number_projects.index.values, number_projects['satisfaction_level'])
# plt.xlabel('number_projects')
# plt.ylabel('employee number')
# plt.show()


# Time Spent in Company
# time_spent = data_set.groupby('time_spend_company').count()
# print(time_spent)
# plt.bar(time_spent.index.values, time_spent['satisfaction_level'])
# plt.xlabel('Number of Years Spend in Company')
# plt.ylabel('Number of Employees')
# plt.show()


# Subplots using Seaborn
# features = ['number_project', 'time_spend_company', 'Work_accident', 'Departments', 'salary']
# for i, j in enumerate(features):
#     plt.subplot(3, 2, i + 1)
#     seaborn.countplot(x=j, data=data_set)
#     plt.subplots_adjust(hspace=1.0)
#     plt.xticks(rotation=90)
#
# plt.show()

# KMeans cluster
# left_data = data_set[['satisfaction_level', 'last_evaluation']][data_set.left == 1]
# kmeans = KMeans(n_clusters=3).fit(left_data)
# left_data['label'] = kmeans.labels_
# print(left_data)
# plt.scatter(left_data['satisfaction_level'], left_data['last_evaluation'], c=left_data['label'])
# plt.xlabel('satisfaction_level')
# plt.xlabel('last_evaluation')
# plt.show()


# Preprocessing

le = LabelEncoder()
data_set['Departments'] = le.fit_transform(data_set['Departments'])
data_set['salary'] = le.fit_transform(data_set['salary'])
print(data_set)

X = data_set[['satisfaction_level', 'last_evaluation', 'number_project', 'average_montly_hours', 'time_spend_company',
              'Work_accident', 'promotion_last_5years', 'Departments', 'salary']]
y = data_set['left']