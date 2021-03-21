dataset_path = './datasets/financial_test.csv'
algorithm_config = {
    "cart": {
        "path_output_image": './outputs/cart_decision_tree.png',
        "class_names": ["NAO", "SIM"]
    }
}
landing_club_config = {
    "from_dataset_path": '../datasets/accepted_2007_to_2018Q4-200.csv',
    "to_dataset_path": '../datasets/landing_club.csv',
    "true_value": 11,
    "false_value": 10,
    "true_label": "EM DIA",
    "false_label": "EM ATRASO"
}
