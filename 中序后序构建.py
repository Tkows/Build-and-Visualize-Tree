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
def buildTree(inorder, postorder) :
    if not inorder:
        return None
    root = TreeNode(postorder[-1])
    i = inorder.index(root.val)
    root.left = buildTree(inorder[:i], postorder[:i])
    root.right = buildTree(inorder[i + 1:], postorder[i:-1])

    return root

in_order = "BDCEAFHG"
post_order = "DECBHGFA"
new_tree = buildTree(in_order,post_order)
draw_tree(new_tree)