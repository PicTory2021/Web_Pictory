const modal = document.querySelector('div.modal');
const modal_head = document.querySelector('div.modal_head');
const modal_address = document.querySelector('div.modal_address');
const modal_text = document.querySelector('div.modal_text');

const body = document.body;

var value;
//주소 클릭하면 모달 오픈 시켜줄 이벤트 함수
function openModal(i){
    modal.style.display="flex";
    body.style.overflow = 'hidden';

    totalDiv = document.getElementById(i);
    title = totalDiv.querySelector("h3").innerText
    address = totalDiv.querySelector("h4").innerText
    content = totalDiv.querySelector("p").innerText

    modal_head.innerText = title;
    modal_address.innerText = address;
    modal_text.innerText = content;

}


//닫기 버튼 누르면 모달에서 빠져나가도록
document.getElementById("modal_close_btn").onclick = function() {
    modal.style.display="none";
    body.style.overflow = 'auto';
}
//esc 누르면 모달에서 빠져나가도록
window.addEventListener("keyup", e => {
    if(modal.style.display === "flex" && e.key === "Escape") {
        modal.style.display = "none"
        body.style.overflow = 'auto';
    }
})
//모달 밖을 누르면 빠져나가도록
modal.addEventListener("click", e => {
    const evTarget = e.target
    if(!evTarget.classList.contains("modal_content")) {
        modal.style.display = "none"
        body.style.overflow = 'auto';
    }
})



