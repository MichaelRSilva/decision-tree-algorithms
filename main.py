import numpy as np
import random

import config
from algorithms.cart.cart_executor import run_cart
from algorithms.edt.edt_executor import run_edt
from algorithms.id3.id3_executor import run_id3
from utils.input_util import read_data

if __name__ == '__main__':

    x, y, h = read_data()

    # run_cart(x, y, h)
    # run_edt(x, y, h)
    run_id3(x, y, h)
