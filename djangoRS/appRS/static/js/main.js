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
        const prevSpan = prevNode.nextSibling.nextSibling;
        prevSpan.childNodes[1].classList.remove("clicked");
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
                const spanImage = node.nextSibling.nextSibling;
                spanImage.childNodes[1].classList.add("clicked");
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
    $.ajax({
        type: 'POST',
        url: '/main/',
        data: JSON.stringify(data),
        success: function (json) {
            cnt++;
            var showImage = "";
            const images = JSON.parse(json.randImage)
            console.log(images);
            for (var i = 0; i < images.length; i++) {
                showImage += "<article class=\"style1\">";
                showImage += "<label>"
                showImage += "<input type=\"radio\" name=\"select"+cnt+"\" value='" + images[i].fields.Name + "' onclick=\"getSelected("+cnt+")\"/>\n"
                showImage += "<span class=\"image\">"
                showImage += "<img src=\"/static/tour_img/" + images[i].fields.Name + "1" + images[i].fields.Extension + "\" alt=\"" + images[i].fields.Name + "\" />\n"
                showImage += "</label>"
                showImage += "</article>"
            }
            $('[class="tiles"]').html(showImage);
            if(cnt==3) {
                selectButton.setAttribute("type", "submit")
                $("#formId").attr("action", "/result/")

            }
        },
        error: function (request, status, err) {
            console.log("실패")
        }
    });
});


