class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

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

# def TreeDepth(pRoot):
#     if pRoot == None:
#         return 0
#     TreeDepth(pRoot.left)
#     TreeDepth(pRoot.right)
#     return max(TreeDepth(pRoot.left),TreeDepth(pRoot.right))+1


def maxDepth(root):
    if root == None:
        return 0
    DL = maxDepth(root.left)
    DR = maxDepth(root.right)
    return max(DL, DR) + 1

count = 0
proot = createTree()
print(maxDepth(proot))