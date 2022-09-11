profile_image=document.getElementById("profile_image");
image=document.getElementById("image");
image.onchange=function(event){
    if(event.target.files.length > 0){
        var src = URL.createObjectURL(event.target.files[0]);
        profile_image.src = src;
    }
};
image_droper=document.getElementById("image_droper");
image_droper.addEventListener("click",function(){
    image.value='';
    profile_image.src='';
});