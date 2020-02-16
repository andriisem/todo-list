$(document).ready(function() {
    $('#addField').click(function(){
        var taskField = document.getElementById("taskField");
        this.style.display = "none";
        taskField.style.display = "block";
    });
    
    $('#cancelAction').click(function(){
        var addField = document.getElementById("addField");
        var taskField = document.getElementById("taskField");
        addField.style.display = "block";
        taskField.style.display = "none";
    });

    $('#addTask').click(function(){
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
        }
    });

    $('.todo').on('click', '.removeTask', function(e) {
        var id = e.target.id;
        $.ajax({
            url: '/_remove',
            data: {
                id: id
            },
            success: function (result) {
                $('#' + id).remove();
                console.log(result)
            }
        });
     });

     $('.todo').on('click', 'input', function(e) {
        var status = e.target.checked;
        var id = e.target.id;
        $.ajax({
            url: '/_mark',
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


