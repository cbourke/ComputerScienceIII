
console.log("Hello World");
console.log("You passed:");

process.argv.forEach(function (val, index, array) {
    console.log(index + ': ' + val);
});
