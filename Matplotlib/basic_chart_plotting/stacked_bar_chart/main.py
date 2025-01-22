
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


android_users = ['10-20', '20-30', '30-40', '40-50', '50-60']

females_values = [100, 200, 300, 400, 500]

males_values  = [200, 250, 350, 450, 560]

plt.figure()

plt.bar(android_users, females_values, color='pink', label='Female Android Users' )
plt.bar(android_users, males_values, bottom=females_values, color='darkblue', label='Male Android Users')

plt.xlabel('ANDROID USERS BY AGE')
plt.ylabel('MALE AND FEMALE USERS')

plt.title('ANDROID USERS BY AGE')
plt.legend()
plt.show()
