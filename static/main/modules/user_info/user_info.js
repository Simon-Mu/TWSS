$(document).ready(function (s) {

    // 导出按钮下拉菜单动画
    var export_button_menu = $('.user_info_export_menu');
    $('#user_info_export').hover(
        // mouse over
        function () { export_button_menu.slideDown('fast'); },
        // mouse leave
        function () { export_button_menu.slideUp('fast'); }
    );

    // 修改
    var modifying = false;
    var modify_button = $('#user_info_modify');

    modify_button.click(function () {
        if(!modifying){
            modifying = true;
            modify_button.text('保存');
            modify_button.css('color','red');
            $('.can_modify').each(function () {
                var data = $(this).text();
                var width = $(this).css('width');
                $(this).html("<input class='modify_area' value="+ data +">");
                $(this).css('width', width);
                $(this).children().css('width', width);
                // 这里要手动设置width避免td自动调整宽度
            });

            // 点击'修改'时模拟点击选择第一个可修改的文本框
            $('.modify_area:first').trigger('select');

            return;
        }

        if(modifying){
            modifying = false;
            modify_button.text('修改');
            modify_button.css('color','black');
            $('.can_modify').each(function () {
                var data = $(this).children().val();
                $(this).html(data);
            });
        }
    });
    
    
    $('#user_info_to_excel').click(function () {
        var form = $('#request_form');
        var requestfor = $('#requestfor');
        form.attr('action', '/to_excel');
        requestfor.val('userinfo');
        form.submit();

        form.attr('action', '');
        requestfor.val('');
    });



});