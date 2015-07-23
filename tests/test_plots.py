# -*- coding: utf 8 -*-
"""
Defines a suite a tests for images run with:

    py.test --mpl

https://pypi.python.org/pypi/pytest-mpl/0.3
"""
from striplog import Striplog
from striplog import Legend, Component, Decor

import matplotlib.pyplot as plt
import pytest

args = {'tolerance': 10,
        'savefig_kwargs': {'dpi': 100},
        }


@pytest.mark.mpl_image_compare(**args)
def test_striplog_plot():
    """
    Tests mpl image of striplog
    """
    legend = Legend.default()

    imgfile = "tutorial/M-MG-70_14.3_135.9.png"

    striplog = Striplog.from_img(imgfile, 14.3, 135.9, legend=legend)

    fig = striplog.thickest(n=5).plot(legend=legend)
    return fig


@pytest.mark.mpl_image_compare(**args)
def test_decor_plot():
    """
    Tests mpl image of decor
    """
    r = {'colour': 'grey',
         'grainsize': 'vf-f',
         'lithology': 'sand'}

    rock = Component(r)

    d = {'color': '#86F0B6',
         'component': rock,
         'width': 3}

    decor = Decor(d)

    fig = plt.figure(figsize=(4, 1))
    fig = decor.plot(fmt="{lithology} {colour} {grainsize}", fig=fig)
    return fig