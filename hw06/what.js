function num() {

    let numbers = [];

    while (numbers.length < 6) {
        let rand = Math.floor(Math.random() * 45) + 1;

        if (!numbers.includes(rand)) {
            numbers.push(rand);
        }
    }

    console.log(numbers);
    return numbers;
}

function num_start() {
    let result = num();
    alert("행운의 숫자 6개: " + result.join(", "));
}