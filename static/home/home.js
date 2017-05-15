$(document).ready(function () {

    var captcha;
    var dict = ['0','1','2','3','4','5','6','7','8','9',
        '0','1','2','3','4','5','6','7','8','9',
        '0','1','2','3','4','5','6','7','8','9',
        '0','1','2','3','4','5','6','7','8','9',
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'];

    //生成验证码
    function init_captcha() {
        captcha = '';
        for(var i = 0; i < 4; i++){
            var rand = Math.floor(Math.random()*92);
            captcha += dict[rand];
        }
        //显示验证码
        $('#captcha_img').text(captcha);
    }
    init_captcha();

    //点击验证码切换
    $('#captcha_img').click(function () {
        //清空验证码输入框
        //延迟0.5秒
        setTimeout(function () {
            $('#captcha').val('').focus();
            init_captcha();
        },500);
    });

    //输完验证码按回车 模拟点击登录按钮
    $('#captcha').bind('keydown',function (event) {
       if(event.keyCode == '13'){
           $('#login').trigger('click');
       }
    });
    

    //点击登录
    $('#login').click(function () {
        //校验验证码
        // var captcha_input = $('#captcha').val();
        // if( captcha_input != captcha &&
        //     captcha_input != captcha.toLowerCase() &&
        //     captcha_input != captcha.toUpperCase())  {
        //     $('#warnings').text('验证码错误');
        //     //刷新验证码
        //     $('#captcha_img').trigger('click');
        // }
        // else {
        //     //将账号和密码发送至服务器校验
        //
        //
        //
        //
        //
        //
        //     //猥琐处理
        //     var status = $('#status').val();
        //     localStorage.setItem('status',status);
        //     window.location.href = '../main/main.html';
        //
        //
        // }


        $('#login_form').submit();
    });


    
});