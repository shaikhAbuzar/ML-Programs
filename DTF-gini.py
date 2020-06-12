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


def entropy_and_gain(column_name, classList, n, ginis):
    print('\n[INFO] Calculating E(A) and gain(A) for column: ', column_name)
    column = X[column_name]
    # print(type(column))
    column_elements = []
    for element in column:
        if element in column_elements:
            continue
        column_elements.append(element)
    # print(column_elements)

#    element_gini = {}
    for element in column_elements:
#        pi = 0
#        ni = 0
        elementClasses = {}
        for j in range(len(column)):
            for elementClass in classList:
                if column[j] == element and y[j] == elementClass:
                    elementClasses[elementClass + column[j]] += 1
        print(elementClasses)
        # i_pi_ni = 0
# =============================================================================
#         if pi == 0 or ni == 0:
#             i_pi_ni = 0
#         elif pi == ni:
#             i_pi_ni = 1
#         else:
#             i_pi_ni = gini(pi, ni)
#         element_gini[element] = [pi, ni, i_pi_ni]
#     # print(element_pi_ni)
#     ent = find_entropy(element_pi_ni, n)
#     print('\t\tEntropy of {} is {}'.format(column_name, ent))
#     gain = find_gain(Ipn, ent)
#     print('\t\tGain of {} is {}'.format(column_name, gain))
#     return gain
# =============================================================================


if __name__ == '__main__':
    data = pd.read_csv('Sunburn.csv')
    # print(data)
    X = data.iloc[:, 1:5]
    y = data.iloc[:, 5]
    y_list = list(y)
    # print(X,'\n', y)

#    positive = y[0]
#    negative = ''
#    pCount = 1
    classList = []
    total = len(y)
    for i in range(total):
        if y[i] not in classList:
            classList.append(y[i])
    probabilityList = []
    for p in classList:
        probabilityList.append((y_list.count(p) / total)**2)
#    nCount = len(y) - pCount
#    ipn = i_p_n(pCount, nCount)
    # pbyn = pCount / n
    # nbyp = nCount / n
    # ipn = round(-(pbyn * log(pbyn, 2) + nbyp * log(nbyp, 2)), 4)
    # print(ipn)
    
    ginis = gini(probabilityList)

    element_dictionary = {}
    for x in X:
        # print(x)
        gain_x = entropy_and_gain(x, classList, total, ginis)
        element_dictionary[x] = gain_x
    # print('\n', element_dictionary)

    root = ''
    large = 0
    for node, gain_n in element_dictionary.items():
        if gain_n > large:
            root = node
            large = gain_n
    print('\n[RESULT] Root Node is:', root)
