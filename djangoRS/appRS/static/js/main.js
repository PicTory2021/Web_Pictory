
// get username
let username
window.onload = function() {
    username = localStorage.getItem('username');
    if(username !== null && username !== ""){
        const inputTag = document.querySelector('.username');
        inputTag.innerText = `${username} 님,`;
    }
    else{
        window.location = '/'
    }
}
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
            data['selected'] = selectedImages
            $.ajax({
                type: 'POST',
                url: '/main/',
                data: JSON.stringify(data),
                success: function (data) {
                    // const url = data.url
                    // const select3 = data.select3
                    // console.log(url)
                    // console.log(select3);
                    const id = parseInt(userId)
                    window.location =  "/"+data.url+"/"+id
                },
                error: function (request, status, err) {
                    console.log("실패")
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
                    const images = JSON.parse(json.randImage)
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
                    // if (cnt == 3) {
                    //     selectButton.setAttribute("type", "submit")
                    //     $("#formId").attr("action", "/result/")
                    //
                    // }
                },
                error: function (request, status, err) {
                    console.log("실패")
                }
            });
        }
    }
});

