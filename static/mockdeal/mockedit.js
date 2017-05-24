/**
 * Created by lsf on 15-12-19.
 */

$(document).ready(function() {
    document.getElementById("real_edit_json_editor").style.display="None";
    Edit.initEditJsonEditor();
});

Edit = {
    initEditJsonEditor: function(jsonValue2){
        var container2 = document.getElementById("edit_json_editor");

        var options2 = {
            mode: 'text',
            change: function(){
                if (editor2 != null){
                    //console.log(editor.getText());
                    var json_datas = $.toJSON(editor2.getText());
                    $('#real_edit_json_editor').val(json_datas);
                    console.log(json_datas);
                    //editor2.expandAll();
                }
            }
        };

        var json2 = JSON.parse($('#real_edit_json_editor').val());
        if (jsonValue2 != undefined && jsonValue2 != null) {
            json2 = jsonValue2;
        }
        var editor2 = new JSONEditor(container2, options2, json2);
    }
};