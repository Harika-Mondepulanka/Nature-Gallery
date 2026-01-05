import matplotlib.pyplot as plt
import numpy as np

data = np.array([[2.0, 3.0], [3.5, 5.0], [1.0, 2.0], [4.0, 4.5]])
attr1, attr2 = data[:, 0], data[:, 1]
labels = ['Instance 1', 'Instance 2', 'Instance 3', 'Instance 4']

# Histogram
plt.figure(figsize=(10, 6))
for attr, name in zip([attr1, attr2], ['Attribute 1', 'Attribute 2']):
    plt.hist(attr, bins=5, alpha=0.7, label=name)
plt.title('Histogram of Attributes'); plt.xlabel('Value'); plt.ylabel('Frequency'); plt.legend(); plt.show()

# Box Plot
plt.boxplot([attr1, attr2], labels=['Attribute 1', 'Attribute 2'])
plt.title('Box Plot of Attributes'); plt.ylabel('Value'); plt.show()

# Bar Chart
x = np.arange(len(labels)); w = 0.35
plt.bar(x - w/2, attr1, w, label='Attribute 1')
plt.bar(x + w/2, attr2, w, label='Attribute 2')
plt.xticks(x, labels); plt.title('Bar Chart of Attributes'); plt.ylabel('Value'); plt.legend(); plt.show()

# Pie Chart
plt.pie(attr1, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title('Pie Chart of Attribute 1'); plt.show()
