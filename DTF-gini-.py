import pandas as pd


def gini(probabilityList):
    return round(1-sum(probabilityList),4)


def find_entropy(attribute_table, p_plus_n):
    # print('Attribute Table:', attribute_table)
    entropy = 0
    for key, values in attribute_table.items():
        # print((values[0]+values[1])*values[2])
        entropy += (values[0] + values[1]) * values[2]
    # print(entropy)
    return round(entropy / p_plus_n, 4)


def find_gain(i_pn, entropy):
    return round(i_pn - entropy, 4)


def entropy_and_gain(column_name, pos, neg, n, ginis):
    print('\n[INFO] Calculating E(A) and gain(A) for column: ', column_name)
    column = X[column_name]
    # print(type(column))
    column_elements = []
    for element in column:
        if element in column_elements:
            continue
        column_elements.append(element)
    # print(column_elements)

    element_gain = {}
    for element in column_elements:
        pi = 0
        ni = 0
        tempClassList = []
        for j in range(len(column)):
            if column[j] == element:
                if y[j] == pos:
                    pi += 1
                elif y[j] == neg:
                    ni += 1
        tempClassList.append(pi)
        tempClassList.append(ni)
#        print(tempClassList)
        if pi == 0 or ni == 0:
            ginia = 0
        elif pi == ni:
            ginia = 0.5
        else:
            tempProbabilityList = []
            for i in tempClassList:
                tempProbabilityList.append((i/sum(tempClassList))**2)   
#            print(tempProbabilityList)
            ginia = gini(tempProbabilityList)
        element_gain[element] = [pi, ni, ginia]
    # print(element_pi_ni)
    giniIndex = find_entropy(element_gain, n)
    print('\t\tGini Index of {} is {}'.format(column_name, giniIndex))
    gain = find_gain(ginis, giniIndex)
    print('\t\tGain Gain of {} is {}'.format(column_name, gain))
    return gain


if __name__ == '__main__':
    data = pd.read_csv('Sunburn.csv')
    # print(data)
    X = data.iloc[:, 1:5]
    y = data.iloc[:, 5]
    y_list = list(y)

    # print(X,'\n', y)

    positive = y[0]
    negative = ''
    pCount = 1
    total = len(y)
    for i in range(1, total):
        if y[i] == positive:
            pCount += 1
        negative = y[i]
#    nCount = len(y) - pCount
    
    classList = []
    for i in range(total):
        if y[i] not in classList:
            classList.append(y[i])
    probabilityList = []
    for p in classList:
        probabilityList.append((y_list.count(p) / total)**2)
    
    ginis = gini(probabilityList)
    # pbyn = pCount / n
    # nbyp = nCount / n
    # ipn = round(-(pbyn * log(pbyn, 2) + nbyp * log(nbyp, 2)), 4)
    # print(ipn)

    element_dictionary = {}
    for x in X:
        # print(x)
        gain_x = entropy_and_gain(x, positive, negative, total, ginis)
        element_dictionary[x] = gain_x
    # print('\n', element_dictionary)

    root = ''
    large = 0
    for node, gain_n in element_dictionary.items():
        if gain_n > large:
            root = node
            large = gain_n
    print('\n[RESULT] Root Node is:', root)
