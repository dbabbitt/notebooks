
import matplotlib.pyplot as plt
import seaborn as sns
import random

colormaps_list = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r',
                  'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys',
                  'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r',
                  'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r',
                  'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy',
                  'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1',
                  'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Vega10', 'Vega10_r',
                  'Vega20', 'Vega20_r', 'Vega20b', 'Vega20b_r', 'Vega20c', 'Vega20c_r', 'Wistia', 'Wistia_r', 'YlGn',
                  'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r',
                  'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r',
                  'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r',
                  'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat',
                  'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern',
                  'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r',
                  'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma',
                  'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma',
                  'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spectral',
                  'spectral_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r',
                  'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'viridis', 'viridis_r',
                  'winter', 'winter_r']

def r(string_list=colormaps_list):

    return random.choice(string_list)

def first_order_linear_scatterplot(df, xname, yname,
                                   xlabel_str='Overall Capitalism (explanatory variable)',
                                   ylabel_str='World Bank Gini % (response variable)',
                                   x_adj='capitalist', y_adj='unequal',
                                   title='"Wealth inequality is huge in the capitalist societies"'):
    '''
    Create a first order (linear) scatter plot assuming the data frame
    has a column called Country
    '''
    fig1_fig = plt.figure(figsize=(12,8))
    merge_axes_subplot = sns.regplot(x=xname, y=yname, scatter=True, data=df)
    if not xlabel_str.endswith(' (explanatory variable)'):
        xlabel_str = '{} (explanatory variable)'.format(xlabel_str)
    xlabel_text = plt.xlabel(xlabel_str)
    if not ylabel_str.endswith(' (response variable)'):
        ylabel_str = '{} (response variable)'.format(ylabel_str)
    ylabel_text = plt.ylabel(ylabel_str)
    kwargs = dict(textcoords='offset points', ha='left', va='bottom',
                  bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                  arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0'))
    least_x = xdata.min()
    most_x = xdata.max()
    most_y = ydata.max()
    least_unequal = ydata.min()
    for label, x, y in zip(df['Country'], xdata, ydata):
        if (x == least_x):
            annotation = plt.annotate('{} (least {})'.format(label, x_adj),
                                      xy=(x, y), xytext=(40, 10), **kwargs)
        elif (x == most_x):
            annotation = plt.annotate('{} (most {})'.format(label, x_adj),
                                      xy=(x, y), xytext=(-120, 220), **kwargs)
        elif (y == most_y):
            annotation = plt.annotate('{} (most {})'.format(label, y_adj),
                                      xy=(x, y), xytext=(45, 0), **kwargs)
        elif (y == least_unequal):
            annotation = plt.annotate('{} (least {})'.format(label, y_adj),
                                      xy=(x, y), xytext=(-200, 0), **kwargs)
        elif (label == 'United States'):
            annotation = plt.annotate('{} (most evil)'.format(label),
                                      xy=(x, y), xytext=(-75, 25), **kwargs)
    title_obj = fig1_fig.suptitle(title, fontsize=24)