checkboxs=document.getElementsByClassName("bonus").length;

for (var i=0; i<checkboxs; i++){
    document.getElementsByClassName("bonus")[i].addEventListener('change',(e)=>{
        if (e.target.checked==false){
                document.getElementById("allbonus").checked=false
        }
    })
}


const stage4select=document.getElementById('stage4')
document.getElementById('auction').addEventListener('change',(e)=>{
    if (e.target.checked==true){
        stage4select.options[1].selected=true;
    }
})

stage4select.addEventListener('change',()=>{
    if (stage4select.options[0].selected==true){
        document.getElementById("auction").checked=false;
    }
})


invennum=0
function invencheck(){
    invenvalue=document.getElementById("inven").value
    if (invenvalue==""){
        document.getElementById("inven").value=invennum;
    }
    invennum=document.getElementById("inven").value
}

function hendscheck(){
    handvalue=document.getElementById("hands").value
    range ="9123456780"
    if (handvalue.length>1){
        str=document.getElementById("hands").value.toString();
        str=str.substr(1,1)
        num=Number(str)
        document.getElementById("hands").value=num
        if (num>5){
            document.getElementById("hands").value=5;
        }
    }
    if (range.indexOf(handvalue)==0){
        document.getElementById("hands").value=0;
    }
    if (num<5){
        document.getElementById("fstreward").checked=false
    } else {
        document.getElementById("fstreward").checked=true
    }
}


document.getElementById('collCalc').onclick=function(){
    var invenv = document.getElementById("inven").value;
    if (invenv<0){
        alert("소지 재료 개수는 0이상 이어야 합니다.")
        document.getElementById("inven").value=0;
        False
    }
    var stage1 = document.getElementById("stage1");
    var stage2 = document.getElementById("stage2");
    var stage3 = document.getElementById("stage3");
    var stage4 = document.getElementById("stage4");
    var stage1v= (stage1.options[stage1.selectedIndex].value);
    var stage2v= (stage2.options[stage2.selectedIndex].value);
    var stage3v= (stage3.options[stage3.selectedIndex].value);
    var stage4v= (stage4.options[stage4.selectedIndex].value);
    var handsv = document.getElementById("hands").value;
    var fstrewardv = document.getElementById("fstreward").checked;
    var stage1Plus = document.getElementById("stage1Plus").checked;
    var stage2Plus = document.getElementById("stage2Plus").checked;
    var stage3Plus = document.getElementById("stage3Plus").checked;
    var stage4Plus = document.getElementById("stage4Plus").checked;
    var auctionv = document.getElementById("auction").checked;
    
    opsion=[0,0,0,0]

    if (stage1v=="normal" || stage1Plus == true){
        opsion[0]=1
    } else if (stage1v=="normal" || stage1Plus == false){
        opsion[0]=2
    } else if (stage1v=="hard" || stage1Plus == true){
        opsion[0]=3
    } else if (stage1v=="hard" || stage1Plus == false){
        opsion[0]=4
    }
    if (stage2v=="normal" || stage2Plus == true){
        opsion[1]=1
    } else if (stage2v=="normal" || stage2Plus == false){
        opsion[1]=2
    } else if (stage2v=="hard" || stage2Plus == true){
        opsion[1]=3
    } else if (stage2v=="hard" || stage2Plus == false){
        opsion[1]=4
    }


    if (stage3v=="normal" || stage3Plus == true){
        opsion[2]=1
    } else if (stage3v=="normal" || stage3Plus == false){
        opsion[2]=2
    } else if (stage3v=="hard" || stage3Plus == true){
        opsion[2]=3
    } else if (stage3v=="hard" || stage3Plus == false){
        opsion[2]=4
    }


    if (stage4v=="hard" || stage4Plus == true){
        opsion[3]=3
    } else if (stage4v=="hard" || stage4Plus == false){
        opsion[3]=4
    }


    const form = document.createElement("form");
    form.setAttribute("method", "get");
    form.setAttribute("action", `/calc/`);

    const entries = document.createElement("input");
    entries.setAttribute("type", "hidden");
    entries.setAttribute("name", "entries");
    entries.setAttribute("value", opsion);

    const auction = document.createElement("input");
    auction.setAttribute("type", "hidden");
    auction.setAttribute("name", "auction");
    auction.setAttribute("value", auctionv);

    const fstreward = document.createElement("input");
    fstreward.setAttribute("type", "hidden");
    fstreward.setAttribute("name", "fstreward");
    fstreward.setAttribute("value", fstrewardv);

    const hands = document.createElement("input");
    hands.setAttribute("type", "hidden");
    hands.setAttribute("name", "hands");
    hands.setAttribute("value", handsv);

    const inven = document.createElement("input");
    inven.setAttribute("type", "hidden");
    inven.setAttribute("name", "inven");
    inven.setAttribute("value", invenv);

    form.appendChild(entries);
    form.appendChild(auction);
    form.appendChild(fstreward);
    form.appendChild(hands);
    form.appendChild(inven);

    document.body.appendChild(form);
    form.submit();

    

    
}