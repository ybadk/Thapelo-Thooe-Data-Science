
import matplotlib.pyplot as plt 
import numpy as np
import  pandas as pd


np.random.seed()

dt = 0.01

t = np.arange(0.0, 10.0, dt)
s1 = np.sin(2* np.pi * 100 * t)
s2 = 2 * np.sin(2 * np.pi * 400 * t)

s = s1 + s2
s = s + np.random.randn(len(t))

plt.figure()

plt.specgram(s, NFT=256, Fs=1/dt, noverlap=128)
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
