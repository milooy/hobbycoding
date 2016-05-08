var Comment = {
    init: function() {
        this.get();
        this.getByPagination();
    },
    get: function() {
        $.get(location.pathname+"comment/", function(data) {
            $(".comments-container").html(data);
            var num = $('.next-page').attr('href');
            $(".comment-more").data("pagination", num? num: 'end');
            Comment.post();
        });
    },
    getByPagination: function() {
        $('.comments-container').on('click', '.comment-more', function() {
            var next_page = $(".comment-more").data("pagination");
            $.get(location.pathname+"comment/"+next_page, function(data) {
                $(data).each(function(index, value) {
                    var $value = $(value);
                    if($value.hasClass('comment-list')){
                        $(".comment-list").append($value.children());
                    } else if($value.hasClass('pagination')) {
                        var num = $value.find('.next-page').attr('href');
                        $(".comment-more").data("pagination", num? num: 'end');
                        if(!num) {
                            $(".comment-more").remove();
                        }
                    }
                });
            });
        });
    },
    post: function() {
        $('form#comment').ajaxForm({
            url: location.pathname+"comment/",
            type: 'post',
            //clearForm: true,
            success: function() {
                Comment.get();
            }
        });
    },
}
$(function() {
    Comment.init();
});
