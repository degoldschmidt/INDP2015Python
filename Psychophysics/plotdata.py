import numpy as np
import matplotlib.pyplot as plt

basma    = 'data/Basma.txt'         # Specify the filename path (location)
dennis   = 'data/Dennis.txt'        # Specify the filename path (location)
marta    = 'data/Marta.txt'         # Specify the filename path (location)
severin  = 'data/Severin.txt'       # Specify the filename path (location)
patricia = 'data/Patricia.txt'      # Specify the filename path (location)

data = []
data.append(np.loadtxt(basma))      # Basma's data
data.append(np.loadtxt(dennis))     # Dennis' data
data.append(np.loadtxt(marta))      # Marta's data
data.append(np.loadtxt(severin))    # Severin's data
data.append(np.loadtxt(patricia))   # Patricia's data
print len(data)
for i in range(len(data)):
    print data[i].shape
    
plt.xlabel('Frequency spread')
plt.ylabel('Success rate')
plt.xlim([0.4,2.1])
plt.ylim([0,1])
four = data[0][(data[0][:,0]==4000)&(data[0][:,2]==20)]
two = data[0][(data[0][:,0]==2000)&(data[0][:,2]==20)]
plt.plot(four[:,1], four[:,8], 'k.-', label='(Basma) 4s')
plt.plot(two[:,1], two[:,8], 'k.--', label='(Basma) 2s') # Plot scatterplot together in one plot

fourB = data[1][(data[0][:,0]==4000)&(data[0][:,2]==20)]
twoB = data[1][(data[0][:,0]==2000)&(data[0][:,2]==20)]
plt.plot(fourB[:,1], fourB[:,8], 'r.-', label='(Dennis) 4s')
plt.plot(twoB[:,1], twoB[:,8], 'r.--', label='(Dennis) 2s') # Plot scatterplot together in one plot

four = data[2][(data[0][:,0]==4000)&(data[0][:,2]==20)]
two = data[2][(data[0][:,0]==2000)&(data[0][:,2]==20)]
plt.plot(four[:,1], four[:,8], 'b.-', label='(Marta) 4s')
plt.plot(two[:,1], two[:,8], 'b.--', label='(Marta) 2s') # Plot scatterplot together in one plot

fourB = data[3][(data[0][:,0]==4000)&(data[0][:,2]==20)]
twoB = data[3][(data[0][:,0]==2000)&(data[0][:,2]==20)]
plt.plot(fourB[:,1], fourB[:,8], 'g.-', label='(Severin) 4s')
plt.plot(twoB[:,1], twoB[:,8], 'g.--', label='(Severin) 2s') # Plot scatterplot together in one plot

four = data[4][(data[0][:,0]==4000)&(data[0][:,2]==20)]
two = data[4][(data[0][:,0]==2000)&(data[0][:,2]==20)]
plt.plot(four[:,1], four[:,8], 'c.-', label='(Patricia) 4s')
plt.plot(two[:,1], two[:,8], 'c.--', label='(Patricia) 2s') # Plot scatterplot together in one plot
plt.legend(loc=0, ncol=2)                                            # Plot legend
plt.savefig("All.pdf")                                       # Save plot to file

plt.xlabel('Success')
plt.ylabel('Decision time [ms]')
plt.xlim([-0.5,1.5])
plt.ylim([0,5000])

successmean = data[0][(data[0][:,3]>0)&(data[0][:,7]==1),3]
print successmean
print np.mean(successmean)
successmean = data[0][(data[0][:,3]>0)&(data[0][:,7]==0),3]
print successmean
print np.mean(successmean)
plt.legend().set_visible(False) 
plt.plot(data[0][:,7], data[0][:,3], 'k.', markersize=5, label='Basma')
plt.plot(data[1][:,7], data[1][:,3], 'r.', markersize=4, label='Dennis')
plt.plot(data[2][:,7], data[2][:,3], 'b.', markersize=3, label='Marta')
plt.plot(data[3][:,7], data[3][:,3], 'g.', markersize=2, label='Severin')
plt.plot(data[4][:,7], data[4][:,3], 'c.', markersize=1, label='Patricia')

plt.savefig("DecisionCluster.pdf")                  # Save plot to file

plt.xlabel('Success')
plt.ylabel('Decision time [ms]')
plt.xlim([-0.2,20.2])
plt.ylim([0,4000])
plt.legend().set_visible(False) 
plt.plot(data[0][:,2], data[0][(data[0][:,7]==1):,3], 'g.', markersize=5, label='Basma')
plt.savefig("TrialDynamics_basma.pdf") 
plt.plot(data[1][:,2], data[1][(data[0][:,7]==1):,3], 'g.', markersize=4, label='Dennis')
plt.savefig("TrialDynamics_dennis.pdf") 
plt.plot(data[2][:,2], data[2][(data[0][:,7]==1):,3], 'g.', markersize=3, label='Marta')
plt.savefig("TrialDynamics_marta.pdf") 
plt.plot(data[3][:,2], data[3][(data[0][:,7]==1):,3], 'g.', markersize=2, label='Severin')
plt.savefig("TrialDynamics_severin.pdf") 
plt.plot(data[4][:,2], data[4][(data[0][:,7]==1):,3], 'g.', markersize=1, label='Patricia')
plt.savefig("TrialDynamics_patricia.pdf")   