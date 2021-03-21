import numpy as np


def check_accuracy(
        model,
        k: int,
        x: np.ndarray,
        y: np.ndarray,
        header=None
):
    total_accuracy = 0.0
    root = None
    p = np.random.permutation(len(y))
    x_shuffled, y_shuffled = x[p], y[p]
    x_batches = np.array_split(x_shuffled, k)
    y_batches = np.array_split(y_shuffled, k)

    for i in range(k):
        print(f'    k-fold iteration: {i + 1}/{k} ', end='', flush=True)
        x_test, y_test = x_batches[i], y_batches[i]
        x_train = np.vstack([batch for j, batch in enumerate(x_batches) if j != i])
        y_train = np.hstack([batch for j, batch in enumerate(y_batches) if j != i])

        if header is not None:
            model.fit(x_train, y_train, h=header)
            accuracy = 1 - model.eval(x_test, y_test, header)
            print(f'accuracy {100 * accuracy:.3f}%')
        else:
            model.fit(x_train, y_train)
            accuracy = 1 - model.eval(x_test, y_test)
            print(f'accuracy {100 * accuracy:.3f}%')

        total_accuracy += accuracy
        root = model.root if hasattr(model, 'root') else None

    return total_accuracy / k, root
