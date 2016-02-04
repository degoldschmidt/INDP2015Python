import numpy as np
import matplotlib.pyplot as plt
 
filename = 'binary_data/example_binary.raw'          
 
# Load numbers from a binary file
data_type = np.float32                                   # Converting binary numbers to 32-bit floats
raw_data = np.fromfile(filename, dtype=data_type)        # Raw data
 
# Now we have a long list of all values in the file. They must be reshaped into
#  2D array with the appropriate dimensions (rows x cols).
number_elements = np.size(raw_data)                      # Number of elements in data matrix
number_cols = 32                                         # 32 channels
number_rows = number_elements/number_cols                # #Elements = #Rows * #Columns 
data = np.reshape(raw_data, (number_rows, number_cols))  # Reshape data matrix
 
# Plot the data in a graph, mark the peaks with r '+' symbols
plt.plot(data[0:100000,2])                               # Plot 2nd column in range 0 to 100000
plt.savefig("binary.pdf")                                # Save plot to file
#plt.show()                                              # Show plot