// 1) თქვენი სიტყვებით ახსენით რა არის higher order functions


// higher order functions არის ფუნქცია რომელიც ფუნქციას იღებს არგუმენტად


// 2)პირობა: შექმენი ორი ცალკეული ფუნქცია:

// sayHello(name) — იღებს სახელს და აბრუნებს ტექსტს: "გამარჯობა, [name]!".

// processUser(name, callback) — იღებს სახელს და callback ფუნქციას.

// დავალება: processUser ფუნქციამ შიგნით უნდა გამოიძახოს გადაცემული callback ფუნქცია (ანუ sayHello), გადასცეს მას name და დაბრუნებული შედეგი დაბეჭდოს კონსოლში (console.log).


function sayHello(name) {
    console.log('გამარჯობა, ${name}!')
}


function processUser(name, greet){
    name = prompt()
    return greet(name)
}

console.log(processUser(name, sayHello))