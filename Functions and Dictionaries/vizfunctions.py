

import numpy as np
import matplotlib as mpl
from matplotlib import rcParams
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import cycler
from matplotlib.ticker import StrMethodFormatter
from matplotlib.axis import Axis
from matplotlib.patches import FancyBboxPatch
from matplotlib.font_manager import FontProperties

col1, col2, edge1, edge2 = '#00263E', '#E1EFF2', 'vertical', 'horizontal'
def allheaders(col1, col2, edge1, edge2):
    for cell in table.get_children():
        cell_text = cell.get_text().get_text()
        if cell_text not in row_headers\
        and cell_text not in column_headers:
            cell.set_edgecolor(col1)
        else:
            cell.set(edgecolor=col2)
    for cell in table.get_children():
        cell_text = cell.get_text().get_text()
        if cell_text in column_headers:
            cell.visible_edges = edge1
        elif cell_text in row_headers:
            cell.visible_edges = edge2
    for cell in table.get_children():
        cell_text = cell.get_text().get_text()
        if cell_text in row_headers\
        or cell_text in column_headers:
            cell.set_text_props(fontproperties=FontProperties(weight='bold'))


#table color functions
def howwide(width):
    ['None' for x in range(width)]
def howlong(indexlength):
    ["None" for x in range(indexlength)]
TABLECOL1 = '#E1EFF2'
TABLECOL2 = '#F4F9F9'
def tablecolors(indexlength, width):
    if indexlength == 2:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)]]
    if indexlength == 3:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)]]
    if indexlength == 4:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)]]
    if indexlength == 5:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)]]
    if indexlength == 6:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 7:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)]]
    if indexlength == 8:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 9:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)]]
    if indexlength == 10:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 11:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)]]
    if indexlength == 12:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 13:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)]]
    if indexlength == 14:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 15:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)]]
    if indexlength == 16:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 17:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)]]
    if indexlength == 18:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 19:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)]]
    if indexlength == 20:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 21:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)]]
    if indexlength == 22:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 23:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)]]
    if indexlength == 24:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)]]
    if indexlength == 25:
        return [[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],[TABLECOL1 for x in range(width)],[TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)], [TABLECOL1 for x in range(width)], [TABLECOL2 for x in range(width)],
               [TABLECOL1 for x in range(width)]]

#table formatting for merged table function
col1, col2, edge1, edge2 = '#00263E', '#E1EFF2', 'vertical', 'horizontal'
def allheadersmerged(col1, col2, edge1, edge2):
    for cell in table.get_children():
        cell_text = cell.get_text().get_text()
        if cell_text not in row_headers\
        and cell_text not in doublecols:
            cell.set_edgecolor(col1)
        elif cell_text in column_headers:
            cell.set_edgecolor(None)
        else:
            cell.set(edgecolor=col2)
        if cell_text in column_headers:
            cell.visible_edges = 'B'
        elif cell_text in row_headers:
            cell.visible_edges = edge2
        elif cell_text in col_names:
            cell.visible_edges = 'LR'
        if cell_text in row_headers\
        or cell_text in doublecols:
            cell.set_text_props(fontproperties=FontProperties(weight='bold'))
#function to make figure invisible for tables
guy1, guy2, guy3 = False, 'off', 'tight'
def makeinvisible(guy1, guy2, guy3):
    return fig.patch.set_visible(guy1), ax.axis(guy2), ax.axis(guy3)


#merge two cells function
def mergecells(table, ix0, ix1):
    ix0,ix1 = np.asarray(ix0), np.asarray(ix1)
    d = ix1 - ix0
    if not (0 in d and 1 in np.abs(d)):
        raise ValueError("ix0 and ix1 should be the indices of adjacent cells. ix0: %s, ix1: %s" % (ix0, ix1))
    if d[0]==-1:
        edges = ('BRL', 'TRL')
    elif d[0]==1:
        edges = ('TRL', 'BRL')
    elif d[1]==-1:
        edges = ('BTR', 'BTL')
    else:
        edges = ('BTL', 'BTR')
    # hide the merged edges
    for ix,e in zip((ix0, ix1), edges):
        table[ix[0], ix[1]].visible_edges = e
    txts = [table[ix[0], ix[1]].get_text() for ix in (ix0, ix1)]
    tpos = [np.array(t.get_position()) for t in txts]
    # center the text of the 0th cell between the two merged cells
    trans = (tpos[1] - tpos[0])/2
    if trans[0] > 0 and txts[0].get_ha() == 'right':
        # reduce the transform distance in order to center the text
        trans[0] /= 2
    elif trans[0] < 0 and txts[0].get_ha() == 'right':
        # increase the transform distance...
        trans[0] *= 2
    txts[0].set_transform(mpl.transforms.Affine2D().translate(*trans))
    # hide the text in the 1st cell
    txts[1].set_visible(False)
#merge multiple cells function
def mergemultcells(table, cells):
    cells_array = [np.asarray(c) for c in cells]
    h = np.array([cells_array[i+1][0] - cells_array[i][0] for i in range(len(cells_array) - 1)])
    v = np.array([cells_array[i+1][1] - cells_array[i][1] for i in range(len(cells_array) - 1)])
    # if it's a horizontal merge, all values for `h` are 0
    if not np.any(h):
        # sort by horizontal coord
        cells = np.array(sorted(list(cells), key=lambda v: v[1]))
        edges = ['BTL'] + ['BT' for i in range(len(cells) - 2)] + ['BTR']
    elif not np.any(v):
        cells = np.array(sorted(list(cells), key=lambda h: h[0]))
        edges = ['TRL'] + ['RL' for i in range(len(cells) - 2)] + ['BRL']
    else:
        raise ValueError("Only horizontal and vertical merges allowed")
    for cell, e in zip(cells, edges):
        table[cell[0], cell[1]]
#stacked bar labels function
belowstackedbarlabels, abovestackedbarlabels = -5, 2
def stackedbarlabels(locationoffset):
    for bar in ax.patches:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + bar.get_y() + locationoffset, str(float(round(bar.get_height(), 1))) + '%', ha='center')
#rounded boxes for stacked bars
boxstyleinput = "round,pad=-0.060,rounding_size=0.15"
def roundedboxes(boxstyleinput):
    new_patches = []
    for patch in reversed(ax.patches):
        bb = patch.get_bbox()
        color=patch.get_facecolor()
        p_bbox = FancyBboxPatch((bb.xmin, bb.ymin),abs(bb.width), abs(bb.height),boxstyle=boxstyleinput, ec="none", fc=color, mutation_aspect=1)
        patch.remove()
        new_patches.append(p_bbox)
    for patch in new_patches:
        ax.add_patch(patch)
