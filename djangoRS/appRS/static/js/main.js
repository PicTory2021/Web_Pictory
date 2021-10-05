
// get username
let username
$(document).ready(function() {
    username = localStorage.getItem('username');
    userId = localStorage.getItem('userId');
    if(userId !== null && userId !== ""){
        const inputTag = document.querySelector('.username');
        inputTag.innerText = `${username} 님,`;
    }
    else{
        alert("이름 등록 후, 이용 가능합니다. 처음 페이지로 이동합니다.")
        window.location = '/'
    }
})

// image select
let selectedImages = [];
const selectButton = document.querySelector("#select-btn");
var prevNode;

function getSelected(num){
    if(prevNode) {
        const prevSpan = prevNode.nextElementSibling.childNodes[1];
        prevSpan.classList.remove("clicked");
    }
    const ImageNodeList = document.getElementsByName("select"+num);
    ImageNodeList.forEach((node)=>{
        if(node.checked){
            if(prevNode == node){
                selectedImages[num-1] = "";
                node.checked = false;
                prevNode = "";
            }
            else{
                selectedImages[num-1] = node.value;
                const spanImage = node.nextElementSibling.childNodes[1];
                spanImage.classList.add("clicked");
                prevNode = node;
            }
        }
    })
    console.log(selectedImages);
}

var cnt = 1;
// progress bar
var progWidth = [33.3,66.6,100,100]

function moveBtn() {
    console.log(cnt)
    if(selectedImages[cnt-1] === undefined || selectedImages[cnt-1]==='') {
        console.log("선택안함")
    }else{
        var progressDiv = document.getElementById('progressing');
        var width = progWidth[cnt - 1]
        var maxWidth;
        if (cnt === 3){ maxWidth = 100; }
        else { maxWidth = progWidth[cnt]; }
        console.log("width : " + width)
        console.log("maxWidth : " + maxWidth)
        var id = setInterval(frame, 45);

        function frame() {
            if (width >= maxWidth) {
                clearInterval(id);
            } else {
                width = width + 2;
                progressDiv.style.width = width + "%";
            }
        }
    }
    window.scrollTo(0,0)
}



// Ajax
$("#select-btn").on('click',function (e){
    console.log("ajax");
    console.log(cnt);
    const userId = localStorage.getItem("userId")
    let data = {
        'userId':userId,
        'selected': selectedImages
    };
    if(selectedImages[cnt-1]===undefined ||selectedImages[cnt-1]===''){
        document.querySelector("#plzSelect").innerHTML = "사진을 선택해주세요.";
        window.scrollTo(0,0)
    }else {
        console.log(data.selected);
        if(cnt == 3){
            $.ajax({
                type: 'POST',
                url: '/main/',
                data: JSON.stringify(data),
                success: function (data) {
                    // const url = data.url
                    // const select3 = data.select3
                    // console.log(url)
                    // console.log(select3);
                    cnt=1;
                    const id = parseInt(userId);
                    window.location =  "/"+data.url+"/"+id;
                },
                error: function (request, status, err) {
                    alert("죄송합니다. 오류가 발생하여 처음 페이지로 돌아갑니다.(문의는 페이지 하단 메일로 부탁드립니다.)");
                    window.location = '/';
                }
            });
        }
        else {
            $.ajax({
                type: 'POST',
                url: '/main/',
                data: JSON.stringify(data),
                success: function (json) {
                    document.querySelector("#plzSelect").innerHTML = "";
                    cnt++;
                    var showImage = "";
                    const images = JSON.parse(json.randImage);
                    console.log(images);
                    for (var i = 0; i < images.length; i++) {
                        showImage += "<article class=\"style1\">" +
                            "            <label>" +
                            "                <input required type=\"radio\" name=\"select" + cnt + "\" value=\"" + images[i].pk + "\" onclick=\"getSelected(" + cnt + ")\"/>" +
                            "                <span class=\"image\">" +
                            "                    <img src=\"/static/tour_img/" + images[i].fields.Name + "1" + images[i].fields.Extension + "\" alt=\"" + images[i].fields.Name + "\" />" +
                            "                </span>" +
                            "            </label>" +
                            "        </article>"
                    }
                    $('[class="tiles"]').html(showImage);
                },
                error: function (request, status, err) {
                    alert("죄송합니다. 오류가 발생하여 처음 페이지로 돌아갑니다.(문의는 페이지 하단 메일로 부탁드립니다.)");
                    window.location = '/';
                }
            });
        }
    }
});