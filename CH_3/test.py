import os
import numpy as np
def replace_word():
    stext1 = 'Iris-setosa'
    stext2 = 'Iris-versicolor'
    stext3 = 'Iris-virginica'
    rtext1 = '0'
    rtext2 = '1'
    rtext3 = '3'

    fin = open('../dataset/iris.data', 'r')
    fout = open('../dataset/data.csv', 'w')

    stats = os.stat('../dataset/data.csv')
    if(stats.st_size > 0):

        for s in fin:
            if s.find(stext1) > -1:
                fout.write(s.replace(stext1, rtext1))
            elif s.find(stext2) > -1:
                fout.write(s.replace(stext2, rtext2))
            elif s.find(stext3) > -1:
                fout.write(s.replace(stext3, rtext3))

        fin.close()
        fout.close()


def main_operation():
    data = np.loadtxt('../dataset/data.data', delimiter=',')
    data[:, :4] = data[:, :4] - data[:, :4].mean(axis=0)
    imax = np.concatenate((data.max(axis=0)*np.ones((1, 5)), data
                           .min(axis=0)*np.ones((1, 5))), axis=0).max(axis=0)
    data[:,:4] = data[:, :4]/imax[:4]

    print(data[0:5,:])

if __name__== "__main__":
    main_operation()