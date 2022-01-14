function init(){
    let reqURL = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
    let req = new XMLHttpRequest();

    req.open("GET", reqURL);
    req.responseType = "json";
    req.onload = function(){
        let datas = req.response;
        getSpots(datas, 0);
        loadMore(datas);
        toggleMenu();
    };
    req.send();
};

function getSpots(jsonObj, startN){
    let spots = jsonObj["result"]["results"];

    for(i = startN; i < startN + 8; i++){
        let spotItem = document.createElement("div");
        let spotPic = document.createElement("div");
        let spotImg = document.createElement("img");
        let spotName = document.createElement("div");

        spotItem.setAttribute("class", "item");
        spotPic.setAttribute("class", "pic")  
        spotName.setAttribute("class", "name");

        let imgUrl = "https://" + spots[i]["file"].split("https://")[1];
        spotImg.src = imgUrl;
        spotName.textContent = spots[i]["stitle"];

        document.getElementById("content").appendChild(spotItem);
        spotItem.appendChild(spotPic);
        spotPic.appendChild(spotImg);
        spotItem.appendChild(spotName);

    };
};

function loadMore(jsonObj){
    let load = document.getElementById("btn-load");
    let count = 0;
    let handler = function(){
        count += 1;
        getSpots(jsonObj, 8 * count);
    };
    load.addEventListener("click", handler);
};

function toggleMenu(){
    let ham = document.getElementById("btn-ham");
    let menu = document.getElementById("menu");
    let handler = function(){
        menu.classList.toggle("hide");
    };
    ham.addEventListener("click", handler);
};
