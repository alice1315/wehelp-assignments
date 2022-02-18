function searchUser(){
    let username = document.getElementById("search-box").value;

    let reqUrl = `http://127.0.0.1:3000/api/members?username=${username}`;

    fetch(reqUrl, {method: "GET"}).then(function(resp){
        return resp.json();
    }).then(function(datas){
        let showMember = document.getElementById("show-member");

        if (datas["data"] != null){
            showMember.innerText = `${datas["data"]["name"]} (${datas["data"]["username"]})`;
        } else if(datas["data"] == null){
            showMember.innerText = "查無此帳號";
        };
    });

    return false;
};

function updateUser(){
    let reqUrl = `http://127.0.0.1:3000/api/member`;

    let data = {"name": document.getElementById("update-box").value};

    let fetchData = {
        method: "POST", 
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    };

    fetch(reqUrl, fetchData).then(function(resp){
        return resp.json();
    }).then(function(datas){
        let showStatus = document.getElementById("show-status");
        if (datas["ok"]){
            showStatus.innerText = `更新成功`;
        } else if (datas["error"]){
            showStatus.innerText = `更新失敗`;
        };
    });

    return false;
};
