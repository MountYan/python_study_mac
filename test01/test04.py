def levelOrderBottom(root):
    stack = [root]
    ret = []
    while stack:
        record = []
        next_stack = []
        for node in stack:
            if not node:
                continue
            record.append(node.val)
            next_stack.append(node.left)
            next_stack.append(node.right)
        if record:
            ret.append(record)
        stack = next_stack
    return ret[::-1]
