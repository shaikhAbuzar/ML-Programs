import pandas as pd
from math import log


def i_p_n(p_count, n_count):
    n = p_count + n_count
    p_by_n = p_count / n
    n_by_p = n_count / n
    i_pn = round(-(p_by_n * log(p_by_n, 2) + n_by_p * log(n_by_p, 2)), 4)
    return i_pn


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


def entropy_and_gain(column_name, pos, neg, n, Ipn):
    print('\n[INFO] Calculating E(A) and gain(A) for column: ', column_name)
    column = X[column_name]
    # print(type(column))
    column_elements = []
    for element in column:
        if element in column_elements:
            continue
        column_elements.append(element)
    # print(column_elements)

    element_pi_ni = {}
    for element in column_elements:
        pi = 0
        ni = 0
        for j in range(len(column)):
            if column[j] == element:
                if y[j] == pos:
                    pi += 1
                elif y[j] == neg:
                    ni += 1
        # i_pi_ni = 0
        if pi == 0 or ni == 0:
            i_pi_ni = 0
        elif pi == ni:
            i_pi_ni = 1
        else:
            i_pi_ni = i_p_n(pi, ni)
        element_pi_ni[element] = [pi, ni, i_pi_ni]
    # print(element_pi_ni)
    ent = find_entropy(element_pi_ni, n)
    print('\t\tEntropy of {} is {}'.format(column_name, ent))
    gain = find_gain(Ipn, ent)
    print('\t\tGain of {} is {}'.format(column_name, gain))
    return gain


if __name__ == '__main__':
    data = pd.read_csv('Sunburn.csv')
    # print(data)
    X = data.iloc[:, 1:5]
    y = data.iloc[:, 5]
    # print(X,'\n', y)

    positive = y[0]
    negative = ''
    pCount = 1
    total = len(y)
    for i in range(1, total):
        if y[i] == positive:
            pCount += 1
        negative = y[i]
    nCount = len(y) - pCount
    ipn = i_p_n(pCount, nCount)
    # pbyn = pCount / n
    # nbyp = nCount / n
    # ipn = round(-(pbyn * log(pbyn, 2) + nbyp * log(nbyp, 2)), 4)
    # print(ipn)

    element_dictionary = {}
    for x in X:
        # print(x)
        gain_x = entropy_and_gain(x, positive, negative, total, ipn)
        element_dictionary[x] = gain_x
    # print('\n', element_dictionary)

    root = ''
    large = 0
    for node, gain_n in element_dictionary.items():
        if gain_n > large:
            root = node
            large = gain_n
    print('\n[RESULT] Root Node is:', root)
