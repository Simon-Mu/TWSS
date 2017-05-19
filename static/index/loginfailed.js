$(document).ready(function () {

    var firstbar = $('#firstbar');
    var time = 10;
    function countdown() {
        if (time <= 0)
            location.href = '/index';

        setTimeout(function () {
            firstbar.text(--time+'秒后返回登录界面');
            countdown();
        }, 1000)
    }
    countdown();


    var overbar = $('#overbar');
    var width = 0;
    function growth() {
        if(width>280){
            var set_radius = '0 ' + (width-280) + 'px 0 0';
            overbar.css('border-radius', set_radius);
        }
        setTimeout(function () {
            overbar.css('width', width++ + 'px');
            growth();
        }, 32);
    }
    growth();

});