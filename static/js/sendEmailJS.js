
var successAlert = document.getElementById("success_alert");
var failedAlert = document.getElementById("failed_alert");


function sendMail(contactForm) {
    emailjs.send("gmail", "art_store", {
        "from_name": contactForm.full_name.value,
        "from_email": contactForm.email_address.value,
        "text_field": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
            contactForm.reset();
            successAlert.classList.add("show");
        },
        function(error) {
            console.log("FAILED", error);
            failedAlert.classList.add("show");
        }
    );
    return false;
}