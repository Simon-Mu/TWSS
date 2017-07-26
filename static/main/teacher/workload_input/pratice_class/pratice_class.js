$(document).ready(function () {
    $('#workload_input_pratice_class').click(function () {
        $('.main_interface').hide();
        $('.pratice_class_content').show();
    });

    $('.pratice_class_add_button').click(function () {
        $('.pratice_class_content_blur_area').css('filter','blur(10px)');
        $('.pratice_class_add').show();
    });

    $('.pratice_class_add_cross').click(function () {
        $('.pratice_class_content_blur_area').css('filter','none');
        $('.pratice_class_add').hide();
    });

    $('#pratice_class_add_cancel').click(function () {
        $('.pratice_class_content_blur_area').css('filter','none');
        $('.pratice_class_add').hide();
    });
});