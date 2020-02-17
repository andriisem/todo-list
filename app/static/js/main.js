$(function () {
    document.title = 'To Do'
    $.ajax({
        type: 'GET',
        url: '/get',
        dataType: 'json',
        success: function (result) {
            var buffer = "";
            $.each(result, function (index, val) {
                for (var i = 0; i < val.length; i++) {
                    var item = val[i];
                    if (item.status) {
                        var style = "text-decoration: line-through;";
                    } else {
                        var style = "";
                    }
                    buffer += 
                        `<li id="${item.id}" style="${style}">
                            <input class="mb-15 mr-10" type="checkbox" id="${item.id}" ${item.status}>${item.description}</input>
                            <i class="fa fa-trash removeTask" id="${item.id}"></i>
                        </li>`;
                }
                $('ul').html(buffer);
            });
        }
    });

    $('#addField').click(function(){
        var taskField = document.getElementById("taskField");
        this.style.display = "none";
        taskField.style.display = "flex";
    });

    $('#cancelAction').click(function () {
        var addField = document.getElementById("addField");
        var taskField = document.getElementById("taskField");
        addField.style.display = "block";
        taskField.style.display = "none";
    });

    $('#addTask').click(function () {
        if ($.trim($('#txtDescription').val()).length > 0) {
            var description = $('#txtDescription');
            $.ajax({
                type: "POST",
                url: '/add',
                data: JSON.stringify({'description': description.val()}),
                success: function (result) {
                    var id = result['id'];
                    var description = result['description'];
                    var li = 
                        `<li id=${id} class='task'>
                            <input class="mb-15 mr-10" type='checkbox' id=${id}>${description}</input>
                            <i class='fa fa-trash removeTask' id=${id}></i>
                        </li>`;
                    $('ul').append(li);
                }
            });
            description[0].value = '';
        }
    });

    $('ul').on('click', '.removeTask', function (e) {
        var todo_id = e.target.id;
        $.ajax({
            type: 'DELETE',
            url: '/remove',
            data: JSON.stringify({'todo_id': todo_id}),
            success: function (result) {
                $('#' + todo_id).remove();
            }
        });
    });

    $('ul').on('click', 'input', function (e) {
        var status = e.target.checked * 1;
        var id = e.target.id;
        $.ajax({
            type: 'PUT',
            url: '/mark',
            data: JSON.stringify({'todo_id': id, 'status': status}),
            success: function (result) {
                if (status) {
                    $('#' + id)[0].setAttribute('style', 'text-decoration: line-through;')
                } else {
                    $('#' + id)[0].removeAttribute('style', 'text-decoration: line-through;')
                }
            }
        });
    });

});
