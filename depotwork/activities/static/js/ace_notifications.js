$(function () {


    $.ajax({
        url: '/notifications/last/',
        data:{foo:"abc"},
        beforeSend: function () {
            //$("#ace_notification_content").html("<div style='text-align:center'><img src='/static/img/loading.gif'></div>");
            $("#ace_notification_content").html("<div class='message-loading-overlay'><i class='fa-spin ace-icon fa fa-spinner orange2 bigger-160'></i></div>");
            //$("#notifications").removeClass("icon-animated-bell");
        },
        success: function (data) {
            $("#ace_notification_content").html(data);
        }
    });


    function check_notifications() {
        $.ajax({
            url: '/notifications/check/',
            cache: false,
            success: function (data) {
                if (data != "0") {
                    $("#ace_notifications i").addClass("icon-animated-bell");
                    $("#unread_notification_num").text(data);
                }
                else {
                    $("#ace_notifications i").removeClass("icon-animated-bell");
                    $("#unread_notification_num").text(0);
                }
            },
            complete: function () {
                window.setTimeout(check_notifications, 10000);
            }
        });
    };
    check_notifications();
});