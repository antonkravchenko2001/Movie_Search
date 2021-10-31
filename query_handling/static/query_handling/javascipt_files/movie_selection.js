let buttons = document.getElementsByName("movie_selection");

buttons.forEach(button  => {
    button.addEventListener("click", function(){
        let id = button.children[0].innerHTML;
        let url = encodeURI(`/find/${id}`);
        console.log(id, url);
        window.open(url,"_self");
    });
});
