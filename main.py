import numpy as np
import random

from config import run_config
from algorithms.brute.brute_executor import run_brute
from algorithms.cart.cart_executor import run_cart
from algorithms.edt.edt_executor import run_edt
from algorithms.id3.id3_executor import run_id3
from utils.input_util import read_data
from utils.landing_club_util import create_csv
from datetime import datetime

if __name__ == '__main__':

    for i in range(1, run_config["recurrence"]):
        time_start = datetime.now()
        x, y, h = read_data()

        if run_config["create_csv"]:
            create_csv()

        if run_config["algorithm"] == 'cart':
            run_cart(x, y, h)
        elif run_config["algorithm"] == 'id3':
            run_id3(x, y, h)
        elif run_config["algorithm"] == 'brute':
            run_brute(x, h)
        else:
            run_edt(x, y, h)

        time_end = datetime.now()
        time_total = (time_end - time_start).total_seconds()
        print('[' + str(i) + '] Time to execute: ' + str(time_total).replace(".", ",") + " seconds | " + str(
            round(time_total / 60)) + " minutes")
