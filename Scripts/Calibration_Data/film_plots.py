
import matplotlib.pyplot as plt
import numpy as np
import statistics as stats

# Some example data to display
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

#fig, axs = plt.subplots(6)
#fig.suptitle('Vertically stacked subplots')
#axs[0].plot(x, y)
#axs[1].plot(x, -y)
#axs[2].plot(x, -y)
#axs[3].plot(x, -y)
#axs[4].plot(x, -y)
#axs[5].plot(x, -y)



#x_50=[48.5, 48.55, 48.6, 48.65, 48.7, 48.75, 48.8, 48.85, 48.9, 48.95, 49.0, 49.05, 49.1, 49.15, 49.2, 49.25, 49.3, 49.35, 49.4, 49.45, 49.5]
#y_50=[3.907720817250568, 3.763318348375959, 3.737188679733019, 3.7322203179931304, 3.738112234832766, 3.7476372347001194, 3.7541887380330508, 3.854993409652912, 3.9153723400080103, 4.001294717281165, 4.413531585142238, 5.162958287561649, 9.397564184424326, 52.544865791578204, 196.95858396182427, 206.52891758427833, 153.09362185358398, 9.4819405919961, 4.495890094442918, 3.627444842226723, 3.514565342388573]
#v_50=49.25
#x_10=[49.2, 49.21, 49.220000000000006, 49.230000000000004, 49.24, 49.25, 49.260000000000005, 49.27, 49.28, 49.290000000000006, 49.300000000000004]
#y_10=[224.5819385714574, 258.14117955477883, 202.3543026379346, 128.3732808575037, 74.00189624582781, 35.93224610681317, 13.421621753521997, 9.944699722900673, 9.406608453666463, 7.619270107299704, 6.495162642708332]
#v_10=49.2
#x_3=[49.179, 49.182, 49.185, 49.188, 49.191, 49.194, 49.197, 49.2, 49.203, 49.206, 49.209, 49.212, 49.215, 49.218, 49.221000000000004]
#y_3=[220.45043545018376, 285.8523321528111, 308.5096368504114, 313.3104412201859, 313.52521423376186, 312.1971722743264, 296.8567310944836, 288.489278446478, 275.67642413832266, 265.3328425375592, 236.4976721214675, 190.566859120556, 145.03687793827334, 136.28600621646115, 117.75695678156762]
#v_3=49.191
#x_1=[49.181000000000004, 49.182, 49.18300000000001, 49.184000000000005, 49.185, 49.18600000000001, 49.187000000000005, 49.188, 49.18900000000001, 49.190000000000005, 49.191, 49.19200000000001, 49.193000000000005, 49.194, 49.19500000000001, 49.196000000000005, 49.197, 49.19800000000001, 49.199000000000005, 49.2, 49.20100000000001]
#y_1=[256.2177271296046, 277.20135949330466, 290.064479202207, 300.4751633882897, 307.5528994537829, 308.6828401313396, 312.677942543133, 312.97463943984184, 313.79686192774057, 314.97774744414806, 315.1656494755057, 310.2810178587531, 305.1602168733046, 302.67507298925307, 301.8531187912996, 297.6010333414373, 290.3215534511029, 285.6272501655507, 273.5700758508739, 268.7557677030012, 260.9583813016866]
#v_1=49.18900000000001

#x_30=[48.365000000000045, 48.395000000000046, 48.42500000000005, 48.45500000000005, 48.48500000000004, 48.51500000000004, 48.545000000000044, 48.575000000000045, 48.60500000000005, 48.63500000000005, 48.66500000000004]
#y_30=[15.943484637725293, 16.162728729798154, 16.21984216174667, 17.07108168330094, 18.141796359036753, 18.30695784810981, 16.169543276975013, 16.386814780069578, 16.361935779893365, 15.90389637199953, 15.899431350751028]
#v_30=48.51500000000004
#x_10=[48.465000000000046, 48.475000000000044, 48.48500000000005, 48.49500000000005, 48.505000000000045, 48.51500000000004, 48.52500000000005, 48.535000000000046, 48.545000000000044, 48.55500000000005, 48.56500000000005]
#y_10=[17.573953324727235, 18.580937336823077, 18.84707334339469, 19.401745755677325, 17.57077385176175, 16.741232346475023, 16.54992009516978, 16.44308587945725, 16.35987568210284, 16.23861682796082, 16.263071154861564]
#v_10=48.48500000000005
#x_3=[48.46400000000005, 48.46700000000005, 48.47000000000005, 48.47300000000005, 48.47600000000005, 48.47900000000005, 48.48200000000005, 48.48500000000005, 48.48800000000005, 48.49100000000005, 48.49400000000005, 48.49700000000005, 48.50000000000005, 48.50300000000005, 48.50600000000005]
#y_3=[17.515635112431173, 18.772529274638607, 18.978343918172747, 18.58383007958706, 17.532424078671873, 18.608391319374356, 21.323106725734764, 21.152001178278013, 20.976599417592865, 20.784278441108704, 20.23877179742209, 17.699811285885794, 17.481236364531682, 17.316020476641242, 17.17927496956688]
#v_3=48.48800000000005
#x_1=[48.47800000000005, 48.47900000000005, 48.480000000000054, 48.48100000000005, 48.48200000000005, 48.483000000000054, 48.48400000000005, 48.48500000000005, 48.486000000000054, 48.48700000000005, 48.48800000000005, 48.489000000000054, 48.49000000000005, 48.49100000000005, 48.492000000000054, 48.49300000000005, 48.49400000000005, 48.495000000000054, 48.49600000000005, 48.49700000000005, 48.498000000000054]
#y_1=[18.042551141802633, 18.281024579741192, 18.450990036767053, 19.540087907762235, 20.37557163189247, 20.564427647773165, 20.800221541362127, 20.24661967933669, 20.124353817909487, 20.031039524461615, 20.03639302367798, 19.791981529648147, 19.41542723075245, 19.024549811145533, 18.964563435605818, 18.490602847263506, 17.96131787736668, 17.720565390526435, 17.782838071079738, 17.81164570611872, 17.745395419780685]
#v_1=48.48500000000005

x_3=[48.573875, 48.576875, 48.579875, 48.582875, 48.585875, 48.588875, 48.591875, 48.594875, 48.597875, 48.600875, 48.603875, 48.606875, 48.609875, 48.612875, 48.615875]
y_3=[56.345137343362666, 73.69870089666539, 99.32676742092835, 119.70191401723235, 131.45847567760148, 116.96931378452523, 101.25243703567864, 96.8136061949711, 90.24389359353012, 86.06148355031553, 86.18411325876276, 78.35903120486772, 77.14455880394462, 76.21223305288223, 66.4163765176306]
v_3=48.588875
x_1=[48.578875000000004, 48.579875, 48.580875000000006, 48.581875000000004, 48.582875, 48.583875000000006, 48.584875000000004, 48.585875, 48.586875000000006, 48.587875000000004, 48.588875, 48.589875000000006, 48.590875000000004, 48.591875, 48.59287500000001, 48.593875000000004, 48.594875, 48.59587500000001, 48.596875000000004, 48.597875, 48.59887500000001]
y_1=[93.77067547628789, 101.99057337018247, 106.95393753712156, 118.84941019742092, 120.92614404072106, 158.36424404726844, 167.59011161994852, 173.90479301310438, 141.43033544787363, 140.94848121824327, 129.8730069163973, 117.6193352337583, 84.69606597289899, 82.06483231115021, 79.10714709702866, 72.11586518855611, 66.03777418304495, 60.10060940511566, 70.26392180722763, 73.7758540931278, 80.41880824880758]
v_1=48.584875000000004


#xs = [x_50, x_10, x_3, x_1]
#ys =  [y_50, y_10, y_3, y_1]
#fs =  [v_50, v_10, v_3, v_1]

#xs = [x_30, x_10, x_3, x_1]
#ys =  [y_30, y_10, y_3, y_1]
#fs =  [v_30, v_10, v_3, v_1]

xs = [x_3, x_1]
ys =  [y_3, y_1]
fs =  [v_3, v_1]

def get_fit(X,Y):
    z = np.polyfit(X, Y, 3)
    
    print("solution:")
    print("{} x^3 + {} x^2 + {} x + {} = y".format(z[0], z[1], z[2], z[3]))
    
    p = np.poly1d(z)

    y_new = np.zeros(len(X))
    for i in range(len(X)):
        x_1 = X[i]
        y_new[i] = p(x_1)
    return y_new

fig, axs = plt.subplots(1, len(xs))
for j in range (len(xs)):
    axs[j].plot(xs[j], ys[j])
    if j >= 2:
        axs[j].plot(xs[j], get_fit(xs[j],ys[j]))
    axs[j].axvline(fs[j], color='r')
    
#axs[0].set_title('50 um')
#axs[1].set_title('10 um')
#axs[2].set_title('3 um')
#axs[3].set_title('1 um')
#
#axs[0].set(xlabel='Z position (mm)')
#axs[1].set(xlabel='Z position (mm)')
#axs[2].set(xlabel='Z position (mm)')
#axs[3].set(xlabel='Z position (mm)')

#axs[0].set_title('30 um')
#axs[1].set_title('10 um')
#axs[2].set_title('3 um')
#axs[3].set_title('1 um')
#
#axs[0].set(xlabel='Z position (mm)')
#axs[1].set(xlabel='Z position (mm)')
#axs[2].set(xlabel='Z position (mm)')
#axs[3].set(xlabel='Z position (mm)')

axs[0].set_title('3 um')
axs[1].set_title('1 um')

axs[0].set(xlabel='Z position (mm)')
axs[1].set(xlabel='Z position (mm)')

axs[0].set(ylabel='Focus Score')

plt.show()