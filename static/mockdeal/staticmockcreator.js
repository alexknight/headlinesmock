/**
 * Created by lsf on 15-12-19.
 */
$(document).ready(function() {
    document.getElementById("static_json_datas").style.display="None";
    StaticCreator.initJsonEditor();
});

StaticCreator = {
    initJsonEditor:function(jsonValue){
        var container = document.getElementById("json_editor");

        var options = {
            mode: 'text',
            change: function(){
                if (editor != null){
                    console.log("editor.getText():\n"+editor.getText());
                    var json_datas = $.toJSON(editor.getText());
                    $('#static_json_datas').val(json_datas);
                    console.log(json_datas);
                    //editor2.expandAll();
                }
            }
        };

        var json = [{}];
        if (jsonValue != undefined && jsonValue != null) {
            json = jsonValue;
        }
        var editor = new JSONEditor(container, options, json);
        }

};


