import pandas as pd
data_set = pd.read_csv('knndata.csv')
train_set = data_set.iloc[:, :2]
test_set = data_set.iloc[:, 2]

prediction_data = list(input('Enter the prediction value: ').split())
nearest_neighbours = int(input('Enter the neighbours: '))

distance_dict = {}
for i in range(len(train_set)):
    temp = train_set.iloc[i, :].values.tolist()
    distance = 0
    for j in range(len(temp)):
        distance += (temp[j] - int(prediction_data[j])) ** 2
    # print(distance)
    distance_dict[distance] = test_set[i]

sorted_distance_dict = {}
i = 0
for key in sorted(distance_dict.keys()):
    if i == nearest_neighbours:
        break
    sorted_distance_dict[key] = distance_dict[key]
    i += 1

class_dict = {}
class_list = list(test_set.unique())

for element in class_list:
    class_dict[element] = 0

for value in sorted_distance_dict.values():
    class_dict[value] += 1

large = 0
belong_class = ''
for key, value in class_dict.items():
    if value >= large:
        belong_class = key
        large = value

if sum(class_dict.values()) == large * len(class_list):
    small = 99999
    belong_class = ''
    for key, value in sorted_distance_dict.items():
        if int(key) < small:
            belong_class = value
            small = key

print(f'The tuple belongs to the class: {belong_class}')



