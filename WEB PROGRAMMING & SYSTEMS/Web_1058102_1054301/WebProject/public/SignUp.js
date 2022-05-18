// const { request } = require("express");

//const { default: swal } = require("sweetalert");

//Συνάρτηση για να κάνουμε CHECK ότι έχουμε βάλει στοιχεία στην φόρμα  χρησιμοποιωντας DOM δες SignUp.ejs BUTTON1.
function SignUpUser(){
    var username = document.getElementById("onoma").value;
    var password = document.getElementById("pass").value;
    var email    = document.getElementById("email").value;
    if(username == ""){
        alert("Πρέπει να βάλετε όνομα για τον χρήστη");
        return ;
    }
    if(password == ""){
        alert("Πρέπει να βάλετε κωδικό για τον χρήστη");
        return ;
    }
    if(email == ""){
        alert("Πρέπει να βάλετε email για τον χρήστη");
        return ;
    }
    if(!passwordSignUpUser(password)){
        return;
    }
    $("#SignUp").on("submit", function (event){
        event.preventDefault();
        // var username = $("#onoma")
        // var password = $("#pass")
        // var email    = $("#email")
        //console.log("Username: "+username+ "Password: " + password + "Email: " + email);
        const request = $.ajax({
            // url:"/SignUp",
            url:"/SignUp",
            method:"POST",
            contentType:"application/json",//HTTP tipos JSON
            data: JSON.stringify({username: username, password: password, email:email}),
            success:function(response){
                if(response.redirect == "/SignUp"){
                    //$.notify(response.message);
                    alert("Ο χρήστης με τα παραπάνω στοιχεία υπάρχει ήδη αλλάξτε τα στοιχεία σας");
                    window.location = response.redirect
                }else if(response.redirect == "/")
                {
                    // console.log(response)
                    alert("Η εγγραφή σας ολοκληρώθηκε με επιτυχία");
                    // window.location = response.redirect
                    window.location = response.redirect
                }
            }           
        });
        //request.done(TelikoCheck);
    })
           
}
//Συνάρτηση PASSWORD SIGN UP USER
function passwordSignUpUser(pass){
    var mistakes = [];//Δηλώνω ένα άδειο array 
    if (pass.search(/[A-Z]/)< 0){
        mistakes.push("Ο κωδικός πρέπει να περιέχει τουλάχιστον ένα κεφαλαίο γράμμα.\n");
    }
    if (pass.search(/[0-9]/)< 0){
        mistakes.push("Ο κωδικός πρέπει να περιέχει τουλάχιστον έναν αριθμό.\n");
    }
    if (pass.length < 8){
        mistakes.push("Ο κωδικός πρέπει να είναι τουλάχιστον 8 χαρακτήρες.\n");
    }
    if (pass.search(/[\\!\\@\\#\\$\\%\\^\\&\\*\\(\\)\\-\\+\\.\\;\\,\\:\\_]/) <  0  ){
        mistakes.push("Ο κωδικός πρέπει να περιέχει τουλάχιστον ένα σύμβολο (π.χ #$*&@)\n");
    }
    if (mistakes.length > 0){
        alert(mistakes.join(" "));
        return false;
    }
    return true;
}                      
// function TelikoCheck(response){
//     if(response.redirect != null){
//         alert("Ο χρήστης με τα παραπάνω στοιχεία υπάρχει ήδη αλλάξτε τα στοιχεία σας");
//         window.location = response.redirect
//     }
//     else if(response.redirect == null){
//         alert("Επιτυχής Εγγραφή!");
//         window.location = response.redirect
//     }
// }

   
//Συνάρτηση για να κάνουμε RESET χρησιμοποιωντας DOM δες SignUp.ejs BUTTON2.
function Reset(){
    var username = document.getElementById("onoma").reset();
    var password = document.getElementById("pass").reset();
    var email    = document.getElementById("email").reset(); 
}

// $(function() {
//     //GETREAD 
//     $('#SignUp').on('submit', function(){
//         console.log('EISAI MLKAS');
//     });
// });

// $(function() {
//         $("SignUp").on("submit", function(event){
//             var username = $("#onoma")
//             var password = $("#pass")
//             var email    = $("#email")
//             console.log("Username: "+username+ "Password: " + password + "Email: " + password);
//             // $.ajax({
//             //     url:"/app",
//             //     method:"POST",
//             //     contentType:"application/json",
//             //     data: JSON.stringify({username: username, password: password, email:email}),
//             //     success: function(res){
//             //     console.log("GEAAA");
//             //     }
//             // })
//         })
// })




//     //console.log(response)
            //     if(response.redirect != null){
            //         //$.notify(response.message);
            //         //response.redirect = alert("Ο χρήστης με τα παραπάνω στοιχεία υπάρχει ήδη αλλάξτε τα στοιχεία σας");
            //         //window.location = response.redirect
            //     }else(response.redirect == null)
            //     {
            //         // console.log(response)
            //         alert("Η εγγραφή σας ολοκληρώθηκε με επιτυχία");
            //         window.location = response.redirect
            //     }