$(document).ready(function (s) {

    // 导出按钮下拉菜单动画
    var export_button_menu = $('.user_info_export_menu');
    $('#user_info_export').hover(
        // mouse over
        function () {
            export_button_menu.slideDown('fast');
        },
        // mouse leave
        function () {
            export_button_menu.slideUp('fast');
        }
    );

    // 修改
    var modifying = false;
    var modify_button = $('#user_info_modify');

    modify_button.click(function () {
        // 判断修改状态
        // 未修改状态时为'修改'按钮
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

        // 修改状态时为'保存'按钮
        if(modifying){
            modifying = false;
            modify_button.text('修改');
            modify_button.css('color','black');
            // 将数据储存为json字符串
            var datas_jsonstr = '{';
            $('.can_modify').each(function () {
                var title = $(this).prev('th').text();
                var data = $(this).children().val();
                datas_jsonstr += '"'+ title +'": "' + data + '",';
                $(this).html(data);
            });
            datas_jsonstr = datas_jsonstr.substring(0, datas_jsonstr.length-1);
            datas_jsonstr += '}';

            var form = $('#request_form');
            var requestfor = $('#requestfor');
            var requestdata = $('#request_data');
            // 配置目标url
            form.attr('action', '/upload');
            // 配置请求的excel为'user_info'
            requestfor.val('user_info');
            // 附上数据
            requestdata.val(datas_jsonstr);
            // 提交
            form.ajaxSubmit({
                success: function () {
                    alert('保存成功');
                },
                error: function () {
                    alert('保存失败');
                }
            });

            // 提交后重置目标url及请求
            form.attr('action', '');
            requestfor.val('');
            requestdata.val('');
        }
    });

    // 点击'导出为Excel'后向服务器发送请求及表单
    var button_user_info_to_excel = $('#user_info_to_excel');
    var button_user_info_to_excel_able = true;
    button_user_info_to_excel.click(function () {
        if(button_user_info_to_excel_able === false){
            return;
        }
        var form = $('#request_form');
        var requestfor = $('#requestfor');
        // 配置目标url
        form.attr('action', '/download');
        // 配置请求的excel为'user_info'
        requestfor.val('user_info');
        // 提交
        form.submit();

        // 提交后重置目标url及请求
        form.attr('action', '');
        requestfor.val('');

        // 禁用该按钮 防止多次点击增加服务器负担
        button_user_info_to_excel_able = false;
        // 5秒后恢复按钮
        setTimeout(function () {
            button_user_info_to_excel_able = true;
        }, 5000);
    });



});