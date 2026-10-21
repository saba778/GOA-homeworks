// 1)შექმენი ცვლადი სადაც შეინახავ ქულას 0-100 (შედეგების მიხედვით გამოიტანე შესაბამისი ქულა A,B,C,F) 
const grade = 74
if (grade > 90 && grade < 100){
    console.log('A')
}else if(grade > 70 && grade < 89){
    console.log('B')
}else if(grade > 50 && grade < 69){
    console.log('C')
}else{
    console.log('F')
}


// 2)მომხმარებელს შემოატანინეთ მისი სახელი და შეინახეთ ცვლადში იმ შემთხვევაში თუ ცარიელი არ იქნება, თუ ცარიელია შეინახეთ Guest და ეს ცვლადი გამოიტანეთ კონსოლში (Truthy და Falsy მინიჭებით)

let name = prompt('enter your name')

if(name == false){
    name = 'Guest'
}
// 3)შექმენი ცვლადი სადაც შეინახავ ასაკს 
// Ternary ოპერატორით შეამოწმე თუ ასაკი მეტია 18 გამოიტანე Acsess Granted სხვა შემთხვევაში გამოიტანე Acsess Denied
const age = 18

age > 18 ? (console.log('Acsess Granted')) : (console.log('Acsess Denied'))