$(document).ready(function () {

    $('#course_info').click(function () {
        $('.main_interface').hide();
        $('.course_content').show();
    });


    // 偶数行增加一个class 稍微不一样的背景色 便于区分
    // 标题行也会受影响 但看不出来 无关紧要
    $('.course_content_table tr:even').addClass('course_content_table_even');
});