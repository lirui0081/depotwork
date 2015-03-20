$(function () {
    $('#ace_notifications').on('click', function () {
        if ($('.purple').hasClass("open")) {
            return 0;
        }
        $.ajax({
            url: '/notifications/last/',
            data: {'current': window.location.pathname},
            beforeSend: function () {
                $("#ace_notification_content").html("<li class='dropdown-header' xmlns='http://www.w3.org/1999/html'> <i class='ace-icon fa fa-exclamation-triangle'></i> <span id='notification_total'></span>通知</li><li><div class='message-loading-overlay'><i class='fa-spin ace-icon fa fa-spinner orange2 bigger-160'></i></div></li>  <li style='text-align: center' class='dropdown-footer'> <a href=''>查看所有通知 <i class='ace-icon fa fa-arrow-right'></i> </a> </li>");
            },
            success: function (data) {
                $("#ace_notification_content").html(data['data']);
                //switch (data_json["stat"]) {
                //    case 0:
                //        window.location.href(data_json["content"]);
                //        break;
                //        // data.form contains the HTML for the replacement form
                //    case 1:
                //        $("#ace_notification_content").html(data_json['content']);
                //        break;
                //}
            }
        });
    });


    function check_notifications() {
        $.ajax({
            url: '/notifications/check/',
            cache: false,
            success: function (data) {
                // data.form contains the HTML for the replacement form
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
                window.setTimeout(check_notifications, 100000);
            }
        });
    };
    check_notifications();
});