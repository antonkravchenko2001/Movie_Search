const form = document.getElementById("searh_form");
const inp = document.getElementById("query");

inp.addEventListener(
    'keyup',
     function(){
        const url = `/autocomplete_rest?q=${inp.value}`;
            fetch(url)
            .then(res => res.json())
            .then(data => {
                let div = document.getElementById("result");
                div.innerHTML = "";
                let list = "";
                let matches = data["matches"];
                let search_url;
                for(let match of matches){
                    list += "<li name=\"suggestion\">" + "<button name=\"autobutton\" type=\"button\">" + match  + "</button>" + "</li>";
                }
                if (matches.length > 0){
                    form.style.cssText += "padding-bottom:25px;"
                } else {
                    form.style.cssText += "padding-bottom:0px;"
                }
                div.innerHTML = list;
                let buttons = document.getElementsByName("autobutton");
                let lists = document.getElementsByName("suggestion");
                lists.forEach((lis) => {
                    lis.classList.add("li-button");
                });
                buttons.forEach((but) => {
                    but.classList.add("auto-button");
                });
                buttons.forEach((btn) => {
                    btn.addEventListener("click", function(){
                        let url = encodeURI(`/search?selection=${btn.innerHTML}`)
                        window.open(url,"_self");
                    });
                });
        })
    }
);