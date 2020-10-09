class SegmentTree{
    constructor(length){
        this.tree = new Array(2*length-1).fill(0);
        this.LazyTree = new Array(2*length-1).fill(0);
        this.size = 2*length-1;
    }
    update(pos, l, r,currentLeft, currentRight, value){
        
        if(pos<=this.size){
        if(this.LazyTree[pos]>0){
            this.tree[pos] += this.LazyTree[pos];
            if(currentLeft!=currentRight){
                this.LazyTree[2*pos+1] += this.LazyTree[pos];
                this.LazyTree[2*pos+2] += this.LazyTree[pos];
            }
            this.LazyTree[pos] = 0;
        }

        if(currentLeft> currentRight || currentLeft>r || currentRight < l){
            return ;
        }

        //total overlap
        if(currentLeft >= l && currentRight <= r){
            this.tree[pos] += value;
            if(currentLeft!=currentRight){
                this.LazyTree[2*pos+1] += value;
                this.LazyTree[2*pos+2] += value;
            }
            return;
        }
        //partial overlap
        let mid = (currentLeft+currentRight)/2;
        if(2*pos+1 <= this.size)
        this.update(2*pos+1, l, r, currentLeft, mid, value);
        if(2*pos+2 <= this.size)
        this.update(2*pos+2, l, r, mid+1, currentRight, value);
        this.tree[pos] = Math.max((this.tree[2*pos+1])?this.tree[2*pos+1]:0 , (this.tree[2*pos+2])?this.tree[2*pos+2]:0);
    }
    }
    updateWrap(l, r, value){
        this.update(0,l, r, 0, this.size-1, value);
    }
}

function carTrip(arr,capacity){
    let myTree = new SegmentTree(7);
    // arr.forEach(tour=>{
    //     console.log(tour)
    //     myTree.updateWrap(tour[1], tour[2], tour[0]);
    // })
    myTree.updateWrap(3, 5, 4)
    console.log(myTree.tree)
    console.log(myTree.LazyTree)
}
carTrip([[2,1,5],[3,3,7]],4)