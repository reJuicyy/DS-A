class Node:
    def __init__(self, leaf=False) -> None:
        self.leaf = leaf
        self.keys = []
        self.child = []
        
class BTree:
    def __init__(self, k) -> None:
        self.root = Node(True)
        self.k = k
        
    def insert(self, item):
        root = self.root
        
        if len(root.keys) == (2 * self.k) - 1:
            tmp = Node()
            self.root = tmp
            tmp.child.insert(0, root)
            self.split(tmp, 0)
            self.insert_non_full(tmp, item)
        else:
            self.insert_non_full(root, item)
    
    def split(self, tmp, i):
        y = tmp.child[i]
        z = Node(y.leaf)
        tmp.child.insert(i + 1, z)
        tmp.keys.insert(i, y.keys[self.k - 1])
        z.keys = y.keys[self.k: (2 * self.k) - 1]
        y.keys = y.keys[0: self.k - 1]
        
        if not y.leaf:
            z.child = y.child[self.k: 2 * self.k]
            y.child = y.child[0: self.k - 1]
    
    def insert_non_full(self, tmp, item):
        i = len(tmp.keys) - 1
        
        if tmp.leaf:
            tmp.keys.append((None, None))
            
            while i >= 0 and item[0] < tmp.keys[i][0]:
                tmp.keys[i + 1] = tmp.keys[i]
                i -= 1
                
            tmp.keys[i + 1] = item
        else:
            while i >= 0 and item[0] < tmp.keys[i][0]:
                i -= 1
            i += 1
            
            if len(tmp.child[i].keys) == (2 * self.k) - 1:
                self.split(tmp, i)
                if item[0] > tmp.keys[i][0]:
                    i += 1
                self.insert_non_full(tmp.child[i], item)
                
    def print_btree(self, tmp, level=0):
        print(f"Level: {level} {len(tmp.keys)}", end=":")
        
        for i in tmp.keys:
            print(i, end=" ")
        print()
        
        level += 1
        
        if len(tmp.child) > 0:
            for i in tmp.child:
                self.print_btree(i, level)