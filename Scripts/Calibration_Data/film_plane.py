'''
======================
3D surface (color map)
======================

Demonstrates plotting a 3D surface colored with the coolwarm color map.
The surface is made opaque by using antialiased=False.

Also demonstrates using the LinearLocator and custom formatting for the
z axis tick labels.
'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from scipy import interpolate
import statistics as stats

#fig = plt.figure()
#ax = fig.gca(projection='3d')

X = np.arange(5000, 50000, 5000)
Y = np.arange(5000, 30000, 5000)
print(X)
print(Y)
X_mesh = X
Y_mesh = Y
X_mesh, Y_mesh = np.meshgrid(X, Y)


Z_real2 = [[48.59800000000003, 48.59812500000001, 48.60125000000001, 48.60450000000001, 48.595625000000005, 48.581625, 48.58975, 48.587875000000004, 48.562875], [48.57200000000004, 48.575250000000004, 48.5805, 48.55575, 48.554, 48.56125000000001, 48.563500000000005, 48.548750000000005, 48.53875], [48.54100000000004, 48.545125000000006, 48.541250000000005, 48.53425, 48.517375, 48.52462500000001, 48.522875000000006, 48.512125000000005, 48.51225000000001], [48.505000000000045, 48.50925, 48.51250000000001, 48.50650000000001, 48.51075, 48.50200000000001, 48.49425, 48.47650000000001, 48.450750000000006], [48.47500000000005, 48.47325000000001, 48.480500000000006, 48.47375, 48.459, 48.470125, 48.46412500000001, 48.443375, 48.449625000000005]]
Z_real2 = np.array(Z_real2)



# do plane fit
xs = []
ys = []
zs = []
# real1
for i in range(len(X)):
    for j in range(len(Y)):
        xs.append(X[i]/1000)
        ys.append(Y[j]/1000)
        zs.append(Z_real2[j][i])  #here
xs = np.array(xs)
ys = np.array(ys)
zs = np.array(zs)

# do fit
tmp_A = []
tmp_b = []
for i in range(len(xs)):
#    tmp_A.append([xs[i], ys[i], 1])
    tmp_A.append([xs[i]*xs[i], xs[i], ys[i]*ys[i], ys[i], 1])
    tmp_b.append(zs[i])
b = np.matrix(tmp_b).T
A = np.matrix(tmp_A)

#*************

fit = (A.T * A).I * A.T * b
errors = b - A * fit
residual = np.linalg.norm(errors)

avg = 0
max = 0
errors_list = []
for i in errors:
    avg += abs(i)
    if i > max:
        max = i
    errors_list.append(float(i))
avg = avg/len(errors)
print("Avg error: {}".format(avg))
print("Max error: {}".format(max))
print("Stdev: {}".format(stats.stdev(errors_list)))

# Manual solution
largest_error = 1
while largest_error > .01:
    largest_error = 0
    largest_error_index = 0
    
    for i in range(len(errors)):
        if errors[i] > largest_error:
            largest_error = errors[i]
            largest_error_index = i
            
    if largest_error > .01:
        tmp_A.pop(largest_error_index)
        tmp_b.pop(largest_error_index)
        print("pop {} at {}".format(largest_error, largest_error_index))
    b = np.matrix(tmp_b).T
    A = np.matrix(tmp_A)
    
    # Manual solution
    fit = (A.T * A).I * A.T * b
    errors = b - A * fit
    residual = np.linalg.norm(errors)

print("solution:")
#print("{} x + {} y + {} = z".format(fit[0], fit[1], fit[2]))
print("{} x^2 + {} x + {} y^2 + {} y + {} = z".format(fit[0]/1000/1000, fit[1]/1000, fit[2]/1000/1000, fit[3]/1000, fit[4]))
avg = 0
max = 0
errors_list = []
for i in errors:
    avg += abs(i)
    if i > max:
        max = i
    errors_list.append(float(i))
avg = avg/len(errors)
print("Avg error: {}".format(avg))
print("Max error: {}".format(max))
print("Stdev: {}".format(stats.stdev(errors_list)))
x1 = fit[0] * 17669.38*17669.38/1000/1000 + fit[2] * 3928.75*3928.75/1000/1000
x2 = fit[0] * 29669.38*29669.38/1000/1000 + fit[2] * 3928.75*3928.75/1000/1000
y1 = fit[0] * 17669.38*17669.38/1000/1000 + fit[2] * 3928.75*3928.75/1000/1000
y2 = fit[0] * 17669.38*17669.38/1000/1000 + fit[2] * 23384.75*23384.75/1000/1000
print("X bow: {} Y bow: {}".format(abs(x1-x2), abs(y1-y2)))

#*************

# plot raw data
fig = plt.figure()
ax = plt.subplot(111, projection='3d')
surf = ax.scatter(xs, ys, zs, color='b')

# plot plane as mesh
Z = np.zeros(X_mesh.shape)
for r in range(X_mesh.shape[0]):
    for c in range(X_mesh.shape[1]):
#        Z[r,c] = fit[0] * X_mesh[r,c]*X_mesh[r,c]/1000/1000 + fit[2] * Y_mesh[r,c]*Y_mesh[r,c]/1000/1000
        Z[r,c] = fit[0] * X_mesh[r,c]*X_mesh[r,c]/1000/1000 + fit[1] * X_mesh[r,c]/1000 + fit[2] * Y_mesh[r,c]*Y_mesh[r,c]/1000/1000 + fit[3] * Y_mesh[r,c]/1000 + fit[4]
#        Z[r,c] = fit[0] * X_mesh[r,c] + fit[1] * Y_mesh[r,c] + fit[2]
ax.plot_wireframe(X_mesh/1000,Y_mesh/1000,Z, color='k')


# evaluate plane for dataset
#Z_plane = []
#for i in range(X_mesh.shape[0]):
#    row = []
#    for j in range(X_mesh.shape[1]):
#        row.append(float(fit[0]) * X[j] + float(fit[1]) * Y[i] + float(fit[2]))
#    Z_plane.append(row)
#Z_plane = np.array(Z_plane)
#
#Z_diff = np.zeros(X_mesh.shape)
#for r in range(X_mesh.shape[0]):
#    for c in range(X_mesh.shape[1]):
#        Z_diff[r,c] = Z[r,c] - zs[r*X_mesh.shape[1]+c]
#print(Z_diff)
#
#ax.plot_wireframe(X_mesh,Y_mesh,Z_diff, color='k')


## create spline and evaluate for dataset
#Z_spline_int = interpolate.RectBivariateSpline(Y, X, Z_real2, kx=3, ky=3) #here
#Z_spline = []
#for i in range(7):
#    row = []
#    for j in range(6):
#        row.append(Z_spline_int.ev(i*2500, j*2500+17000))
#    Z_spline.append(row)
#Z_spline = np.array(Z_spline)
#
#print(Z_spline_int.ev(22709.38, 18098.75))


## evaluate differences
#Z_diff = []
#for i in range(X_mesh.shape[0]):
#    row = []
#    for j in range(X_mesh.shape[1]):
#        row.append(Z_real2[i][j]-Z_plane[i][j]) #here
#    Z_diff.append(row)
#Z_diff = np.array(Z_diff)


## Plot the data as mesh.
#surf = ax.plot_surface(X_mesh, Y_mesh, Z_real2, cmap=cm.coolwarm, # here
#                    linewidth=0, antialiased=False)


## Plot the diff as mesh.
#surf = ax.plot_surface(X_mesh, Y_mesh, Z_diff, cmap=cm.coolwarm,
#                    linewidth=0, antialiased=False)
#

## plot the spline as mesh
#Z_spline = []
#for i in range(175):
#    row = []
#    for j in range(150):
#        row.append(Z_spline_int.ev(i*100, j*100+17000))
#    Z_spline.append(row)
#Z_spline = np.array(Z_spline)
## Plot extrapolated data?
#surf = ax.plot_surface(X_mesh, Y_mesh, Z_spline, cmap=cm.coolwarm,
#                        linewidth=0, antialiased=False)


## Customize the z axis.
##ax.set_zlim(49.2, 49.4)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.03f'))
#
## Add a color bar which maps values to colors.
#fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_title('Film Plane')
ax.set_xlabel('X position (mm)')
ax.set_ylabel('Y position (mm)')
ax.set_zlabel('Z position (mm)')

plt.show()
