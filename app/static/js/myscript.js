$('#query').keyup(function(){
    var query = $('#query').val()
    if (query.trim().length>1){
        $.ajax({
            type: "POST",
            url: "",
            data: {
                name:query
            },
            success: function(data){
                console.log("success",data)
                $('#out-data').html("");
                $.each(data, function(key,value){
                    // console.log("data is ",value.name,value.image,value.description);
                    $('#out-data').append(`<span>`+value.name+`</span>\
                    <img src="media/`+value.image+`" alt="image" />\
                    <span>`+value.description+`</span>`
                    )

                });
            },
            error: function(data){
                console.log("error",data)
            }
        });
    }


});