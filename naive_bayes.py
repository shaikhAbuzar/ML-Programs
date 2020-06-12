import pandas as pd
data_set = pd.read_csv('naive.csv')
training_set = data_set.iloc[:, [1, 2, 3, 4]]
test_set = data_set.iloc[:, -1:]

main_probability = list(test_set.play.unique())
main_probability_dict = {}
test_set_probability = {}
temp = test_set.values.tolist()
test_set_list = []
for i in range(len(temp)):
    # print(temp[i][0])
    test_set_list.append(temp[i][0])

for element in main_probability:
    # print(test_set_list.count(element))
    test_set_probability[element] = test_set_list.count(element)
    main_probability_dict[element] = round(test_set_list.count(element)/len(test_set_list), 4)

column_dict = {}
for column in training_set.columns:
    print(f'\n{column}')
    for probability in main_probability:
        temp = training_set[column].values.tolist()
        column_element_list = list(training_set[column].unique())
        for column_element in column_element_list:
            temp_probability = 0
            for i in range(len(temp)):
                if temp[i] == column_element and test_set_list[i] == probability:
                    temp_probability += 1
            print(f'P({column_element}|{probability}) = {temp_probability} / {test_set_probability[probability]}')
            column_dict[f'P({column_element}|{probability})'] = round(temp_probability/test_set_probability[probability], 4)

# while True:
validation_set = list(input('\nEnter the test set: ').split(','))
belongs_to = {}
for probability in main_probability:
    result = 1
    for valid in validation_set:
        result = round(result * column_dict[f'P({valid}|{probability})'], 4)
        # print(f"probability {valid}: {column_dict[f'P({valid}|{probability})']}")
    # print(f'probability {probability}: {main_probability_dict[probability]}')
    result = round(result * main_probability_dict[probability], 4)
    belongs_to[probability] = result
    # print(f'\nProbability of {probability}: {result}')

large = 0
belong_class = ''
for key, value in belongs_to.items():
    if value >= large:
        belong_class = key
        large = value

print(f'The tuple belongs to the class: {belong_class}')





