$(document).ready(function() {
    MockTask.showData();
});

MockTask ={
    startId: "start_mock",
    editId: "mock_edit_format",
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
        if (document.getElementById("mock_info")) {
            var thiz = this;
            var content = null;
            this.GetMehods(this.info_url, true, function(datas) {
                var tableDiv = $("#"+thiz.tableId);

                for(var i=0;i<datas.length;i++){
                    var data = datas[i];

                    var _id = '<td>' + data.id + '</td>';
                    var _api_id = '<td>' + data.api_id + '</td>';
                    var _createAt = '<td>' + data.createAt + '</td>';
                    var _api = '<td>' +  data.api + '</td>';
                    var _flag = '<td>' +  data.flag + '</td>';

                    var html =  _api_id  +'\n' + _api + '\n' + _flag +'\n' + _createAt + '\n';
                    var op = '<td>'+'\n'+'<a type=\"button\" class=\"btn btn-outline btn-success btn-sm\" id=\"'+data.id+'\" href=\"'+'/mock/detail/' + data.id + '\">详细</button>'+'\n'+'</a>'+ '&nbsp'+
                        '<a type=\"button\" class=\"btn btn-outline btn-success btn-sm\" id=\"'+data.id+'\" href=\"'+'/mock/editor/' + data.id + '\">编辑</button>'+'\n'+'</a>'+ '&nbsp'+
                        '<a type=\"button\" class=\"btn btn-outline btn-success btn-sm\" id=\"'+data.id+'\" href=\"'+'/mock/delete/' + data.id + '\">删除</button>'+'\n'+'</td>';
                    content = content + '<tr>'+html+op+'</tr>'+'\n';
                }
                tableDiv.append(content);
                    $('#mock_info').DataTable({
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

