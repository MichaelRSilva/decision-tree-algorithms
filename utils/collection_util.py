from itertools import permutations


def get_data_permutations(data, metadata):
    cols_quantity = len(data[0])
    target_column = [row[cols_quantity - 1] for row in data]
    all_index_permutations = list(permutations(range(cols_quantity - 1)))
    dataset = []
    metas = []

    for options in all_index_permutations:
        matrix = []
        meta = []

        for idx, col in enumerate(list(options)):
            values = [row[col] for row in data]
            matrix.append(values)
            meta.append(metadata[col])

        matrix.append(target_column)
        dataset.append([[row[i] for row in matrix] for i in range(len(matrix[0]))])

        meta.append(metadata[cols_quantity - 1])
        metas.append(meta)

    return dataset, metas
