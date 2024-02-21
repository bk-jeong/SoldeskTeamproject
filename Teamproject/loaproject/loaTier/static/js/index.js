//alert("chack");

let dragged;
const sources = document.getElementsByClassName("imgtag");

for (let index = 0; index < sources.length; index++) {
    var source= sources.item(index);

    // source.addEventListener("drag",(event) => {
    //     console.log("dragging");
    // });
    source.addEventListener("dragstart", (event) => {
        // store a ref. on the dragged elem
        dragged = event.target;
        // make it half transparent
        event.target.classList.add("dragging");
    });
    
    source.addEventListener("dragend", (event) => {
        // reset the transparency
        event.target.classList.remove("dragging");
    });
      
    /* events fired on the drop targets */
    
    const targets = document.getElementsByClassName("renkin");
    for (let index = 0; index < targets.length; index++) {
      var target = targets.item(index);
      
      target.addEventListener(
          "dragover",
          (event) => {
            // prevent default to allow drop
            event.preventDefault();
          },
          false,
      );
      
      target.addEventListener("dragenter", (event) => {
          // highlight potential drop target when the draggable element enters it
          if (event.target.classList.contains("dropzone")) {
            event.target.classList.add("dragover");
          }
      });
        
      target.addEventListener("dragleave", (event) => {
          // reset background of potential drop target when the draggable element leaves it
          if (event.target.classList.contains("renkin")) {
            event.target.classList.remove("dragover");
          }
      });
        
      target.addEventListener("drop", (event) => {
          // prevent default action (open as link for some elements)
          event.preventDefault();
          // move dragged element to the selected drop target
          if (event.target.classList.contains("renkin")) {
            event.target.classList.remove("dragover");
            event.target.appendChild(dragged);
          }
      });
    }

}

document.getElementById("send").onclick = function(){
  var sicon="";
  var tia=[,,,,,];
  var T=0;
  const lains =document.getElementsByClassName("renkin");
  for (let index = 0; index < lains.length; index++) {
    var lain= lains.item(index); 
    var icons= lain.getElementsByClassName("imgtag"); 
    for (let index = 0; index < icons.length; index++) {
      var icon=icons.item(index);
      if (sicon==""){
        sicon= sicon+ icon.id;
      } else {
        sicon= sicon+"," +icon.id;
      }
    }
    tia[T]=sicon;
    sicon="";
    T++;
  }
  alert(tia[0]);
  const form=document.createElement('form');
  form.setAttribute('method','post');
  form.setAttribute('action',"res/");

  const Atia=document.createElement('input');
  Atia.setAttribute('type','hidden');
  Atia.setAttribute('name','1tia');
  Atia.setAttribute('value',tia[0]);

  const Btia=document.createElement('input');
  Btia.setAttribute('type','hidden');
  Btia.setAttribute('name','2tia');
  Btia.setAttribute('value',tia[1]);

  const Ctia=document.createElement('input');
  Ctia.setAttribute('type','hidden');
  Ctia.setAttribute('name','3tia');
  Ctia.setAttribute('value',tia[2]);

  form.appendChild(Atia);
  form.appendChild(Btia);
  form.appendChild(Ctia);

  document.body.appendChild(form);
  form.submit();
};

  



// let dragged;

// const source = document.getElementById("1img");

// source.addEventListener("drag",(event) => {
//     console.log("dragging");
// });
// source.addEventListener("dragstart", (event) => {
//     // store a ref. on the dragged elem
//     dragged = event.target;
//     // make it half transparent
//     event.target.classList.add("dragging");
// });

// source.addEventListener("dragend", (event) => {
//     // reset the transparency
//     event.target.classList.remove("dragging");
// });
  
// /* events fired on the drop targets */
// const target = document.getElementById("Aicon");
// target.addEventListener(
//     "dragover",
//     (event) => {
//       // prevent default to allow drop
//       event.preventDefault();
//     },
//     false,
// );

  
// target.addEventListener("dragenter", (event) => {
//     // highlight potential drop target when the draggable element enters it
//     if (event.target.classList.contains("dropzone")) {
//       event.target.classList.add("dragover");
//     }
// });
  
// target.addEventListener("dragleave", (event) => {
//     // reset background of potential drop target when the draggable element leaves it
//     if (event.target.classList.contains("renkin")) {
//       event.target.classList.remove("dragover");
//     }
// });
  
// target.addEventListener("drop", (event) => {
//     // prevent default action (open as link for some elements)
//     event.preventDefault();
//     // move dragged element to the selected drop target
//     if (event.target.classList.contains("renkin")) {
//       event.target.classList.remove("dragover");
//       event.target.appendChild(dragged);
//     }
// });