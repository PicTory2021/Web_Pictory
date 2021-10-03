const modal = document.querySelector('div.modal');
const modal_close_head = document.querySelector("div .modal_close_head");
const modal_head = document.querySelector('div.modal_head');
const modal_address = document.querySelector('div.modal_address');
const modal_text = document.querySelector('div.modal_text');

const body = document.body;
const features = document.getElementsByClassName('feature');

var container = document.getElementById('map'); //지도를 담을 영역의 DOM 레퍼런스

var value;
contents = {};

//개요 contents Object에 저장 후 index 페이지의 개요는 글자 줄이기
for(var i=0;i<features.length;i++)
{
    contents_id = $(features[i]).attr('id');
    contents[contents_id] = (document.getElementById(contents_id)).querySelector("p").innerText;
    if(((document.getElementById(contents_id)).querySelector("p").innerText).length >200)
        { (document.getElementById(contents_id)).querySelector("p").innerText = contents[contents_id].substr(0,250) + "...";}
}

const resultPage = document.getElementById("resultPage")?1:0;
console.log(resultPage);

let openTime;
let closeTime;
let tourName;
//주소 클릭하면 모달 오픈 시켜줄 이벤트 함수
function openModal(i){
    tourName = i;
    openTime = new Date();
    console.log(openTime)
    modal.style.display="flex";
    body.style.overflow = 'hidden';

    totalDiv = document.getElementById(i);
    title = totalDiv.querySelector("h3").innerText;
    address = totalDiv.querySelector("h4").innerText;
    content = contents[i];
    latitude = totalDiv.querySelector(".latitude").innerText;
    longitude = totalDiv.querySelector(".longitude").innerText;

    modal_head.innerText = title;
    modal_address.innerText = address;
    modal_text.innerText = content;

    var options = { //지도를 생성할 때 필요한 기본 옵션
    center: new kakao.maps.LatLng(latitude, longitude), //지도의 중심좌표.
    level: 3 //지도의 레벨(확대, 축소 정도)
    };
    var map = new kakao.maps.Map(container, options); //지도 생성 및 객체 리턴
    var markerPosition  = new kakao.maps.LatLng(latitude, longitude);  //마커 표시 위치
    var marker = new kakao.maps.Marker({ //마커생성
        position: markerPosition
    });
    marker.setMap(map);

}


//닫기 버튼 누르면 모달에서 빠져나가도록
document.getElementById("modal_close_btn").onclick = function() {
    closeTime = new Date();
    console.log(closeTime);
    console.log((closeTime-openTime)/1000);
    pushClickDB();
    modal.style.display="none";
    body.style.overflow = 'auto';
}

modal_close_head.addEventListener("click",evt => {
    closeTime = new Date();
    pushClickDB();
    modal.style.display="none";
    body.style.overflow = 'auto';
})


//esc 누르면 모달에서 빠져나가도록
window.addEventListener("keyup", e => {
    if(modal.style.display === "flex" && e.key === "Escape") {
        closeTime = new Date();
        pushClickDB();
        modal.style.display = "none"
        body.style.overflow = 'auto';
    }
})
//모달 밖을 누르면 빠져나가도록
modal.addEventListener("click", e => {
    const evTarget = e.target
    if(evTarget.classList.contains("modal_layer")) {
        closeTime = new Date();
        pushClickDB();
        modal.style.display = "none";
        body.style.overflow = 'auto';
        // map.relayout();
    }
})

function pushClickDB(){
    if (resultPage === 0) return
    let data = {
        'UserId':localStorage.getItem('userId'),
        'UserName':localStorage.getItem('username'),
        'SelectImage':tourName,
        'clickOpenDate':openTime,
        'stayTime':(closeTime-openTime)/1000,
    };
    console.log(data);
    $.ajax({
        type: 'POST',
        url: '/result/click',
        data: JSON.stringify(data),
        success: function (json) {
            console.log("ok")
        },error: function (request, status, err) {
            console.log("실패")
            }
        });
}




