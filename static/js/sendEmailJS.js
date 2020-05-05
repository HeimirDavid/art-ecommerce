/*
var templateParams = {
    "from_name": contactForm.full_name.value,
    "from_email": contactForm.email_address.value,
    "text_field": contactForm.message.value
}*/

var successAlert = document.getElementById("success_alert");

var failedAlert = document.getElementById("failed_alert");

console.log(successAlert, failedAlert)



function sendMail(contactForm) {
    emailjs.send("gmail", "art_store", {
        "from_name": contactForm.full_name.value,
        "from_email": contactForm.email_address.value,
        "text_field": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            contactForm.reset()
            //alert("Your email has been sent!")
            //console.log(successAlert)
            successAlert.classList.add("show")
        },
        function(error) {
            console.log("FAILED", error)
            failedAlert.classList.add("show")
        }
    )
    return false;
}