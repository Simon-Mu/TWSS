$(document).ready(function () {
    $('#workload_input_theory_class').click(function () {
        $('.main_interface').hide();
        $('.theory_class_content').show();
    });

    $('.theory_class_add_button').click(function () {
        $('.theory_class_content_blur_area').css('filter','blur(10px)');
        $('.theory_class_add').show();
    });

    $('.theory_class_add_cross').click(function () {
        $('.theory_class_content_blur_area').css('filter','none');
        $('.theory_class_add').hide();
    });

    $('#theory_class_add_cancel').click(function () {
        $('.theory_class_content_blur_area').css('filter','none');
        $('.theory_class_add').hide();
    });
});