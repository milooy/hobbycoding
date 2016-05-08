var Comment = {
    init: function() {
        this.get();
        this.getByPagination();
    },
    /*-- FN: 현재 페이지의 댓글을 ajax로 가져옴 --*/
    get: function() {
        $.get(location.pathname+"comment/", function(data) {
            $(".comments-container").html(data);
            Comment.setPagination();
            Comment.post();
        });
    },
    /*-- FN: 댓글 더보기 버튼을 누르면 ajax로 다음 페이지를 가져와서 노드를 추가 --*/
    getByPagination: function() {
        $('.comments-container').on('click', '.comment-more', function() {
            var next_page = $(".comment-more").data("pagination");
            $.get(location.pathname+"comment/"+next_page, function(data) {
                /*-- get으로 가져온 돔에서 comment-list만 parsing하기 --*/
                $(data).each(function(index, value) {
                    var $value = $(value);
                    if($value.hasClass('comment-list')){
                        $(".comment-list").append($value.children());
                    } else if($value.hasClass('pagination')) {
                        Comment.setPagination($value);
                    }
                });
            });
        });
    },
    /*-- FN: 다음 페이지가 있으면 data-pagination에 저장하고, 없으면 더보기 버튼을 삭제 --*/
    setPagination: function($value) {
        var num = $value? $value.find('.next-page').attr('href') : $('.next-page').attr('href');
        $(".comment-more").data("pagination", num? num: 'end');
        if(!num) {
            $(".comment-more").remove();
        }
    },
    /*-- FN: 댓글 ajax POST --*/
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
