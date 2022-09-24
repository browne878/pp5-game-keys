document.addEventListener('DOMContentLoaded', () => {
    $('#increment-quantity').off('click').on('click', function () {
        if (parseInt($('#game-quantity').val()) == 5) return;
        $('#game-quantity').val(parseInt($('#game-quantity').val()) + 1);
        $('#game_quantity_form').trigger('submit');
    });

    $('#decrement_quantity').off('click').on('click', function () {
        if (parseInt($('#game-quantity').val()) == 0) return;
        $('#game-quantity').val(parseInt($('#game-quantity').val()) - 1);
        $('#game_quantity_form').trigger('submit');
    });
});