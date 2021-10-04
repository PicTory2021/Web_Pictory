const naverModal = document.querySelector('.naverModal');
const naver_modal_close_head = document.querySelector(".naverModal .modal_close_head");
//const body = document.body;

function openNaverModal(i){
    naverModal.style.display="flex";
    body.style.overflow = 'hidden';
    console.log(naverModal.querySelector('iframe'));
    naverModal.querySelector('iframe').src = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=모던화랑';
}

//닫기 버튼 누르면 모달에서 빠져나가도록
document.getElementById("naverModal_close_btn").onclick = function() {
    naverModal.style.display="none";
    body.style.overflow = 'auto';
}

naver_modal_close_head.addEventListener("click",evt => {
    naverModal.style.display="none";
    body.style.overflow = 'auto';
})


//esc 누르면 모달에서 빠져나가도록
window.addEventListener("keyup", e => {
    if(naverModal.style.display === "flex" && e.key === "Escape") {
        naverModal.style.display = "none"
        body.style.overflow = 'auto';
    }
})
//모달 밖을 누르면 빠져나가도록
naverModal.addEventListener("click", e => {
    const evTarget = e.target
    if(evTarget.classList.contains("naverModal_layer")) {
        naverModal.style.display = "none";
        body.style.overflow = 'auto';
        // map.relayout();
    }
})