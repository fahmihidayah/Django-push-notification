$(document).ready(function() {

        if($('#id_is_single').checked) {
            $('#div_id_token').show();
        }
        else {
            $('#div_id_token').hide();
        }

        $('#id_is_single').change(function(){
            if(this.checked) {
                $('#div_id_token').show();
            }
            else {
                $('#div_id_token').hide();
            }
        });
})
