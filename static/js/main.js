// static/js/main.js

document.addEventListener('DOMContentLoaded', () => {
    // jump to anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        // add click event listener to each anchor link (for each food category)
        anchor.addEventListener('click', function (e) {
            // prevent the default behavior of the link which is navigating to a different page (we are just trying to jump on the SAME page)
            e.preventDefault();

            // find the row associated with the anchor link and scroll to it
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'auto' // jump
            });
        });
    });

    // retrieve DOM elements
    const menuInputs = document.querySelectorAll('.submenu input');
    const orderSummaryTextarea = document.querySelector('#order-form textarea');
    const customerNameInput = document.querySelector('#customer-name');

    // add event listeners to menu inputs
    menuInputs.forEach((input) => {
        input.addEventListener('input', updateOrderSummary);
    });
});

// function to update the order summary
function updateOrderSummary() {
    const menuInputs = document.querySelectorAll('.submenu input');
    const orderSummaryTextarea = document.querySelector('#order-form textarea');
    
    // clear existing content in the textarea
    orderSummaryTextarea.value = '';

    // iterate over menu inputs and update the textarea
    menuInputs.forEach((input) => {
        const menuItem = input.closest('li');
        const itemName = menuItem.querySelector('h3').textContent;
        const itemQuantity = input.value;

        if (itemQuantity > 0) {
            const itemTotal = parseFloat(itemQuantity) * 2.50; // each item costs $2.50
            orderSummaryTextarea.value += `${itemQuantity} ${itemName}(s)    $${itemTotal.toFixed(2)}\n`;
        }
    });
}