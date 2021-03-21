dataset_path = './datasets/landing_club.csv'
algorithm_config = {
    "cart": {
        "path_output_image": './outputs/cart_decision_tree.png',
        "class_names": ["NAO", "SIM"]
    },
    "brute": {
        "value_true": 11,
        "value_false": 10,
        "max_cols": 8,
        "max_data": 500
    }
}
landing_club_config = {
    "from_dataset_path": './datasets/accepted_2007_to_2018Q4-1000.csv',
    "to_dataset_path": './datasets/landing_club.csv',
    "true_value": 11,
    "false_value": 10,
    "true_label": "EM DIA",
    "false_label": "EM ATRASO"
}
