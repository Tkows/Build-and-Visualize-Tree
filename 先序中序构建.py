import turtle
def draw_tree(root):

    def height(head):
        return 1 + max(height(head.left), height(head.right)) if head else -1

    def jump_to(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jump_to(x, y - 20)
            t.write(node.val, align="center")
            draw(node.left, x - dx, y - 60, dx / 2)
            jump_to(x, y - 20)
            draw(node.right, x + dx, y - 60, dx / 2)

    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jump_to(0, 30 * h)
    draw(root, 0, 30 * h, 40 * h)
    t.hideturtle()
    turtle.mainloop()

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None
    if len(preorder) == 0 or len(inorder) == 0:
        return None
    root_val = preorder[0]
    root = TreeNode(root_val)
    mid = inorder.index(root_val)
    root.left = buildTree(preorder[1: mid+1], inorder[0:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root

pre_order = "ABDHECFGI"
in_order = "HDBEAFCGI"
new_tree = buildTree(pre_order,in_order)
draw_tree(new_tree)
