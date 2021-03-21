import numpy as np
import random

import config
from algorithms.brute.brute_executor import run_brute
from algorithms.cart.cart_executor import run_cart
from algorithms.edt.edt_executor import run_edt
from algorithms.id3.id3_executor import run_id3
from utils.input_util import read_data
from utils.landing_club_util import create_csv
from datetime import datetime

if __name__ == '__main__':

    time_start = datetime.now()
    x, y, h = read_data()

    # create_csv()

    # run_cart(x, y, h)
    # run_edt(x, y, h)
    # run_id3(x, y, h)
    run_brute(x, h)

    time_end = datetime.now()
    time_total = (time_end - time_start).total_seconds()
    print('Time to execute: ' + str(time_total) + " seconds | " + str(round(time_total/60)) + " minutes")
