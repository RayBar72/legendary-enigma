from numpy.ma.core import identity
#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

fig = plt.figure(constrained_layout=True)

fig.suptitle('All in One')

axd = fig.subplot_mosaic(
    """
    AB
    CD
    EE
    """
)

# axd.set_title('All in One')

axd['A'].plot(range(len(y0)), y0, '-r')

axd['B'].scatter(x1, y1, color='m')
axd['B'].set_title("Men's Height vs Weight", size='x-small')
axd['B'].set_xlabel('Height (in)', size='x-small')
axd['B'].set_ylabel('Weight (lbs)', size='x-small')

axd['C'].plot(x2, y2, '-b')
axd['C'].set_title('Exponential Decay of C-14', size='x-small')
axd['C'].set_xlabel('Time (years)', size='x-small')
axd['C'].set_ylabel('Fraction Remaining', size='x-small')
axd['C'].set_yscale('log')
axd['C'].set_xlim([0, 28650])

axd['D'].plot(x3, y31, '--r', x3, y32, '-g')
axd['D'].set_title('Exponential Decay of Radioactive Elements', size='x-small')
axd['D'].set_xlabel('Time (years)', size='x-small')
axd['D'].set_ylabel('Fraction Remaining')
axd['D'].set_xlim([0, 20000])
axd['D'].set_ylim([0, 1])
axd['D'].legend(['C-14', 'Ra-226'])

axd['E'].hist(student_grades, range(0, 101, 10), edgecolor='black')
axd['E'].set_title('Project A', size='x-small')
axd['E'].set_xlabel('Grades', size='x-small')
axd['E'].set_ylabel('Numeber of Students', size='x-small')
axd['E'].set_xlim([0, 100])
axd['E'].set_ylim([0, 30])
axd['E'].set_xticks(range(0, 101, 10))
axd['E'].set_yticks(range(0, 31, 5))

plt.show()
