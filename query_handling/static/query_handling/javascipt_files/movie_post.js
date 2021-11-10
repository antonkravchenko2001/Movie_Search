let form = document.getElementById('post_form');
for(let i = 1; i < form.children.length - 1; i++){
    div = form.children[i];
    console.log(div)
    if(div.children.length > 2){
        div.children[1].style.background = '#cb03031a';
    }
};