def weight_generator(inputs, n, w, c):
    for j in range(1, n+1):
        print(f'\nStep {j}')
        # print('\nX full', inputs['X'+str(j)])
        x = inputs['X'+str(j)][0]
        print('X:', x)
        d = inputs['X'+str(j)][1]
        print('d:', d)
        net = round(float(np.matmul(w, x)), 2)
        if net > 0:
            o = 1
        elif flag == 1 and net < 0:
            o = -1
        else:
            o = 0
        print('o: '.format(o))
        r = d - o
        print('r:', r)
        delta_w = c*r*x
        print('delta_w:', delta_w)
        w += delta_w
        print('weight:', w)
    return w


if __name__ == '__main__':
    import numpy as np
    no_inputs = int(input('Enter total inputs: '))

    X_dictionary = {}
    flag = 0
    for i in range(1, no_inputs+1):
        temp = []
        input_matrix = np.array(list(input('Enter Matrix{}: '.format(i)).split()), dtype=float)
        temp.append(input_matrix)
        desired_output = float(input("Enter it's desired output: "))
        if desired_output == -1:
            flag = 1
        temp.append(desired_output)
        X_dictionary['X'+str(i)] = temp
    # print(X_dictionary)

    weight = np.array(list(input('Enter Weight Matrix: ').split()), dtype=float)
    constant = float(input('Enter the value of constant: '))

    no_iterations = int(input('Enter no. of iterations: '))

    for iteration in range(no_iterations):
        print(f"\n[ITERATION {iteration+1}]:")
        weight = weight_generator(X_dictionary, no_inputs, weight, constant)
        print(f'\n Weight after {iteration+1}: {weight}')



