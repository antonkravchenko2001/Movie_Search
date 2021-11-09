let nav_search =  document.getElementById('nav-search');
let nav_about =  document.getElementById('nav-about');
let nav_add_movies =  document.getElementById('nav-add-movies');
let nav_home =  document.getElementById('nav-home');
let search_button_html = "<button><i class=\"fa fa-search\" style=\"font-size:0.8rem\"></i></button>";

nav_search.addEventListener('click', function(event) {
    if((nav_search.children[0].tagName !== "BUTTON") & (event.target.tagName == 'I')){
        nav_search.innerHTML = search_button_html;
    } else if (nav_search.children[0].tagName == "BUTTON"){
        nav_search.innerHTML = create_form_html();
    };
});

nav_about.addEventListener('click', function() {
    let url = encodeURI('/about');
    window.open(url, '_self');
}
);

nav_home.addEventListener('click', function() {
    let url = encodeURI('/');
    window.open(url, '_self');
}
);

nav_add_movies.addEventListener('click', function() {
    let url = encodeURI('/addmovies');
    window.open(url, '_self');
}
);






function create_form_html(){
    let input_html =  "<input type='text' id='query' name='query' class='form-control form-input' style='font-size:0.8rem;height:27px' placeholder='Search Movies...'>";
    let search_symbol =  "<i class='fa fa-search' style='font-size:0.8rem; top:9px; left:15px'></i>";
    let form_html = "<form autocomplete='off' action='/search/' method='get' class='form' style='max-width=20rem;box-shadow: 0 0 1em 0.1em rgb(100 132 179);'>" + 
                    search_symbol + input_html + "</form>";
    return form_html;
}