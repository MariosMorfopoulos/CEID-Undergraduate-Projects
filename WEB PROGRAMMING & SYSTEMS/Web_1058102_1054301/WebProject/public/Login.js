
function LoginUserAdmin(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if(username == ""){
        alert("Πρέπει να βάλετε όνομα για τον χρήστη");
        return ;
    }
    if(password == ""){
        alert("Πρέπει να βάλετε κωδικό για τον χρήστη");
        return ;
    }
    $("#LoginUserAdmin").on("submit", function (event){
        event.preventDefault();
        // var username = $("#onoma")
        // var password = $("#pass")
        // var email    = $("#email")
        //console.log("Username: "+username+ "Password: " + password);
        const request = $.ajax({
            url:"/",
            method:"POST",
            contentType:"application/json",
            data: JSON.stringify({username: username, password: password}),
            success:function(response){
                //|| response.redirect == "/AdminIndex"
                if(response.redirect == "/Upload"){
                    alert("Σύνδεση!!!");
                    window.location = response.redirect
                }
                // if(response.redirect == "/AdminIndex"){
                //     alert("Σύνδεση!!!");
                //     window.location = response.redirect

                // }
                else if(response.redirect == "/")
                {
                    alert("Λάθος στοιχεία");
                    window.location = response.redirect
                }
            }           
        });
        // request.done(TelikoCheck);
    })
}
