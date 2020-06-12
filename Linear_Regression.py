n = int(input('Enter no of Samples: '))
X = []
Y = []
for i in range(n):
    Xy = input(f'Enter the x{i+1} and y{i+1} seperated by \' \': ').split()
    X.append(int(Xy[0]))
    Y.append(int(Xy[1]))
xpredict = int(input('Enter the sample for which you need output: '))
#find xbar and ybar
xbar = sum(X)/n
ybar = sum(Y)/n

# find B1 and B0
xi_Xbar = []
yi_ybar = []
xi_xbar_square = []
xi_Xbar_mul_yi_ybar =  []
for x in X:
    xi_Xbar.append(x - xbar)

for y in Y:
    yi_ybar.append(y - ybar)

for x in xi_Xbar:
    xi_xbar_square.append(x**2)

for i in range(n):
    xi_Xbar_mul_yi_ybar.append(xi_Xbar[i]*yi_ybar[i])

B1 = round(sum(xi_Xbar_mul_yi_ybar)/sum(xi_xbar_square), 3)
B0 = round(ybar - B1*xbar, 3)
print('\nEqaution:\ny = {} + {}x'.format(B0, B1))
ypredict = B0 + B1*xpredict
print('y = {} for x = {}'.format(ypredict, xpredict))