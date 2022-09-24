document.addEventListener('DOMContentLoaded', () => {
    $('.game-quantity').on('keydown', function (e) {
        e.preventDefault();
    });

    $('.btn-group').children('button').off('click').on('click', function (e) {
        if (e.currentTarget.classList.contains('increment-quantity')) {
            if ($(e.currentTarget)[0].parentElement.children[1].lastElementChild.value > 4) return;

            $(e.currentTarget)[0].parentElement.children[1].lastElementChild.value =
                parseInt($(e.currentTarget)[0].parentElement.children[1].lastElementChild.value) + 1;
            $(e.currentTarget.parentElement.children[1]).trigger('submit');
        } else if (e.currentTarget.classList.contains('decrement-quantity')) {
            if ($(e.currentTarget)[0].parentElement.children[1].lastElementChild.value < 1) return;

            $(e.currentTarget)[0].parentElement.children[1].lastElementChild.value =
                parseInt($(e.currentTarget)[0].parentElement.children[1].lastElementChild.value) - 1;
            $(e.currentTarget.parentElement.children[1]).trigger('submit');
        }
    });
});