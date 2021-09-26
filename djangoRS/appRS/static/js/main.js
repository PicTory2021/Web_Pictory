
// get username
const username = localStorage.getItem('username');
const inputTag = document.querySelector('.username');
inputTag.innerText = `${username} 님,`;

