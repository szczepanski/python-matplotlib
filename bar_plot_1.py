import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib import style

colors = [u'indigo', u'gold', u'firebrick', u'indianred', u'yellow', u'darkolivegreen', u'darkseagreen',u'midnightblue',
          u'darkorange', u'darkslategrey', u'mediumvioletred', u'mediumorchid', u'mediumslateblue',u'salmon',u'pink',
          u'black', u'springgreen', u'orange', u'brown', u'turquoise', u'olivedrab',u'slategrey',u'peachpuff',u'dimgray',
          u'cyan', u'silver', u'skyblue', u'gray', u'darkturquoise', u'goldenrod', u'darkgreen', u'darkviolet',
          u'darkgray', u'teal', u'darkmagenta', u'yellowgreen',u'blueviolet',u'y', u'mediumaquamarine', u'darkorchid',
          u'thistle', u'violet', u'navy', u'dimgrey', u'orchid', u'blue',u'cornflowerblue', u'palegoldenrod',
          u'darkblue', u'coral', u'darkkhaki', u'mediumpurple', u'red', u'bisque', u'slategray',u'hotpink',u'm',
          u'darkcyan',u'khaki', u'wheat', u'deepskyblue', u'rebeccapurple', u'darkred', u'steelblue',u'tomato',
          u'gainsboro', u'c', u'mediumturquoise', u'g', u'k', u'purple', u'burlywood', u'darksalmon',u'powderblue',
          u'greenyellow', u'royalblue', u'sienna', u'orangered', u'lime', u'palegreen', u'mistyrose', u'seashell',
          u'mediumspringgreen', u'fuchsia', u'chartreuse', u'blanchedalmond', u'peru', u'aquamarine',
          u'darkslategray', u'darkgoldenrod', u'lawngreen', u'chocolate', u'crimson',u'seagreen', u'mediumblue',
          u'forestgreen', u'darkgrey', u'olive', u'b', u'moccasin',u'green', u'paleturquoise',
          u'limegreen', u'saddlebrown', u'grey', u'darkslateblue', u'r', u'deeppink', u'plum',u'rosybrown',
          u'cadetblue', u'dodgerblue', u'maroon', u'sandybrown', u'aqua', u'magenta', u'tan',u'palevioletred',
          u'mediumseagreen', u'slateblue']

# y - data_set
y = [10,22,32,45,15,99,63,56,23,89,55,43,17,93,24]
# x - 0 to the length of dataset(y)
x = [x for x in range(1, len(y)+1)]
# Legend - names
legend_names = ['a/ACPProxy/Random/Lond/Data/tree/Name','b/ACPProxy/Random/Lond/Data/tree/Name',
           'c/ACPProxy/Random/Lond/Data/tree/Name','d/ACPProxy/Random/Lond/Data/tree/Name',
           'e/ACPProxy/Random/Lond/Data/tree/Name','e/ACPProxy/Random/Lond/Data/tree/Name',
           'f/ACPProxy/Random/Lond/Data/tree/Name','g/ACPProxy/Random/Lond/Data/tree/Name',
           'h/ACPProxy/Random/Lond/Data/tree/Name','i/ACPProxy/Random/Lond/Data/tree/Name',
           'j/ACPProxy/Random/Lond/Data/tree/Name','k/ACPProxy/Random/Lond/Data/tree/Name',
           'l/ACPProxy/Random/Lond/Data/tree/Name','m/ACPProxy/Random/Lond/Data/tree/Name',
           'n/ACPProxy/Random/Lond/Data/tree/Name']


fig = plt.figure()


ax1 = plt.subplot2grid((8,5), (0,0), rowspan=6, colspan=5)
# ax1.set_facecolor('snow')
ax1.spines['left'].set_color('lightgrey')
ax1.spines['bottom'].set_color('lightgrey')
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.set_xticks(x)


ax1.set_title('ACP Domain')
for index, val in enumerate(y):
    ax1.bar(x[index], y[index], 1, label=legend_names[index], alpha=0.5, color = random.sample(colors, 30))
for a,b in zip(x, y):
    plt.text(a, b, str(b), ha='center', color='grey')
ax1.set_xlabel('x axis label')
ax1.set_ylabel('y axis label')


ax2 = plt.subplot2grid((8, 5), (6, 0), rowspan=2, colspan=5)
ax2.set_facecolor('white')
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.set_xticks([],minor=False)
ax2.set_yticks([],minor=False)

handles, labels = ax1.get_legend_handles_labels()
legend = ax2.legend(handles, labels, loc='center', framealpha=0.1, ncol=4,prop={'size':8}, fancybox=True, borderaxespad=0)
for text in legend.get_texts():
    text.set_color("grey")

plt.subplots_adjust(wspace=0.2,hspace=2)

plt.show()
