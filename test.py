
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

a = np.arange(15).reshape(3, 5)
print(a)
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.show()
