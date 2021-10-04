
// get username
$(document).ready(function() {
    const username = localStorage.getItem('username');
    const userId = localStorage.getItem('userId');
    if(userId !== null && userId !== ""){
        const inputTag = document.querySelector('.username');
        document.querySelector('header p').innerText = `${username} 님을 위한 추천 여행지 입니다.`;
        inputTag.innerText = `${username} 님, 추천 결과가 만족스러우신가요?`;
    }
    else{
        alert("이름 등록 후, 이용 가능합니다. 처음 페이지로 이동합니다.")
        window.location = '/'
    }
})

$(".eval").on('click',function(e){
    const state = e.target.id
    const eval = ( state === "good" ) ? true:false
    changeGoodBadIcon(eval)
    const data = {'eval':eval, 'userId':localStorage.getItem("userId")}
    $.ajax({
        type:'POST',
        url:'/eval/',
        data:JSON.stringify(data),
        success:function(){
            console.log("성공")
        },
        error: function (request, status, err) {
            alert("죄송합니다. 오류가 발생하여 처음 페이지로 돌아갑니다.(문의는 페이지 하단 메일로 부탁드립니다.)")
            window.location = '/'
        }
    })
})
function changeGoodBadIcon(eval){
    var goodicon= $('#goodIcon');
    var badicon = $('#badIcon');
    var goodicon_fa_prefix= goodicon.attr('data-prefix');
    var badicon_fa_prefix= badicon.attr('data-prefix');
    if (eval===true) {
        goodicon.attr('data-prefix','fas');
        badicon.attr('data-prefix','far');
    } else {
        goodicon.attr('data-prefix','far');
        badicon.attr('data-prefix','fas');
    }
}

// 새로고침시, 알림, main으로 다이렉트 beforeunload:페이지가 unload 되기 전 실행.
// window.addEventListener('beforeunload', (event) => {
//     event.preventDefault();
//     event.returnValue = '';
//     }
// );
