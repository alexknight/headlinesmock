/**
 * Created by Administrator on 2015/12/21.
 */


function showSuccessToast() {
    $().toastmessage('showSuccessToast', "Success Dialog which is fading away ...");
}
function showStickySuccessToast() {
    $().toastmessage('showToast', {
        text     : 'Success Dialog which is sticky',
        sticky   : true,
        position : 'top-right',
        type     : 'success',
        closeText: '',
        close    : function () {
            console.log("toast is closed ...");
        }
    });

}

function showNoticeToast() {
    $().toastmessage('showNoticeToast', "Notice  Dialog which is fading away ...");
}

function showStickyNoticeToast() {
    $().toastmessage('showToast', {
         text     : 'Notice Dialog which is sticky',
         sticky   : true,
         position : 'top-right',
         type     : 'notice',
         closeText: '',
         close    : function () {console.log("toast is closed ...");}
    });
}

function showWarningToast(msg) {
    $().toastmessage('showWarningToast', msg);
}

function showStickyWarningToast() {
    $().toastmessage('showToast', {
        text     : 'Warning Dialog which is sticky',
        sticky   : true,
        position : 'top-right',
        type     : 'warning',
        closeText: '',
        close    : function () {
            console.log("toast is closed ...");
        }
    });
}

function showErrorToast() {
    $().toastmessage('showErrorToast', "Error Dialog which is fading away ...");
}

function showStickyErrorToast() {
    $().toastmessage('showToast', {
        text     : 'Error Dialog which is sticky',
        sticky   : true,
        position : 'top-right',
        type     : 'error',
        closeText: '',
        close    : function () {
            console.log("toast is closed ...");
        }
    });
}

