# Finance-Project

## Reading and writing Pickle
```python
import pickle 

example_dict = {'first': 23 , 'second': 45, 'third': 65, 'fourth': 'this will not be in the correct order' ,
'fifth': 'dictionaries are not ordered by number', 'sixth': 897}
example_dict['seventh'] = 'I did not do the keys correctly'
example_dict['eight'] = 9080

#print(example_dict.keys())
#print(example_dict.values())

# wb : write binary
pickle_out = open('dict.pickle', 'wb')

# read data from the dictionary and put in the pickle file
pickle.dump(example_dict, pickle_out)
pickle_out.close()

# rb : read bytes
pickle_in = open('dict.pickle', 'rb')
# read the pickle file and put information into the dictionary
example_dict = pickle.load(pickle_in)
```

## TinyDB

หากคุณเป็นนักพัฒนาภาษา Python และคุณต้องการสร้างโปรแกรมขนาดเล็กที่ต้องการฐานข้อมูลขนาดเล็ก แต่คุณไม่ต้องการใช้ SQLite ขอแนะนำให้รู้จัก Database ที่ชื่อ TinyDB

TinyDB เป็นระบบฐานข้อมูลขนาดเล็กที่เขียนด้วยภาษา Python และเป็นฐานข้อมูลประเภท NoSQL แถมเป็น Document-Oriented Database (เก็บข้อมูลในรูปแบบเอกสารเดียวกัน) ไม่ต้องการไลบารีอื่นเพิ่มเติม เพราะเป็น pure Python

- รองรับทั้ง Python 2.7 และ Python 3
- ง่าย สะดวกและรวดเร็ว
- ทำงานได้ทั้ง CPython และ PyPy

[Source:](https://python3.wannaphong.com/2017/10/python-tinydb.html)

### Basic Usage
```python
from tinydb import TinyDB, Query
db = TinyDB('db.json')
User = Query()
db.insert({'type': 'apple', 'count': 7})
db.insert({'type': 'peach', 'count': 3})
db.all()
```
output:
```
[{'count': 7, 'type': 'apple'}, {'count': 3, 'type': 'peach'}]
```
```python
for item in db:
  print(item)
 ```
 Output:
  ```
{'count': 7, 'type': 'apple'}
{'count': 3, 'type': 'peach'}
   ```
 ```python
Fruit = Query()
db.search(Fruit.type == 'peach')
```
```
[{'count': 3, 'type': 'peach'}]
```
```python
db.search(Fruit.count > 5)
```
```
[{'count': 7, 'type': 'apple'}]
 ```
```python
db.update({'count': 10}, Fruit.type == 'apple')
db.all()
```
```
[{'count': 10, 'type': 'apple'}, {'count': 3, 'type': 'peach'}]
```
```python
db.remove(Fruit.count < 5)
db.all()
```
```
[{'count': 10, 'type': 'apple'}]
```
```python
db.purge()
db.all()
```
```
[]
```

[Document:](https://tinydb.readthedocs.io/en/latest/index.html)


## Reading and writing HDF5 format files

### seed for replication
```python

np.random.seed(123456)
# create a DataFrame of dates and random numbers in three columns
df = pd.DataFrame(np.random.randn(8, 3), 
                  index=pd.date_range('1/1/2000', periods=8),
                  columns=['A', 'B', 'C'])
```
### create HDF5 store
```python

store = pd.HDFStore('data/store.h5')
store['df'] = df # persisting happened here
store
```

```
<class 'pandas.io.pytables.HDFStore'>
File path: data/store.h5
/df            frame        (shape->[8,3])
```
### read in data from HDF5
```python

store = pd.HDFStore("data/store.h5")
df = store['df']
df[:5]
```

```
                   A         B         C
2000-01-01  0.469112 -0.282863 -1.509059
2000-01-02 -1.135632  1.212112 -0.173215
2000-01-03  0.119209 -1.044236 -0.861849
2000-01-04 -2.104569 -0.494929  1.071804
2000-01-05  0.721555 -0.706771 -1.039575
```

### this changes the DataFrame, but did not persist
```python

df.iloc[0].A = 1 
# to persist the change, assign the DataFrame to the 
# HDF5 store object
store['df'] = df
# it is now persisted
# the following loads the store and 
# shows the first two rows, demonstrating
# the the persisting was done
pd.HDFStore("data/store.h5")['df'][:5] # it's now in there
```
```
                   A         B         C
2000-01-01  1.000000 -0.282863 -1.509059
2000-01-02 -1.135632  1.212112 -0.173215
2000-01-03  0.119209 -1.044236 -0.861849
2000-01-04 -2.104569 -0.494929  1.071804
2000-01-05  0.721555 -0.706771 -1.039575
```
