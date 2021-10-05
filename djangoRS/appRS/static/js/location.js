var gps_use = null; //gps의 사용가능 여부
var gps_lat = null; // 위도
var gps_lng = null; // 경도
var gps_position; // gps 위치 객체

gps_check();
// gps가 이용가능한지 체크하는 함수이며, 이용가능하다면 show location 함수를 불러온다.
// 만약 작동되지 않는다면 경고창을 띄우고, 에러가 있다면 errorHandler 함수를 불러온다.
// timeout을 통해 시간제한을 둔다.
function gps_check(){
    if (navigator.geolocation) {
        var options = {timeout:60000};
        navigator.geolocation.getCurrentPosition(showLocation, errorHandler, options);
    } else {
        alert("GPS_추적이 불가합니다.");
        gps_use = false;
    }
}


// gps 이용 가능 시, 위도와 경도를 반환하는 showlocation함수.
function showLocation(position) {
    gps_use = true;
    gps_lat = position.coords.latitude;
    gps_lng = position.coords.longitude;
    console.log("GPS: ",gps_lat,"   ", gps_lng); //nearLocation
    const data = {'Latitude':gps_lat, 'Longitude':gps_lng};
    $.ajax({
        type:'POST',
        url:'/nearLocation/',
        data:JSON.stringify(data),
        success:function(json){
            console.log("위도 보내기 성공");
            console.log(json)
            const images = json.randImage
            // console.log(images)
            var showImage = ""
            console.log(json.length)
            for( var i = 0; i<images.length; i++){
                console.log(images[i])
                showImage +="<section class=\"feature 6u 12u$(small)\" id=\""+images[i].Id+"\">"+
                    "                        <img onclick=openModal(\""+images[i].Id+"\") class=\"image fit\" src=\""+images[i].Url+"\" alt=\""+images[i].Name+"\" />"+
                    "                        <h3 class=\"name\"> <span onclick=openModal(\""+images[i].Id+"\")>"+images[i].Name+"</span></h3>\n"+
                    "                        <h4 class=\"address\" > <i class=\"fas fa-map-marker-alt\"></i> "+images[i].Address+"</h4>"+
                    "                        <h6 class=\"latitude\">"+images[i].Latitude+"</h6>"+
                    "                        <h6 class=\"longitude\">"+images[i].Longitude+"</h6>" +
                    "                        <p>"+images[i].Contents+"</p>" +
                    "                    </section>"
            }
            $('[class="row"]').html(showImage);
        },
        error: function (request, status, err) {
            console.log(err);
            // alert("죄송합니다. 오류가 발생하여 처음 페이지로 돌아갑니다.(문의는 페이지 하단 메일로 부탁드립니다.)")
            // window.location = '/'
        }
    });
}


// error발생 시 에러의 종류를 알려주는 함수.
// function errorHandler(error) {
//     if(error.code == 1) {
//         alert("접근차단");
//     } else if( err.code == 2) {
//         alert("위치를 반환할 수 없습니다.");
//     }
//     gps_use = false;
// }
