maxi = float("-inf")

def max_path_sum(root):
    global maxi
    if not root:
        return 0
    left = max(max_path_sum(root.left), 0)
    right = max(max_path_sum(root.right), 0)
    maxi = max(maxi, root.val + left + right)
    return root.val + max(left, right)