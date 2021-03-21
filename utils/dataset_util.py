# Divide o data set em dois conjuntos
def split(dataset, col, value):
    # testar
    set_right = [row for row in dataset if row[col] == value]
    set_left = [row for row in dataset if not row[col] == value]

    return set_left, set_right


def distinct(data, col):
    values = [row[col] for row in data]
    return list(set(values))
