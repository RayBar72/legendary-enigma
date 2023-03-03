#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)


plt.title('Project A')
plt.ylabel('Number of Students')
plt.xlabel('Grades')
plt.xlim([0, 100])
plt.ylim([0, 30])
plt.xticks(range(0, 101, 10))
plt.yticks(range(0, 31, 5))
plt.hist(student_grades, range(10, 101, 10), edgecolor='black')
plt.show()
