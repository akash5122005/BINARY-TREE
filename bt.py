class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert(root,key):
    if root is None:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
        return root

def build_tree():
    n = int(input())
    elements = list(map(int,input().split()))
    if not elements:
        return None

    root = None
    for element in elements:
        root = insert(root, element)
    print("Tree structure successfully built!")
    return root
def main():
    build_tree()

if __name__ == "__main__":
    main()                                
