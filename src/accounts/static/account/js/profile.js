options=document.getElementById("options")
function showOptions(){
    options.style.display="block";
}

function hideOptions(){
    options.style.display="none"
}
 
show_options_btn=document.getElementById("show_options_btn")
show_options_btn.addEventListener("click", showOptions);

options_close_btn=document.getElementById("options_close_btn")
options_close_btn.addEventListener("click",hideOptions);
