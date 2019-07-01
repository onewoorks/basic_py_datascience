import pandas as pd 

left = pd.DataFrame({
    'id': [1,2,3,4,5],
    'Name': ['Alex', 'Amy', ' Allen', 'Alice', 'Ayoung'],
    'Subject_id': ['sub 1', 'sub 2', 'sub 5', 'sub 9', 'sub 10']
})

right = pd.DataFrame({
    'id': [1,2,3,4,5],
    'Name': ['Amir', 'Mahadi', 'Khairul', 'Pak Yus', 'Iqbal'],
    'Subject_id':['sub 3', 'Sub 6', 'Sub 8', 'Sub 2', 'Sub 1']
})

print(left)
print(right)