# 전위 순회
def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

# 중위 순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

# 후위 순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

N = int(input())

tree = {}
for _ in range(N):
    root, left_node, right_node = input().split()
    tree[root] = [left_node, right_node]

preorder('A')
print()
inorder('A')
print()
postorder('A')