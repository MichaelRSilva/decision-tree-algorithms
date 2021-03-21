import numpy as np


# def print_tree(node, y_name, no_name, label_name, attr_name, header: np.array, is_root=True):
#     if node is not None:
#         if is_root:
#             lines, *_ = print_tree(node, y_name, no_name, label_name, attr_name, header, False)
#             for line in lines:
#                 print(line)
#         else:
#             if (node is not None) and getattr(node, no_name) is None and getattr(node, y_name) is None:
#                 line = '%s' % "[" + header[-1] + " = " + str(getattr(node, label_name)) + "]"
#                 width = len(line)
#                 height = 1
#                 middle = width // 2
#                 return [line], width, height, middle
#             left, n, p, x = print_tree(getattr(node, no_name), y_name, no_name, label_name, attr_name, header, False)
#             right, m, q, y = print_tree(getattr(node, y_name), y_name, no_name, label_name, attr_name, header, False)
#             s = '%s' % header[int(getattr(node, attr_name))]
#             u = len(s)
#             first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
#             second_line = x * ' ' + '0' + (n - x - 1 + u + y) * ' ' + '1' + (m - y - 1) * ' '
#             if p < q:
#                 left += [n * ' '] * (q - p)
#             elif q < p:
#                 right += [m * ' '] * (p - q)
#             zipped_lines = zip(left, right)
#             lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
#             return lines, n + m + u, max(p, q) + 2, n + u // 2


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
        x_test, y_test = x_batches[i], y_batches[i]
        x_train = np.vstack([batch for j, batch in enumerate(x_batches) if j != i])
        y_train = np.hstack([batch for j, batch in enumerate(y_batches) if j != i])

        if header is not None:
            model.fit(x_train, y_train, h=header)
            accuracy = 1 - model.eval(x_test, y_test, header)
        else:
            model.fit(x_train, y_train)
            accuracy = 1 - model.eval(x_test, y_test)

        total_accuracy += accuracy
        root = model.root if hasattr(model, 'root') else None

    return total_accuracy / k, root
