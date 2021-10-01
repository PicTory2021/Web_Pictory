// get username
const username = localStorage.getItem('username');
const inputTag = document.querySelector('.username');
inputTag.innerText = `${username} 님, 마음에 드는 사진 한 장을 선택해주세요.`;

// image select
let selectedImages = new Array(3)
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
// Ajax
$("#select-btn").on('click',function (e){
    console.log("ajax");
    console.log(cnt);
    let data = {'selected': selectedImages};
    if(data.selected[cnt-1]===undefined || data.selected[cnt-1]===''){
        document.querySelector("#plzSelect").innerHTML = "사진을 선택해주시기 바랍니다";
        location.href="#plzSelect";
    }else {
        console.log(data.selected[cnt - 1]);
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
                if (cnt == 3) {
                    selectButton.setAttribute("type", "submit")
                    $("#formId").attr("action", "/result/")

                }
            },
            error: function (request, status, err) {
                console.log("실패")
            }
        });
    }
});

