import LowestCommonAncestor

root = LowestCommonAncestor.Node(1) 
root.left = LowestCommonAncestor.Node(2) 
root.right = LowestCommonAncestor.Node(3) 
root.left.left = LowestCommonAncestor.Node(4) 
root.left.right = LowestCommonAncestor.Node(5) 
root.right.left = LowestCommonAncestor.Node(6) 
root.right.right = LowestCommonAncestor.Node(7) 

assert LowestCommonAncestor.findLCA(root, 4, 5) == 2, "Should be 2"
assert LowestCommonAncestor.findLCA(root, 4, 6) == 1, "Should be 1"
assert LowestCommonAncestor.findLCA(root, 4, 9) == -1, "Should be -1"
assert LowestCommonAncestor.findLCA(root, -1, 2) == -1, "Should be -1"
root = None;
assert LowestCommonAncestor.findLCA(root, 4, 6) == -1, "Should be -1 (null root)"