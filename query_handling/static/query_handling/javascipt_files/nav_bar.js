let headerGroup = document.getElementsByClassName('header-group')[0];
let hamburger = document.getElementsByClassName('hamburger')[0];

let search =  document.getElementById('header-search');
let about =  document.getElementById('header-about');
let addMovies =  document.getElementById('header-addmovies');
let home =  document.getElementById('header-home');

const searchIcon = "<i class='fa fa-search' style='font-size: 0.8rem'></i>";



search.addEventListener('click', function(event) {
    if((search.children[0].tagName !== "BUTTON") & (event.target.tagName == 'I')){
        search.innerHTML = "<button>" + searchIcon + "</button>";
    } else if (search.children[0].tagName == "BUTTON"){
        search.innerHTML = create_form_html();
    };
});



about.addEventListener('click', function() {
    let url = encodeURI('/about');
    window.open(url, '_self');
}
);

home.addEventListener('click', function() {
    let url = encodeURI('/');
    window.open(url, '_self');
}
);

addMovies.addEventListener('click', function() {
    let url = encodeURI('/addmovies');
    window.open(url, '_self');
    }
);

hamburger.addEventListener('click', function() {
    headerGroup.classList.toggle('active');
}
);

function create_form_html(){
    let input_html =  "<input type='text' id='query' name='query' class='header-form-input' placeholder='Search Movies...'>";
    let search_symbol =  "<i class='fa fa-search header-search-icon'></i>";
    let form_html = "<form autocomplete='off' action='/search/' method='get' class='header-form'>" + 
                    search_symbol + input_html + "</form>";
    return form_html;
}