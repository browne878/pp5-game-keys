const stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
const clientSecret = $('#id_client_secret').text().slice(1, -1);

const stripe = Stripe(stripePublicKey);


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
const card = elements.create('card', { style: style, hidePostalCode: true, zipCode: false });
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

const form = document.getElementById('payment-form');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    stripe.createToken(card).then(function (result) {
        if (result.error) {
            console.log('error');
            console.log(result.error);
        } else {
            stripeTokenHandler(result.token);
        }
    });
});

const stripeTokenHandler = (token) => {
    const hiddenInput = document.createElement('input');
    hiddenInput.setAttribute('type', 'hidden');
    hiddenInput.setAttribute('name', 'stripeToken');
    hiddenInput.setAttribute('value', token.id);

    form.appendChild(hiddenInput);

    // submit form
    form.submit();
};