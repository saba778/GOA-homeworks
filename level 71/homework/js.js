// 1.მოცემულია მასივი:
// const fruits = ["Apple", "Banana", "Orange", "Kiwi"];
// forEach-ით დაბეჭდე თითოეული ხილი.


const fruits = ["Apple", "Banana", "Orange", "Kiwi"]

let fruitr = fruits.forEach(fruit => {
    console.log(fruit)
});

// 2.მოცემულია მასივი:
// const numbers = [2, 4, 6, 8, 10];
// forEach-ით დაბეჭდე თითოეული რიცხვი ×2.

const numbers = [2, 4, 6, 8, 10]

let mumber2 = numbers.forEach(numb =>{
    console.log(numb * 2)
})

// 3.მოცემულია მასივი:
// const names = ["gio", "vano", "nika", "ana"];
// forEach-ით დაბეჭდე ყველა სახელი დიდი ასოებით.

const names = ["gio", "vano", "nika", "ana"]

let bigletter = names.forEach(name =>{
    console.log(name.toUpperCase())
})

// 4.მოცემულია მასივი:
// const prices = [15, 30, 20, 45];
// forEach-ით გამოთვალე ყველა ელემენტის ჯამი.

const prices = [15, 30, 20, 45]

let total = 0

let allprice = prices.forEach(price =>{
  total += price
})


// 5.მოცემულია მასივი:
// const nums = [1, 2, 3, 4, 5, 6, 7, 8];
// forEach-ით დაბეჭდე მხოლოდ ლუწი რიცხვები.

const nums = [1, 2, 3, 4, 5, 6, 7, 8]

let evennumbers = nums.forEach(num => {
    if(num % 2 == 0){
        console.log(num)
    }
})

// 6.მოცემულია მასივი:
// const colors = ["Red", "Blue", "Green"];
// forEach-ით დაბეჭდე ინდექსი და ელემენტი.

const colors = ["Red", "Blue", "Green"]

let number6 = colors.forEach((El,index) =>{
    console.log(index,El)
})


// 7.მოცემულია მასივი:
// const words = ["JavaScript", "HTML", "CSS", "React"];
// forEach-ით დაბეჭდე თითოეული სიტყვა და მისი სიგრძე.

const words = ["JavaScript", "HTML", "CSS", "React"]

let number7 = words.forEach(word =>{
    console.log(word,word.length)
})

// 8.მოცემულია მასივი:
// const ages = [12, 18, 25, 16, 30, 21];
// forEach-ით დაბეჭდე მხოლოდ 18 ან მეტი ასაკი.

const ages = [12, 18, 25, 16, 30, 21]

let number8 = ages.forEach(elem => {
    if(elem >= 18){
        console.log(elem)
    }
})

// 9.მოცემულია მასივი:
// const numbers = [1, 2, 3, 4, 5];
// forEach-ით შექმენი ახალი მასივი, სადაც ყველა რიცხვი კვადრატშია.

const numbers2 = [1, 2, 3, 4, 5]
let numb2 = []
let number9 = numbers2.forEach(numbs => {
    numb2.push(numbs**2)
})

// 10.მოცემულია მასივი:
// const users = [
//   { name: "Gio", age: 20 },
//   { name: "Ana", age: 17 },
//   { name: "Nika", age: 25 }
// ];
// forEach-ით დაბეჭდე თითოეული მომხმარებლის სახელი და ასაკი.
 
const users = [
   { name: "Gio", age: 20 },
   { name: "Ana", age: 17 },
   { name: "Nika", age: 25 }
]

let number10 = users.forEach(namesofpeop =>{
    console.log(namesofpeop.name)
    console.log(namesofpeop.age)
})