import numpy as np
import babypandas as bpd
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
plt.style.use('ggplot')

np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option("display.max_rows", 7)
pd.set_option("display.max_columns", 8)
pd.set_option("display.precision", 2)

from ipywidgets import widgets
from IPython.display import clear_output, display

import warnings
warnings.filterwarnings('ignore')

def standard_units(col):
    return (col - col.mean()) / np.std(col)

def standardize(df):
    """Return a DataFrame in which all columns of df are converted to standard units."""
    df_su = bpd.DataFrame()
    for column in df.columns:
        df_su = df_su.assign(**{column + ' (su)': standard_units(df.get(column))})
    return df_su

def calculate_r(df, x, y):
    '''Returns the average value of the product of x and y, 
       when both are measured in standard units.'''
    x_su = standard_units(df.get(x))
    y_su = standard_units(df.get(y))
    return (x_su * y_su).mean()

def slope(df, x, y):
    '''Returns the slope of the regression line between columns x and y in df (in original units).'''
    r = calculate_r(df, x, y)
    return r * np.std(df.get(y)) / np.std(df.get(x))

def intercept(df, x, y):
    '''Returns the intercept of the regression line between columns x and y in df (in original units).'''
    return df.get(y).mean() - slope(df, x, y) * df.get(x).mean()

# All of the following code is for visualization.
def plot_regression_line(df, x, y, margin=.02, alpha=1, resid=False):
    '''Computes the slope and intercept of the regression line between columns x and y in df (in original units) and plots it.'''
    m = slope(df, x, y)
    b = intercept(df, x, y)
    
    df.plot(kind='scatter', x=x, y=y, s=50, figsize=(10, 5), label='original data', alpha=alpha)
    left = df.get(x).min()*(1 - margin)
    right = df.get(x).max()*(1 + margin)
    domain = np.linspace(left, right, 10)
    plt.plot(domain, m*domain + b, color='orange', label='regression line', lw=4)
    plt.suptitle(format_equation(m, b), fontsize=18)
    plt.legend();
    
    if resid:
        idx = np.random.randint(0, mom_son_predictions.shape[0], size=50)
        for i, k in enumerate(idx):
            x = mom_son_predictions.get('mom').iloc[k]
            y = mom_son_predictions.get('son').iloc[k]
            p = mom_son_predictions.get('predicted').iloc[k]
            plt.plot([x,x], [y,p], linewidth=3, color='purple', label='residuals' if i == 0 else None)
        plt.legend();
        print('Correlation:', calculate_r(mom_son, 'mom', 'son'))
        
def non_linear():
    np.random.seed(23)
    x2 = bpd.DataFrame().assign(
    x=np.arange(-6, 6.1, 0.5) + np.random.normal(size=25), 
    y=np.arange(-6, 6.1, 0.5)**2 + np.random.normal(size=25)
    )
    plot_regression_line(x2, 'x', 'y')

def format_equation(m, b):
    if b > 0:
        return r'$y = %.2fx + %.2f$' % (m, b)
    elif b == 0:
        return r'$y = %.2fx' % m
    else:
        return r'$y = %.2fx %.2f$' % (m, b)
    
# Don't worry about how this code works.
def pred_interval(mom):
    plt.figure(figsize=(10, 5))
    x = np.arange(50, 80)
    ys = []
    for i, (m, b) in enumerate(zip(m_boot[:50], b_boot)):
        ys.append(m * x + b)
        plt.plot(x, m * x + b, linewidth=1, alpha=0.1)  
        
    boot_preds = m_boot * mom + b_boot
    l = np.percentile(boot_preds, 2.5)
    r = np.percentile(boot_preds, 97.5)
    plt.plot([mom, mom], [l, r], linewidth=5, color='#eb7e35', label='95% prediction interval')
    plt.xlim(50, 80)
    plt.ylim(62, 77)
    plt.title(f'95% prediction interval for the height of a son whose mother is {mom} inches tall: {[np.round(l, 3), np.round(r, 3)]}')
    plt.legend()
    plt.show()

def slider_widget():
    mom_slider = widgets.IntSlider(value=64, min=50, max=78, step=1, description="mom's height")
    ui = widgets.HBox([mom_slider])
    out = widgets.interactive_output(pred_interval, {'mom': mom_slider})
    display(ui, out)
    
def draw_many_lines(m_boot, b_boot):
    plt.figure(figsize=(10, 5))
    x = np.arange(50, 80)
    ys = []
    for i, (m, b) in enumerate(zip(m_boot[:50], b_boot)):
        ys.append(m * x + b)
        fig = plt.plot(x, m * x + b, linewidth=1)  