

function euler1(a, b, c) {
    var total = 0;
    for(var idx=0; idx<c; idx++){
        if(idx % a == 0 || idx %b == 0){
            total += idx;
        }
    }
    return total;
}

console.log(euler1(3,5,1000));



