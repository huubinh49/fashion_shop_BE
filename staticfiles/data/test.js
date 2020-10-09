function projectionArea(arr){
    let colMax= 0;
    let tx = 0;
    for(let i =0 ; i<arr.length;i++){
        colMax = (arr[i].length > colMax)? arr[i].length:colMax;
        tx += arr[i].length;
    }
    let tp = new Array(arr.length).fill(0);
    let st = new Array(colMax).fill(0);
    for(let i = 0; i<arr.length;i++){
        for(let j = 0; j<arr[i].length;j++){
            if(arr[i][j]>tp[i]){
                tp[i] = arr[i][j];
            }
            if(arr[i][j]>st[j]){
                st[j] = arr[i][j];
            }
        }
    }
    return tx+tp.reduce((sum, cur)=> sum+cur, 0)+st.reduce((sum, cur)=> sum+cur, 0);
}
function carTrip(arr,capacity){
    let lengthTour = 0;
    for(let i = 0; i< arr.length;i++){
        if(arr[i][2] > lengthTour)
        lengthTour =arr[i][2];
    }
    tours = new Array(lengthTour+1).fill(0)
    for(let i = 0; i < arr.length;i++){
        tours[arr[i][1]]+=arr[i][0];
        tours[arr[i][2]]-=arr[i][0];
    }

    let current
    for(let i = 0; i<=lengthTour;i++){

        if(tours[i] > capacity){
            return false;
        }
    }
    return true;
}
// carTrip([[2,1,5],[3,3,7]],4);

function goodReverseNumbers(n){
    let count  = 0;
    for(let i = 12; i<=n;i++){
        if(i%10==0) continue;

        let number = i + parseInt((i+"").split("").reverse().join(""));
        let check = number+"";
        let flag = true;
        for(let i = 0; i<check.length; i++){
            if(parseInt(check[i])%2==0){
                flag = false;
            }
        }
        if(flag)
        count++;
    }
    console.log(count)
    
}
for(let i = 1; i<10;i++){
    goodReverseNumbers(1000+(i*1000))
}

goodReverseNumbers(10**9)
