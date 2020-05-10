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
            if node.name is not None:
                t.write(node.name+'--'+str(node.weight), align="center")
            else:
                t.write(str(node.weight), align="center")
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
class Node:
    def __init__(self, name, weight):
        self.name = name #节点名
        self.weight = weight #节点权重
        self.left = None #节点左孩子
        self.right = None #节点右孩子
        self.father = None # 节点父节点
    #判断是否是左孩子
    def is_left_child(self):
        return self.father.left == self

#创建最初的叶子节点
def create_prim_nodes(data_set1, labels1):
    if len(data_set1) != len(labels1):
        raise Exception('数据和标签不匹配!')
    nodes2 = []
    for i in range(len(labels1)):
        nodes2.append( Node(labels1[i],data_set1[i]) )
    return nodes2


# 创建huffman树
def create_HF_tree(nodes1):
    #此处注意，copy()属于浅拷贝，只拷贝最外层元素，内层嵌套元素则通过引用，而不是独立分配内存
    tree_nodes = nodes1.copy()
    while len(tree_nodes) > 1: #只剩根节点时，退出循环
        tree_nodes.sort(key=lambda node: node.weight)#升序排列
        new_left = tree_nodes.pop(0)
        new_right = tree_nodes.pop(0)
        new_node = Node(None, (new_left.weight + new_right.weight))
        new_node.left = new_left
        new_node.right = new_right
        new_left.father = new_right.father = new_node
        tree_nodes.append(new_node)
    tree_nodes[0].father = None #根节点父亲为None
    return tree_nodes[0] #返回根节点

#获取huffman编码
def get_huffman_code(nodes1):
    codes1 = {}
    for node in nodes1:
        code=''
        name = node.name
        while node.father is not None:
            if node.is_left_child():
                code = '0' + code
            else:
                code = '1' + code
            node = node.father
        codes1[name] = code
    return codes1


if __name__ == '__main__':
    labels = ['a','b','c','d','e','f','g','h']
    data_set = [10, 8, 25, 4, 13, 12,2,26]
    nodes = create_prim_nodes(data_set,labels)#创建初始叶子节点
    hf_root = create_HF_tree(nodes)#创建huffman树
    codes = get_huffman_code(nodes)#获取huffman编码
    #打印huffman码
    for key in codes.keys():
        print(key,': ',codes[key])
    #画出huffman树
    draw_tree(hf_root)
    #计算WPL
    print("WPL:",sum([data_set[labels.index(k)]*len(codes[k]) for k in codes.keys()]))
