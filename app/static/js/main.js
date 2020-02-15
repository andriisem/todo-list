function addFieldAction() {
    var TaskField = document.getElementById("TaskField");
    var TaskButton = document.getElementById("TaskButton");

    if (TaskField.style.display === "none") {
        TaskField.style.display = "block";
        TaskButton.style.display = "none"
    } else {
        TaskField.style.display = "none";

    }
}

function cancelAction() {
    var TaskField = document.getElementById("TaskField");
    var TaskButton = document.getElementById("TaskButton");
    var description = $('#txtDescription');
    description[0].value = '';
    TaskField.style.display = "none";
    TaskButton.style.display = "block"
}

function addTask() {

    if ($.trim($('#txtDescription').val()).length > 0) {
        var description = $('#txtDescription');
        $.ajax({
            url: '/_add',
            data: {
                description: description.val()
            },
            success: function (result) {
                $(".todo").append(result);
            }
        });
        cancelAction();
    }
}

function removeTask(id) {
    $.ajax({
        url: '/_delete',
        data: {
            id: id
        },
        success: function (result) {
            $('#'+ id).remove();
        }
    });
}