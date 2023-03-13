#initial Machine Learning
----
##type models of ML
- Supervised : teach the model by labeling with human ,such as: Classification, Regression,
- unsupervised: no human supervise ,such as: clustering
- Semi supervised: some data have labled
- reinforce: data force to learn
-------
##Library Python for ML
- NumPy : big matrix and arrays
- Keras : neural network
- TensorFlow : graph
- PyTorch : Natural language and vision machine
- Scrapy : give data from website
- BeautifulSoup : extract data from HTML , XML
- Pandas : tables , data analysis,Heterogeneous data
- Scipy: complex math
- Scikit learn : modeling and categorize and clustering and regression  BASE ON Matplotlib , Numpy
- Matplotlib : draw chart
- Seaborn : Data visualization
- NetworkX : In addition to very good 2D and 3D illustrations, many parameters and
Provides standard graph algorithms to the user, such as shortest path, centrality, page ranking
and other
------
##main construction python
- add : append,insert,extend
- del : clear,remove,pop,del
- len ,index, sort, max , min , zeros , ones ,
- tuple : A tuple is a fixed and immutable sequence of objects in Python - tuple_A = (item 1, item 2, item 3,…, item n)
- dictionary: accusative array
- set : It is changeable - not follow a specific order - don't have repetitive element - set_a = {"item 1", "item 2", "item 3",….., "item n"}
-----
## Csv : communication programs with it
```shell
import csv
# opening the CSV file
with open('data.csv', mode ='r')as file:

 # reading the CSV file
 csvFile = csv.reader(file)
 # displaying the contents of the CSV file
 for lines in csvFile:
 print(lines)
```
## request
```shell
import requests
r =requests.get('https://fa.wikipedia.org/wiki/عمیق_یری یادگ('
print(r.content)
```
#DictReader.csv
```shell
import csv
# opening the CSV file
with open('data.csv', mode ='r')as file:

# reading the CSV file
csvFile = csv.DictReader(file)
# displaying the contents of the CSV file
for lines in csvFile:
print(lines)


```
#pandas.read_csv
```shell
import pandas
# reading the CSV file
csvFile = pandas.read_csv('data.csv')
# displaying the contents of the CSV file
print(csvFile)

```