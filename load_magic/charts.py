
# This should by imported something like this in your notebook:
# %run ../../load_magic/charts.py
#

from cycler import cycler
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import random
import seaborn as sns

# Use the following only if you are on a high definition device
from IPython.display import set_matplotlib_formats
set_matplotlib_formats('retina')

colormaps_list = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap',
                  'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r',
                  'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r',
                  'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples',
                  'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r',
                  'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia',
                  'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot',
                  'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r',
                  'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix',
                  'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat',
                  'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r',
                  'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r',
                  'hsv', 'hsv_r', 'icefire', 'icefire_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'mako',
                  'mako_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r',
                  'prism', 'prism_r', 'rainbow', 'rainbow_r', 'rocket', 'rocket_r', 'seismic', 'seismic_r', 'spring',
                  'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c',
                  'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r',
                  'viridis', 'viridis_r', 'vlag', 'vlag_r', 'winter', 'winter_r']
FACEBOOK_ASPECT_RATIO = 1.91
TWITTER_ASPECT_RATIO = 16/9

def r(string_list=colormaps_list):

    return random.choice(string_list)

def first_order_linear_scatterplot(df, xname, yname,
                                   xlabel_str='Overall Capitalism (explanatory variable)',
                                   ylabel_str='World Bank Gini % (response variable)',
                                   x_adj='capitalist', y_adj='unequal',
                                   title='"Wealth inequality is huge in the capitalist societies"',
                                   idx_reference='United States', annot_reference='most evil',
                                   aspect_ratio=FACEBOOK_ASPECT_RATIO,
                                   least_x_xytext=(40, -10), most_x_xytext=(-150, 55),
                                   least_y_xytext=(-200, -10), most_y_xytext=(45, 0),
                                   reference_xytext=(-75, 25), color_list=None):
    '''
    Create a first order (linear) scatter plot assuming the data frame
    has a index called Country or something
    '''
    fig_width = 18
    fig_height = fig_width/aspect_ratio
    fig = plt.figure(figsize=(fig_width, fig_height))
    ax = fig.add_subplot(111, autoscale_on=True)
    line_kws = dict(c='k', zorder=1, alpha=.25)
    if color_list is None:
        scatter_kws = dict(s=30, lw=.5, edgecolors='k', zorder=2)
    else:
        scatter_kws = dict(s=30, lw=.5, edgecolors='k', zorder=2, color=color_list)
    merge_axes_subplot = sns.regplot(x=xname, y=yname, scatter=True, data=df, ax=ax,
                                     scatter_kws=scatter_kws, line_kws=line_kws)
    if not xlabel_str.endswith(' (explanatory variable)'):
        xlabel_str = '{} (explanatory variable)'.format(xlabel_str)
    xlabel_text = plt.xlabel(xlabel_str)
    if not ylabel_str.endswith(' (response variable)'):
        ylabel_str = '{} (response variable)'.format(ylabel_str)
    ylabel_text = plt.ylabel(ylabel_str)
    kwargs = dict(textcoords='offset points', ha='left', va='bottom',
                  bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
                  arrowprops=dict(arrowstyle='->',
                                  connectionstyle='arc3,rad=0'))
    
    xdata = df[xname].values
    least_x = xdata.min()
    most_x = xdata.max()
    
    ydata = df[yname].values
    most_y = ydata.max()
    least_y = ydata.min()
    
    least_x_tried = most_x_tried = least_y_tried = most_y_tried = False
    for label, x, y in zip(df.index, xdata, ydata):
        if (x == least_x) and not least_x_tried:
            annotation = plt.annotate('{} (least {})'.format(label, x_adj),
                                      xy=(x, y), xytext=least_x_xytext, **kwargs)
            least_x_tried = True
        elif (x == most_x) and not most_x_tried:
            annotation = plt.annotate('{} (most {})'.format(label, x_adj),
                                      xy=(x, y), xytext=most_x_xytext, **kwargs)
            most_x_tried = True
        elif (y == least_y) and not least_y_tried:
            annotation = plt.annotate('{} (least {})'.format(label, y_adj),
                                      xy=(x, y), xytext=least_y_xytext, **kwargs)
            least_y_tried = True
        elif (y == most_y) and not most_y_tried:
            annotation = plt.annotate('{} (most {})'.format(label, y_adj),
                                      xy=(x, y), xytext=most_y_xytext, **kwargs)
            most_y_tried = True
        elif (label == idx_reference):
            annotation = plt.annotate('{} ({})'.format(label, annot_reference),
                                      xy=(x, y), xytext=reference_xytext, **kwargs)
    title_obj = fig.suptitle(t=title, x=0.5, y=0.91)
    
    # Get r squared value
    inf_nan_mask = get_inf_nan_mask(xdata, ydata)
    pearsonr_tuple = pearsonr(xdata[inf_nan_mask], ydata[inf_nan_mask])
    pearson_r = pearsonr_tuple[0]
    pearsonr_statement = str('%.2f' % pearson_r)
    coefficient_of_determination_statement = str('%.2f' % pearson_r**2)
    p_value = pearsonr_tuple[1]
    if p_value < 0.0001:
        pvalue_statement = '<0.0001'
    else:
        pvalue_statement = '=' + str('%.4f' % p_value)
    s_str = r'$r^2=' + coefficient_of_determination_statement + ',\ p' + pvalue_statement + '$'
    text_tuple = ax.text(0.75, 0.9, s_str, alpha=0.5, transform=ax.transAxes, fontsize='x-large')
    
    return fig

def save_fig_as_various(fig, chart_name, verbose=False):
    """
    save_fig_as_various(fig, 'relative_search_strength_of_unprecedented', verbose=True)
    """
    for dir_name in ['pgf', 'png', 'svg']:
        try:
            dir_path = os.path.join('../saves', dir_name)
            os.makedirs(name=dir_path, exist_ok=True)
            file_path = os.path.join(dir_path, '{}.{}'.format(chart_name, dir_name))
            if os.path.exists(file_path):
                os.remove(file_path)
            if verbose:
                print('Saving plot to {}'.format(os.path.abspath(file_path)))
            fig.savefig(file_path, bbox_inches='tight')
        except Exception as e:
            message = str(e).strip()
            print(message)

def get_color_cycler(n):
    """
    color_cycler = get_color_cycler(len(possible_cause_list))
    for possible_cause, face_color_dict in zip(possible_cause_list, color_cycler()):
        face_color = face_color_dict['color']
    """
    color_cycler = None
    if n < 9:
        color_cycler = cycler('color', plt.cm.Accent(np.linspace(0, 1, n)))
    elif n < 11:
        color_cycler = cycler('color', plt.cm.tab10(np.linspace(0, 1, n)))
    elif n < 13:
        color_cycler = cycler('color', plt.cm.Paired(np.linspace(0, 1, n)))
    else:
        color_cycler = cycler('color', plt.cm.tab20(np.linspace(0, 1, n)))
    
    return color_cycler

def ball_and_chain(ax, index, values, c):
    """
    colormap = r()
    cmap = mpl.cm.get_cmap(colormap)
    norm = LogNorm(vmin=values.min(), vmax=values.max())
    ball_and_chain(ax, index, values, c=cmap(norm(values)))
    """
    ax.plot(index, values, c='k', zorder=1, alpha=.25)
    ax.scatter(index, values, s=30, lw=.5, c=c, edgecolors='k', zorder=2)

def get_inf_nan_mask(x_list, y_list):
    x_mask = np.logical_and(np.logical_not(np.isinf(x_list)), np.logical_not(np.isnan(x_list)))
    y_mask = np.logical_and(np.logical_not(np.isinf(y_list)), np.logical_not(np.isnan(y_list)))
    
    return np.logical_and(x_mask, y_mask)