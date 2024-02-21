# Thermochimica-generated plot script
import matplotlib.pyplot as plt
import numpy as np
import thermoTools

datafile = '/home/mlouis9/thermochimica/outputs/corrVerif500-900C.json'
xkey     = 'temperature'
yused    = [['solution phases', 'MSCL#3', 'quadruplets', 'Cr[2+]-Cr[2+]-Cl-Cl', 'mole fraction'], ['solution phases', 'MSCL#3', 'quadruplets', 'Cr[3+]-Cr[3+]-Cl-Cl', 'mole fraction'], ['solution phases', 'MSCL#3', 'quadruplets', 'Cr[2+]-Cr[3+]-Cl-Cl', 'mole fraction'], ['solution phases', 'PNNM', 'species', 'CrCl2', 'mole fraction'], ['solution phases', 'PNNM#5', 'species', 'CrCl2', 'mole fraction'], ['solution phases', 'P63_M', 'species', 'CrCl2', 'mole fraction'], ['solution phases', 'P63_M#7', 'species', 'CrCl2', 'mole fraction']]
legend   = ['MSCL#3: Cr[2+]-Cr[2+]-Cl-Cl', 'MSCL#3: Cr[3+]-Cr[3+]-Cl-Cl', 'MSCL#3: Cr[2+]-Cr[3+]-Cl-Cl', 'PNNM: CrCl2', 'PNNM#5: CrCl2', 'P63_M: CrCl2', 'P63_M#7: CrCl2']
yused2   = []
legend2  = []
x,y,y2,xlab,ylab,ylab2 = thermoTools.plotDataSetup(datafile,xkey,yused,yused2=yused2)
lns=[]
# Start figure
fig = plt.figure()
ax  = fig.add_axes([0.2, 0.1, 0.75, 0.85])
color = iter(plt.cm.rainbow(np.linspace(0, 1, len(y))))
for yi in range(len(y)):
    c = next(color)
    lns = lns + ax.plot(x,y[yi],'.-',c=c,label=legend[yi])
labs = [l.get_label() for l in lns]
ax.legend(lns, labs, loc=0)
ax.set_xlabel(xlab)
ax.set_ylabel(ylab)
plt.show()
