from algorithms.brute.BruteNode import BruteNode
from utils.dataset_util import distinct, split


def create_display_tree(node: BruteNode):
    if node.left is None and node.right is None:
        line = '%s' % "[" + ((str(node.label) + "=" + str(node.value)) if node.value is not None else str(node.label)) + "]"
        width = len(line)
        height = 1
        middle = width // 2
        return [line], width, height, middle

    left, n, p, x = create_display_tree(node.left)
    right, m, q, y = create_display_tree(node.right)
    s = '%s' % ((str(node.label) + "=" + str(node.value)) if node.value is not None else str(node.label))
    u = len(s)
    first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
    second_line = x * ' ' + '0' + (n - x - 1 + u + y) * ' ' + '1' + (m - y - 1) * ' '
    if p < q:
        left += [n * ' '] * (q - p)
    elif q < p:
        right += [m * ' '] * (p - q)
    zipped_lines = zip(left, right)
    lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
    return lines, n + m + u, max(p, q) + 2, n + u // 2


def print_tree(root):
    lines, *_ = create_display_tree(root)
    for line in lines:
        print(line)


def build_tree(dataset, next_col, value, metadata, index_results, value_false):
    # Divide os dados em dois conjuntos (false,true)
    data_distinct = distinct(dataset, index_results)

    # Se só houver um valor, entao esse eh um no folha
    if len(data_distinct) == 1:
        return BruteNode(metadata[index_results], None, None, data_distinct[0])

    # Condicao de parada para esse ramo da arvore
    if len(dataset) == 0:
        return BruteNode(metadata[index_results], None, None, value_false)

    # Cria os ramos left e right da arvore dependendo do dado dividido
    split_dataset = split(dataset, next_col, value)

    left = build_tree(split_dataset[0], next_col + 1, value, metadata, index_results, value_false)
    right = build_tree(split_dataset[1], next_col + 1, value, metadata, index_results, value_false)

    return BruteNode(metadata[next_col], left=left, right=right)


def depth_tree(node: BruteNode):
    left_depth = depth_tree(node.left) if node.left else 0
    right_depth = depth_tree(node.right) if node.right else 0

    return max(left_depth, right_depth) + 1


def height_tree(root: BruteNode):
    return depth_tree(root) - 1


def size_tree(node: BruteNode):
    if not node:
        return 0
    return 1 + size_tree(node.left) + size_tree(node.right)


def print_min_tree(trees: [BruteNode]):
    min_height = None
    min_size = None
    min_tree = None

    for tree in trees:
        height = height_tree(tree)
        size = size_tree(tree)

        if min_tree is None or (height <= min_height and size <= min_size):
            min_height = height
            min_size = size
            min_tree = tree

    print("")
    print("=================== ARVORE MINIMA =====================")
    print("Altura: " + str(min_height))
    print("Nos: " + str(min_size))
    print("*********************** TREE *************************")
    print_tree(min_tree)


def print_all_min_tree(trees: [BruteNode]):
    height_size_trees = [(int, int, BruteNode)]
    min_height = None
    min_size = None

    for tree in trees:
        height = height_tree(tree)
        size = size_tree(tree)
        height_size_trees.append((height, size, tree))

        if min_height is None or (height <= min_height and size <= min_size):
            min_height = height
            min_size = size

    print("\n")
    print("=================== ARVORES MINIMAS =====================")
    print("Altura: " + str(min_height))
    print("Nos: " + str(min_size))

    for idx, tree in enumerate(list(height_size_trees)):
        if tree[0] == min_height and tree[1] == min_size:
            print("\n")
            print("*********************** TREE [" + str(idx) + "] *************************")
            print("\n")
            print_tree(tree[2])


def print_all_tres(trees: [BruteNode]):
    print("")
    print("================= TODAS AS ARVORES ====================")

    for idx, tree in enumerate(list(trees)):
        print("\n\n")
        print("[*********************** TREE [" + str(idx) + "] *************************")
        print_tree(tree)
        print("*******************************************************]")
