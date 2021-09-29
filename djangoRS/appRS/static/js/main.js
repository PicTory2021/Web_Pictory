// get username
const username = localStorage.getItem('username');
const inputTag = document.querySelector('.username');
inputTag.innerText = `${username} 님,`;

// image select
let selectedImages = new Array(3)
const selectButton = document.querySelector(".button.select");

function getSelected(num){
    const ImageNodeList = document.getElementsByName("select"+num);
    ImageNodeList.forEach((node)=>{
        if(node.checked){
            selectedImages[num-1] = node.value;
        }
    })
    console.log(selectedImages);
}
function getSelected2(){
    const ImageNodeList = document.getElementsByName("select2");
    ImageNodeList.forEach((node)=>{
        if(node.checked){
            selectedImages[1] = node.value;
            selectedImages[2] = '';
        }
    })
    console.log(selectedImages);
}
function getSelected3(){
    const ImageNodeList = document.getElementsByName("select3");
    ImageNodeList.forEach((node)=>{
        if(node.checked){
            selectedImages[2] = node.value;
        }
    })
    console.log(selectedImages);
}
// selectButton.addEventListener("click",selectBtn);
var cnt = 1;
// Ajax
$(".button.select").on('click',function (e){
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


