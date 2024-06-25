某公司出钱冠名了一场线上赛，没有直播，没有任何监督。预赛阶段选出800人。比赛结束公布的排名中，在一众王者玩家之间，出现了一个青铜（对应中考数学没做完，上了中专），排名12。已知：青铜没有参加过任何其他比赛，但是有一个王者师傅，多次参加了这个比赛，而且都晋级了。 怀疑这个王者师傅代打难道不是正常人应该有的的想法吗？

随着事情的不断发酵，大家还发现
- 青铜选手在线下宣传片中屡次出现eq二连放成qe二连的低级错误
- 青铜选手在青铜级别的练习赛中出现了补兵漏一半的情况
- 王者师傅在去年的比赛中有作弊嫌疑





超凡的主张需要有超凡的证据，想要证明青铜有王者的实力，线下比赛看看操作。

class TreeNode:
    __slots__ = ['l','r','val','lazy']
    def __init__(self, val=0):
        self.l = -1 # 区间左端点
        self.r = -1
        self.val = val
        self.lazy = 0

def lc(p): #p是节点编号
    return 2*p+1

def rc(p):
    return 2*p+2

class SegmentTree:
    def __init__(self, size, a=None):
        self.size = size
        self.a = a # 初始值
        self.merge_function = max # 修改：如何合并左右孩子的值
        self.tree = [TreeNode() for i in range(size*4)]
        self.build(0,0,self.size-1) 

    # 从编号为p的节点的左孩子和右孩子，向上更新p的区间值
    def pushup(self, p):
        self.tree[p].val = self.merge_function(self.tree[lc(p)].val, self.tree[rc(p)].val)
    
    def addtag(self, p, val):
        self.tree[p].lazy = val
        self.tree[p].val = self.merge_function(self.tree[p].val, val)

    def pushdown(self,p):
        lazy = self.tree[p].lazy
        if lazy:   # 有lazy标记，这是以前做区间修改时留下的, 需要传递给左右孩子
            self.addtag(lc(p), lazy)
            self.addtag(rc(p), lazy)
            self.tree[p].lazy = 0
        
    # 建树，p是节点编号，指向区间[l,r]
    def build(self, p, l, r):
        self.tree[p].l = l
        self.tree[p].r = r
        if l == r: # leaf
            self.tree[p].val = self.a[l] if self.a else 0
            return
        mid = l+r>>1
        self.build(lc(p),l,mid)
        self.build(rc(p),mid+1,r)
        self.pushup(p)

    # 区间修改，将[L,R]的值变为val, 调用时从根节点，p=0
    def update(self, p, L, R, val):
        if L<=self.tree[p].l and self.tree[p].r<=R: 
            self.addtag(p, val)
            return
        self.pushdown(p)  #如果[l,R]不能完全覆盖p的区间，需要向下传递tag
        mid = self.tree[p].l + self.tree[p].r >> 1
        if L <= mid: self.update(lc(p), L, R, val)
        if mid < R:  self.update(rc(p), L, R, val)
        self.pushup(p)  

    # 返回当前节点代表的区间与查询区间[L,R]交集的区间值
    def query(self,p,L,R):
        if L <= self.tree[p].l and self.tree[p].r <= R: return self.tree[p].val
        self.pushdown(p)
        mid = self.tree[p].l + self.tree[p].r >> 1
        res_left = res_right = 0 # 修改：视题目修改
        if L <= mid: res_left = self.query(lc(p), L, R)
        if R > mid: res_right = self.query(rc(p), L, R)
        return self.merge_function(res_left,res_right)