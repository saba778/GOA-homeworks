// 1)შექმენი ფუნქცია რომელიც იღებს სახელს და აბრუნებს მისალმებას Hello Name!

let user = prompt('enter name')

function greet(user){
    return `hello ${user}`
}


// 2)შექმენი ფუნქცია რომელიც იღებს ორ რიცხვს და აბრუნებს მათ ჯამს

function add(number1,number2){
    return number1 + number2            
    // ორივეს უმატებს
}




// 3)შექმენი ფუნქცია რომელიც ამოწმებს რიცხვი ლუწია თუ კენტი


function odd(numb){
    if (numb % 2 == 0){
        console.log(even)
    } else{
        console.log('odd')
    }
}


// 4)კომენტარებით ახსენი რა არის default parameter და მოიყვანე 1 მაგალით თუ როგორ მუშაობ
// default paramiter არის რაც გაიშვება იმ შემთხვევაში ტო ფუნქციაში არ ჩაიწერება არგუმენტი
// function function greet(user == 'guest'){
//     return `hello ${user}`
// }S