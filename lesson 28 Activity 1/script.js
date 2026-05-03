

// var Question = prompt("Is it Raining? (y/n)")



// if (Question == "y") {


//     alert("Please Take An Umbrella")
// }
// else {


//     alert("No Need For One!!!!")

// }

// var Question2 = prompt('it is it really hot outside? (y/n)')

// if (Question2 == "y") {

//     alert(" You should put on sun screen today")
// }

// else {

//     alert('you dont need sun screen today')
// }
var counter  = 0
while ( counter <= 3) {

var Question3 = prompt('Guess a number between 1 and 20')
if (Question3 > 10) {
    alert('its lower than that')
}
else if (Question3 < 10) {

    alert('its higher than that')
}
else if (Question3 == 10) {

    alert('you got it right')
}


counter = counter+1 
}
