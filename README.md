Piotr Szczepanski

# python-matplotlib
<br>
References:

https://www.udemy.com/data-visualization-with-python-and-matplotlib/learn/v4/content
<br>
<br>
<br>
# python-matplotlib

## Basic Graph

```python
#!/usr/bin/env python
# basic 2 plot graph
import matplotlib.pyplot as plt

# 1st plot
x1 = [1, 2, 3, 4, 5]
y1 = [6, 7, 4, 5, 2]

# 2nd plot
x2 = [2, 4, 7, 3, 4]
y2 = [3, 3, 4, 6, 4]

# 3rd argument - label name => to be used in legend
plt.plot(x1, y1, label='1st plot')
plt.plot(x2, y2, label='2nd plot')

plt.title('Basic Graph \n'
          'with a new line subtitle')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.legend()
plt.show()

```
## Basic bar chart

```python
#!/usr/bin/env python
# basic 2 plot bar chart
import matplotlib.pyplot as plt

# 1st plot
x1 = [1, 2, 3, 4, 5]
y1 = [6, 7, 4, 5, 2]

# 2nd plot
x2 = [2, 4, 7, 3, 6]
y2 = [3, 3, 4, 6, 4]

# 3rd argument - label name => to be used in legend
plt.bar(x1, y1, label = '1st plot', color = 'g')
plt.bar(x2, y2, label = '2nd plot', color = 'r')

plt.title('Basic Bar chart\n with a new line subtitle')
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.legend()
plt.show()

```
