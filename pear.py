import numpy as np

x1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y1_ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
y2_ls = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]



def pearson_corr(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    #print(mean_x)
    #print(mean_y)

    dx = []
    dy = []
    for i in range(len(x)):
        dx.append(x[i]- mean_x)
        dy.append(y[i] - mean_y)
    
    sum_dxdy = 0
    for i in range(len(x)):
        sum_dxdy += dx[i]*dy[i]
    
    dx2 = 0
    dy2 = 0
    for i in range(len(x)):
        dx2 += (x[i]- mean_x)**2
        dy2 += (y[i] - mean_y)**2

    sqr_dx2dy2 = np.sqrt(dx2*dy2)

    r = sum_dxdy/sqr_dx2dy2

    return r

print(pearson_corr(x1_ls, y2_ls))