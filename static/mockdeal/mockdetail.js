/**
 * Created by lsf on 15-12-20.
 */

$(document).ready(function() {
    document.getElementById("real_detail_json_editor").style.display="None";
    Edit.initEditJsonEditor();
});

Edit = {
    initEditJsonEditor: function(jsonValue2){
        var container2 = document.getElementById("detail_json_editor");

        var options2 = {
//            mode: 'code,text,form,view'
            mode: 'tree'
        };

        var json2 = JSON.parse($('#real_detail_json_editor').val());
        if (jsonValue2 != undefined && jsonValue2 != null) {
            json2 = jsonValue2;
        }
        var editor2 = new JSONEditor(container2, options2, json2);
    }
};