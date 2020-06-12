// Question 1
const showNumbers = (limit)=> {
  for (let i = 0; i <= limit; i++) {
    if ((i%2)=== 0) {
      console.log(`${i} EVEN`);
    } else {
      console.log(`${i} ODD`);
    }
  }
}
showNumbers(10)

// Question 2
const showStars =  (length) => {
  var star = "";
  for (var i = 1; i <= length; i++) {
    for (var j = 1; j <= i; j++) {
      star += "* "
    }
    star += "\n";
  }
  return star
}
console.log(showStars(10))

// Question 3
const myFunc = (limit) => {
  let res = 0;
  for (var i = 0; i <= limit; i++) {
    if ((i%3 === 0) || (i%5 === 0)) {
      console.log(i);
      res +=1;
    }
  }
}
myFunc(20)
