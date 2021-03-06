# EXECUTION TIME: 17m48

# Python 3 ImportError
import sys
sys.path.append('.')

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

import src as ya

# prettify plots
plt.rcParams['font.family'] = 'Times New Roman'
sns.set_style({"xtick.direction": "in", "ytick.direction": "in"})

b_sns, g_sns, r_sns, p_sns, y_sns, l_sns = sns.color_palette("muted")

np.random.seed(1)

###########################################################################
# Centroids Vector Quantization
###########################################################################

for num_features in [1, 2, 5, 10, 25, 50]:
    data_train, data_query = ya.data.getCaltech(codebook="random-forest",
                                                num_descriptors=1e5,
                                                pickle_load=False,
                                                pickle_dump=False,
                                                num_features=num_features)
    # TRAINING
    X_train, y_train = data_train[:, :-1], data_train[:, -1]
    class_list = np.unique(y_train)
    fig, axes = plt.subplots(nrows=len(class_list),
                             figsize=(3.0, 3.0*len(class_list)), sharey=True)
    for image_class, ax in zip(class_list, axes.flatten()):
        imgs = X_train[y_train == image_class]
        average_features = np.mean(imgs, axis=0)
        ax.bar(range(1, 1+len(average_features)),
               average_features, color=b_sns)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.set_title('Class %i' % (image_class + 1))
    fig.tight_layout()
    fig.savefig('assets/3.3/bar/train/%i.pdf' % (num_features),
                format='pdf',
                dpi=300,
                transparent=True,
                bbox_inches='tight',
                pad_inches=0.01)
    # TESTING
    X_test, y_test = data_query[:, :-1], data_query[:, -1]
    class_list = np.unique(y_test)
    fig, axes = plt.subplots(nrows=len(class_list),
                             figsize=(3.0, 3.0*len(class_list)), sharey=True)
    for image_class, ax in zip(class_list, axes.flatten()):
        imgs = X_test[y_test == image_class]
        average_features = np.mean(imgs, axis=0)
        ax.bar(range(1, 1+len(average_features)),
               average_features, color=r_sns)
        ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=5))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.set_title('Class %i' % (image_class + 1))
        plt.setp(ax.get_yticklabels(), visible=True)
    fig.tight_layout()
    fig.savefig('assets/3.3/bar/test/%i.pdf' % (num_features),
                format='pdf',
                dpi=300,
                transparent=True,
                bbox_inches='tight',
                pad_inches=0.01)
    print('| %03d DONE |' % num_features)
