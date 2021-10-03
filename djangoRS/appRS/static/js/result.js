// get username
const username = localStorage.getItem('username');
const inputTag = document.querySelector('.username');
document.querySelector('header p').innerText = `${username} 님을 위한 추천 여행지 입니다.`;
inputTag.innerText = `${username} 님, 추천 결과가 만족스러우신가요?`;


$(".eval").on('click',function(e){
    const state = e.target.id
    const eval = ( state === "good" ) ? true:false
    const data = {'eval':eval}
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
