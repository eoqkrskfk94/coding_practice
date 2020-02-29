def preorder(node):
  print(node.item, end = "")
  if node.left != ".":
    preorder(tree[node.left])
  if node.right != ".":
    preorder(tree[node.right])

def midorder(node):
  if node.left != ".":
    midorder(tree[node.left])
  print(node.item, end = "")
  if node.right != ".":
    midorder(tree[node.right])

def postorder(node):
  if node.left != ".":
    postorder(tree[node.left])
  if node.right != ".":
    postorder(tree[node.right])
  print(node.item, end = "")
  
class Node:
  def __init__(self, item, left, right):
    self.item = item
    self.left = left
    self.right = right

N = int(input())

tree = {}

for i in range(N):
  temp = input().split()
  tree[temp[0]] = Node(item = temp[0] , left = temp[1], right = temp[2])


preorder(tree['A'])
print()
midorder(tree['A'])
print()
postorder(tree['A'])






