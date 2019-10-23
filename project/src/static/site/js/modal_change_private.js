$(document).ready(function () {
    console.log('test modal private');
    $('#confirmation-private-modal').on('show.bs.modal', function (event) {
        console.log('test open modal');
        $('#modal_private_button_yes').click(function() {
            $('#form-change-private').submit()
        });

    });
})