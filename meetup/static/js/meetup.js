var Map = {
    init: function() {
        console.log("맵이 있다 ")
        var mapContainer = document.getElementById('map'); // 지도를 표시할 div
        var mapData = $('#map'); // 지도를 표시할 div
        var lat = mapData.data('lat'),
            lon = mapData.data('lon'),
            locationName = mapData.data('location');

        var mapOption = {
            center: new daum.maps.LatLng(lat, lon), // 지도의 중심좌표
            level: 3 // 지도의 확대 레벨
        };

        var map = new daum.maps.Map(mapContainer, mapOption);

        // 마커가 표시될 위치입니다
        var markerPosition  = new daum.maps.LatLng(lat, lon);

        // 마커를 생성합니다
        var marker = new daum.maps.Marker({
            position: markerPosition
        });

        // 마커가 지도 위에 표시되도록 설정합니다
        marker.setMap(map);

        var positionURL = 'http://map.daum.net/link/map/'+locationName+','+lat+','+lon;
        var iwContent = '<div style="padding:5px;"><a href="'+positionURL+'" style="color:blue" target="_blank">'+locationName+'</a>', // 인포윈도우에 표출될 내용으로 HTML 문자열이나 document element가 가능합니다
            iwPosition = new daum.maps.LatLng(lat, lon); //인포윈도우 표시 위치입니다

        // 인포윈도우를 생성합니다
        var infowindow = new daum.maps.InfoWindow({
            position : iwPosition,
            content : iwContent
        });

        // 마커 위에 인포윈도우를 표시합니다. 두번째 파라미터인 marker를 넣어주지 않으면 지도 위에 표시됩니다
        infowindow.open(map, marker);
    }
};

/*-- 밋업 참여/관심 버튼 ajax --*/
var Users = {
    init: function() {
        this.get('');
        $('button.like').on('click',function() {
            Users.get('like');
            $(this).toggleClass('liked');
        });
        $('button.join').on('click',function() {
            Users.get('join');
            $(this).toggleClass('joined');
        });

    },
    get: function(arg) {
        var arg = arg? '?q=' + arg : '';
        $.get(location.pathname+"user/"+arg, function(data) {
            $(".users-container").html(data);
        });
    },
};

$(function() {
    Users.init();
    if($('#map').data('lat')) {
        Map.init();
    }
});