// get username
const username = localStorage.getItem('username');
const inputTag = document.querySelector('.username');
document.querySelector('header p').innerText = `${username} 님을 위한 추천 여행지 입니다.`;
inputTag.innerText = `${username} 님, 추천 결과가 만족스러우신가요?`;


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
            console.log("실패")
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