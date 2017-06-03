$(document).ready(function () {

    // 退出按钮动画
    // $('#logout').click(function () {
    //     var body = $('body');
    //     body.css('filter','blur(5px)');
    //     setTimeout(function () {
    //         var confirm_logout = confirm('确定退出吗?');
    //         if(confirm_logout == true){
    //             window.close();
    //         }
    //         else {
    //             body.css('filter','none');
    //         }
    //     },100);
    //
    // });

    // 禁用左侧菜单的双击选择文字，影响使用体验
    $('.left_unit').addClass('no_select');
    // 禁用全局按钮的双击选择文字
    $('.content_button').addClass('no_select');


    //左侧菜单动画
    $('.unit_title').click(function () {
        // 点击标题后 隐藏其他模块的子菜单 显示本模块的子菜单
        $('.unit_options').slideUp('fast');
        if($(this).next().css('display') === 'none'){
            $(this).next().slideDown('fast');
        }

        // 隐藏其他模块的主界面 显示本模块的主界面
        // $('.main_interface').hide();
        // var title_name = $(this).attr('id');
        // var content_name = title_name.replace('_title','_content');
        // $('.'+content_name).show();
    });

});