



//Get the price for the print and quantity of a specific print the user has picked

function getPriceForPrints() {
    var selectOptions = document.getElementById("sizeOptions").value;
    var quantity = document.getElementById("quantity").value;
    var priceForPrints = parseFloat(selectOptions * quantity).toFixed(2);
    
    if(isNaN(priceForPrints) || priceForPrints == 0) {
        document.getElementById('displayPrice').innerHTML = "You need to pick both a size and wished number of prints.";
        document.getElementById('currency-euro').innerHTML = "";
    } else {
        document.getElementById('displayPrice').innerHTML = priceForPrints;
        document.getElementById('currency-euro').innerHTML = "€";
    };
};


// Get the selected address
let shipping_selection = document.querySelector('#shipping_addresses')
var address = "{{ all_shipping_addresses }}"
console.log(address)

shipping_selection.addEventListener('change', () => {
    let result = shipping_selection.options[shipping_selection.selectedIndex].value;
    console.log(result) 
})



//Submit Shipping and billing forms with one button
submitShippingBilling = function(){
    document.forms["shipping_form"].submit();
    document.forms["billing_form"].submit();
}