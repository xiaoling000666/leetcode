class TreeNode(object):
    '''
    二叉树类
    '''

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def createTree():
    '''
    创建二叉树函数
    '''
    # 创建如图的二叉树
    # 1.创建节点
    A = TreeNode('A')
    B = TreeNode('B')
    C = TreeNode('C')
    D = TreeNode('D')
    E = TreeNode('E')
    F = TreeNode('F')
    # 列表解析
    # A, B, C, D, E, F = [TreeNode(x) for x in 'ABCDEF']

    # 2.创建节点之间的关系
    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F
    return A

def preOrder(node):
    if node is None:
        return
    preOrder(node.left)
    preOrder(node.right)
    print(node.data)

if __name__ == '__main__':
    # 二叉树的创建
    root = createTree()
    # 二叉树的遍历
    preOrder(root)

