/**
 * Created by lsf on 15-12-19.
 */

$(document).ready(function() {
    DynamicMockTask.initTagInput();
//    DynamicMockTask.FlagView();
});

DynamicMockTask = {
    initTagInput: function(){

        $('#datatextarea').tagsInput({
            'height':'100%',
            'width':'100%',
            'interactive':true,
            'defaultText':'添加接口'
        });
    },

    FlagView:function(){
        if ($('#batch').val() != 1){
        document.getElementById("flag").style.display="None";
        }
    }
};