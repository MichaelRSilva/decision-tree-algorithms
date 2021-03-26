import csv

import numpy as np
import pandas as pd

import config

__columns = [
    'term_greater_36',
    'loan_greater_20k',
    'installment_greater_450',
    'good_grade',
    'job_grater_6',
    'home_owner',
    'annual_pay',
    'rate',
    'is_credit_card',
    'is_debt_consolidation',
    'is_home_improvement',
    'status'
]


def get_gt(value, gt) -> int:
    true_value = config.landing_club_config["true_value"]
    false_value = config.landing_club_config["false_value"]

    if isinstance(value, float) or isinstance(value, int):
        return true_value if value > gt else true_value
    else:
        return false_value if float(''.join(i for i in value if i.isdigit())) > gt else false_value


def get_header() -> np.array:
    with open(config.landing_club_config["from_dataset_path"], newline='') as f:
        reader = csv.reader(f)
        return next(reader)


def create_csv():
    header = get_header()
    df = pd.read_csv(config.landing_club_config["from_dataset_path"], header=1, dtype='unicode')
    df.columns = header

    df['term_greater_36'] = df['term'].apply(lambda val: get_gt(val, 36))
    df['loan_greater_20k'] = df['loan_amnt'].apply(lambda val: get_gt(val, 20000))
    df['installment_greater_450'] = df['installment'].apply(lambda val: get_gt(val, 450))
    df['good_grade'] = df['grade'].apply(lambda val: 11 if val == 'A' or val == 'B' or val == 'C' else 10)
    df['job_grater_6'] = df['emp_length'].apply(lambda val: get_gt(val, 6))
    df['home_owner'] = df['home_ownership'].apply(lambda val: 11 if str(val).upper() == 'OWN' else 10)
    df['annual_pay'] = df['annual_inc'].apply(lambda val: get_gt(val, 70000))
    df['rate'] = df['int_rate'].apply(lambda val: get_gt(val, 6))
    df['status'] = df['loan_status'].apply(
        lambda val: 11 if 'FULL' in str(val).upper() or 'CURRENT' in str(val).upper() else 10)
    df['is_credit_card'] = df['purpose'].apply(lambda val: 11 if val == 'credit_card' else 10)
    df['is_debt_consolidation'] = df['purpose'].apply(lambda val: 11 if 'debt_consolidation' == val else 10)
    df['is_home_improvement'] = df['purpose'].apply(lambda val: 11 if 'home_improvement' == val else 10)

    df.to_csv(path_or_buf=config.landing_club_config["to_dataset_path"], columns=__columns, index=False)
