def plot2Ddata(path):
    import numpy as np
    import matplotlib.pyplot as plt

    dat=np.loadtxt(path, unpack=True)    
    plt.plot(dat[0,:],dat[1,:])
    plt.show()
