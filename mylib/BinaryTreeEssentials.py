#Binary Tree Essentials

#find height of the tree - length of the longest path from the leaf to the root, #nodes
def findHeight(node):
	if node is None:
		return 0
	lheight = findHeight(node.left)
	rheight = findHeight(node.right)
	return max(lheight,rheight) + 1

#Maximum(Diameter of left sub­tree, Diam­e­ter of right sub­tree, Longest path between two nodes which passes through the root.)
#Naive solution: O(n^2)
def findDiameter1(node):
	if node is None:
		return 0
	lheight = findHeight(node.left)
	rheight = findHeight(node.right)
	return max(lheight+rheight+1 , findDiameter1(node.left),findDiameter1(node.right))

#Optimized solution to find diameter and height together
def findDiameter2(node):
	if node is None:
		return 0,0
	lheight,ldiameter = findDiameter2(node.left)
	rheight,rdiameter = findDiameter2(node.right)
	path = lheight + rheight + 1 #longest path via root
	print("node=%d lh=%d ld=%d rh=%d rd=%d" % (node.data,lheight,ldiameter, rheight,rdiameter))
	d = max(ldiameter,rdiameter,lheight + rheight + 1 )
	h = max(lheight,rheight)+1
	print(node.data,d,h)
	return d,h

#Find max value in a Binary Tree
def findMax(node,nmax):
	if node is None:
		return nmax
	if nmax is None:
		nmax = node.data
	elif node.data > nmax:
		nmax = node.data
	lmax = findMax(node.left,nmax)
	rmax = findMax(node.right,nmax)
	#print("node=%d lmax=%d rmax=%d" % (nmax,lmax,rmax))
	return max(nmax,lmax,rmax)


def isLeaf(node):
    if (node.getLeft() is None and  node.getRight() is None):
        return True
    else:
        return False


#Find all path and sum
#Modified post order traversal
def findPathSum(node,path,psum):
	if node is None:
		return
	path.append(node.data)
	psum += node.data
	findPathSum(node.left,path,psum)
	findPathSum(node.right,path,psum)
	#Important: Path ends in a leaf!
	if node.left is None and node.right is None:
		print(path, psum)
	#Important: pop and remove value on the way back!
	path.pop()
	psum -= node.data

#Clone tree
#Modified pre order traversal
def cloneBT(node):
	if node is None:
		return
	newNode = BinaryTree(node.data)
	newNode.left = cloneBT(node.left)
	newNode.right = cloneBT(node.right)
	return newNode 

#Deepest node: Level order traversal
