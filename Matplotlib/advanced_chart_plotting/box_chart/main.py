
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(5000,  45000, 1000) for _ in range(5)]

plt.figure()

plt.boxplot(data, labels=['Retail', 'Utilities', 'Technology', 'Finance', 'Healthcare'])
plt.xlabel('Industries')
plt.ylabel('Salaries')
plt.title('Estimated Y1 salaries + annual bonus  in SA  - 2025')
plt.grid(True, color='g')
plt.show()
