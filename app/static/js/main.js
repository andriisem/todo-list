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
                            <input type="checkbox" id="${item.id}" ${item.status}> ${item.description}</input>
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
        taskField.style.display = "block";
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
                url: '/add',
                data: {
                    description: description.val()
                },
                success: function (result) {
                    var id = result['id'];
                    var description = result['description'];
                    var li = 
                        `<li id=${id} class='task'>
                            <input type='checkbox' id=${id}> ${description}</input>
                            <i class='fa fa-trash removeTask' id=${id}></i>
                        </li>`;
                    $('ul').append(li);
                }
            });
        }
    });

    $('ul').on('click', '.removeTask', function (e) {
        var todo_id = e.target.id;
        $.ajax({
            url: '/remove',
            data: {
                todo_id: todo_id
            },
            success: function (result) {
                $('#' + todo_id).remove();
            }
        });
    });

    $('ul').on('click', 'input', function (e) {
        var status = e.target.checked;
        var id = e.target.id;
        $.ajax({
            url: '/mark',
            data: {
                id: id,
                status: status * 1
            },
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
