// get username
const username = localStorage.getItem('username');
const inputTag = document.querySelector('.username');
document.querySelector('header p').innerText = `${username} 님을 위한 추천 여행지 입니다.`;
inputTag.innerText = `${username} 님, 추천 결과가 만족스러우신가요?`;

// 만족도 저장
const goodBtn = document.querySelector(".good");
const badBtn = document.querySelector(".bad");

function setSatisfaction(e){
    const targetElement = e.target;
    const state = targetElement.className;
    if(state === "good"){

    }else{

    }
}

goodBtn.addEventListener('click',setSatisfaction);
badBtn.addEventListener('click',setSatisfaction);
