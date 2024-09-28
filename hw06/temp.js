function f2c() {
    let a = document.getElementById('inputA').value;
    document.getElementById("valueA").innerHTML = a;
    document.getElementById("resultA").innerHTML = ((Number(a)-32) * 5 / 9).toFixed(1);
}

function c2f(){
    let b = document.getElementById('inputB').value;
    document.getElementById("valueB").innerHTML = b;
    document.getElementById("resultB").innerHTML = ((Number(b) * 9 / 5) + 32).toFixed(1);
}