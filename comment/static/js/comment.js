var Comment = {
    init: function() {
        this.get();

    },
    get: function() {
        $.get(location.pathname+"comment/", function(data) {
            $( ".comments-container" ).html(data);
            Comment.post();
        });
    },
    post: function() {
        //$.post(location.pathname+"review/", function() {
        //    console.log("석세스스스");
        //    Comment.get();
        //}).fail(function() {
        //    alert( "error" );
        //});

        $('form#comment').ajaxForm({
            url: location.pathname+"comment/",
            type: 'post',
            //clearForm: true,
            //beforeSubmit: function(formData) {
            //    console.log("form2: ", formData);
            //    if(Comment.init.dataurl) {
            //        formData.map(function(obj) {
            //            if(obj.name==='photo') {
            //                obj.value = Comment.init.dataurl;
            //            }
            //        });
            //    }
            //    console.log("form3: ", formData);
            //    console.log(formData[3].value);
            //},
            success: function() {
                console.log("석세스스스");
                Comment.get();
            }
        });
    },
}
$(function() {
    Comment.init();
});
