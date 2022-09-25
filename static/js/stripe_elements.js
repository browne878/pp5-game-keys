const stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
const client_secret = $('#id_client_secret').text().slice(1, -1);

const stripe = Stripe(stripe_public_key);


var style = {
    base: {
        hidePostalCode: true,
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': { color: '#aab7c4' }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
const elements = stripe.elements();
const card = elements.create('card', { style: style });
card.mount('#payment-element');

card.addEventListener('change', function (event) {
    if (event.error) {
        $('#error-message').html(`
        <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>`
        );
    } else {
        $('#error-message').text('');
    }
});