// get username
const username = localStorage.getItem('username');
const inputTag = document.querySelector('.username');
document.querySelector('header p').innerText = `${username} 님을 위한 추천 여행지 입니다.`;
inputTag.innerText = `${username} 님, 추천 결과가 만족스러우신가요?`;


