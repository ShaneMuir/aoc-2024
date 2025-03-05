def createXmasTree(height, ornament):
    the_tree = []
    total_width = (height * 2 - 1)
    for i in range(height):
        special_characters = 2 * i + 1
        underscores_ = int((total_width - special_characters) / 2)
        tree_line = "_" * underscores_ + ornament * special_characters + "_" * underscores_
        the_tree.append(tree_line)

    trunk_underscores = (total_width - 1) // 2

    trunk_line = "_" * trunk_underscores + "#" + "_" * trunk_underscores
    the_tree.append(trunk_line)
    the_tree.append(trunk_line)

    return '\n' . join(the_tree)


tree = createXmasTree(5, '*')
print(tree)
