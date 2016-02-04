import numpy as np
import matplotlib.pyplot as plt

filefeed = 'feedled_data/results_feedback.txt'               # Specify the filename path (location)
filenofeed = 'feedled_data/results_forward.txt'              # Specify the filename path (location)
dataA = np.loadtxt(filefeed)                                 # Load numbers from a text file with comma separated values (CSV)
dataB = np.loadtxt(filenofeed)                               # Load numbers from a text file with comma separated values (CSV)

#f, myfig = plt.subplots(2, sharex=True)                     # Create two subplots for feedback and no feedback condition
plt.xlabel('Potentiometer input')
plt.ylabel('Light resistor output')
#myfig[0].set_title('Feedback data')
#myfig[0].plot(dataA[:,1], dataA[:,2] , 'r.')                # Plot the data in a graph
#myfig[1].set_title("No feedback data")
#myfig[1].plot(dataB[:,1], dataB[:,2], 'b.')                 # Plot the data in a graph
plt.ylim([0,700])
plt.plot(dataA[:,1], dataA[:,2], 'r.', label='Feedback')
plt.plot(dataB[:,1], dataB[:,2], 'b.', label='No feedback')  # Plot scatterplot together in one plot
plt.legend(loc=4)                                            # Plot legend
plt.savefig("scatter.pdf")                                   # Save plot to file
#plt.show()                                                  # Show plot