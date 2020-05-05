console.log("HEllo World")

function sendMail(contactForm) {
    console.log("Hejhopp")
    emailjs.send("gmail", "art_store", {
        "from_name": contactForm.full_name.value,
        "from_email": contactForm.email_address.value,
        "text_field": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error)
        }
    )
    return false;
}