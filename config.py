dataset_path = './datasets/landing_club.csv'
algorithm_config = {
    "cart": {
        "path_output_image": './outputs/cart_decision_tree.png',
        "class_names": ["NAO", "SIM"],
        "plot": False
    },
    "brute": {
        "value_true": 11,
        "value_false": 10,
        "max_cols": 5,
        "max_data": 200,
        "print": False
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
run_config = {
    "algorithm": "brute",
    "recurrence": 11,
    "create_csv": True
}
