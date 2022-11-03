with open('./data_files/normalized-data.csv', 'r+') as input:
    rows = input.readlines()

total_lines= len(rows)
# print (total_lines)
training_len = round((2/3)*total_lines)
validation_len = round((1/3)*total_lines)+training_len

data_train=[]
data_val=[]

for i in range(0,total_lines):
    if i <= training_len:
        data_train.append(rows[i])
    if i <= validation_len and i > training_len:
        data_val.append(rows[i])

with open("./data_files/training-data.csv", "w+") as file:
    for data in data_train:
        file.write(data)

with open("./data_files/validation-data.csv", "w+") as file:
    for data in data_val:
        file.write(data)
