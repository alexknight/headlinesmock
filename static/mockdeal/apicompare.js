/**
 * Created by Administrator on 2015/12/22.
 */
$(document).ready(function() {
    ApiCompare.showData();
});

ApiCompare ={
    tableId: "mock_table",
    info_url: "/mock/api/all",

    GetMehods:function(url,async,func){
        if (async == null || async == undefined) {
            async = true;
        }

        var datas = null;

        $.ajax({
            type: "GET",
            url: url,
            async: async,
            dataType:'json',
            success : function(result) {
                if (result.code != 'succ') {
                    alert("数据获取失败");
                    return;
                }
                datas = result.data;
                if (func != undefined && $.isFunction(func)) {
                    func(datas);
                }
            }
        });
       return datas;
    },

    showData: function (){
        if (document.getElementById("apicompare_info")) {
            var thiz = this;
            var content = null;
            this.GetMehods(this.info_url, true, function(datas) {
                var tableDiv = $("#"+thiz.tableId);

                for(var i=0;i<datas.length;i++){
                    var data = datas[i];
                    var _id = '<td>' + (i+1) + '</td>';
                    var _api = '<td>' +  data.api + '</td>';
                    var _part_online_api = '<td>' + '<a href=\"'+ data.online_api +'\" title=\"'+ data.online_api +'\" target=\"_blank\">' + data.part_online_api + '</a>' +'</td>';
                    var _createAt = '<td>' + data.createAt + '</td>';

                    var html = _id +'\n' + _api + '\n' + _part_online_api +'\n' + _createAt + '\n';
                    content = content + '<tr>' + html + '</tr>'+'\n';
                }
                tableDiv.append(content);
                    $('#apicompare_info').DataTable({
                        "lengthMenu": [[5, 10, 20,-1], [5, 10, 20,"All"]],
                        "bStateSave": false,
                        "iDisplayLength": 10,
                        "order": [[ 3, "desc" ]]
                    });
            });
        } else {
            return;
        }
    }

};

function isEmptyString(info) {
    if (info == null || info == undefined || info.length == 0){
        return true;
    }
    return false
}

