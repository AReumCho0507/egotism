#20단

for i in range(2, 20):
    print('[', i, '단]')
    for j in range(1, 10):
        print('%dx%d=%d'%(i,j,i*j))
    print('')

