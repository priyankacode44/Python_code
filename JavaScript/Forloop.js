let fruits=[apple,banana,grapes];
let x;
for(x in fruits){
    console.log(fruits[x]);    //apple,banana,grapes
    console.log(x);            //0,1,2
}

for( x of fruits){
    console.log(x); //apple,banana,grapes
}


let fruits1=['apple','banana','grapes'];
console.log(fruits1);
fruits1.pop();  // remove last element from array
fruits1.shift(); //remove start element from array
fruits1.unshift('lemon'); // it add lemon into starting index
fruits1.splice(1,2);  // it removes from index 1 to index2 element
fruits1.splice(2,0,'orange','cherry') ///it adds orange and cherry into array


let evennumber=[2,4,6];
let oddnumber=[1,3,5];
let primenumber=[2,3,5]
let number=evennumber.concat(oddnumber,primenumber); // add three array by using concat function
console.log(number);

a=24;



