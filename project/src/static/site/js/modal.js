$(document).ready(function() {

    $('#confirmation-modal').on('show.bs.modal', function (event) {

        var button = $(event.relatedTarget) // Button that triggered the modal
        var recipient = button.data('name')
        var modal = $(this)
        $('#modal_label_message').text('Do you want to delete data ' + recipient  + ' ?')
        $('#modal_button_yes').click(function() {
            $('#form-delete-' + button.data('id')).submit()
        })
    })


    $('#update-confirmation-modal').on('show.bs.modal', function (event) {

        var button = $(event.relatedTarget) // Button that triggered the modal
        var recipient = button.data('name')
        var modal = $(this)
        $('#modal_update_label_message').text('Do you want to update ' + recipient  + ' status ?')
        $('#modal_update_button_yes').click(function() {
            $('#form-update-' + button.data('id')).submit()
        })
    })
})
