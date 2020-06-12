import pandas as pd
data = pd.read_csv('data.csv')
X = data.iloc[:, 0:2]
y = data.iloc[:, 2]

# print(X)
# print(y)

w1 = 1
w2 = 1
# weights = {}
# for i in range(len(X.columns)):
#     weights['w'+str(i+1)] = 0
# print(weights)
theta = 1

# print(len(X.values))

for i in range(len(X.values)):
    x = X.iloc[i]
    if y[i] == 0:
        # Inhibition
        if w1*x[0] + w2*x[1] < theta:
            continue
        else:
            theta += w1*x[0] + w2*x[1]
    else:
        if w1*x[0] + w2*x[1] >= theta:
            continue
        else:
            # theta += w1*x[0] + w2*x[1]
            if x[0] == 0:
                w2 -= theta
            else:
                w1 -= theta
    # print(x)

print(f'w1:{w1}\nw2:{w2}\ntheta:{theta}')


