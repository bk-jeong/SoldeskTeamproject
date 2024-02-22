//alert("chack");

let dragged;
const sources = document.getElementsByClassName("imgtag");

for (let index = 0; index < sources.length; index++) {
  var source = sources.item(index);

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
      false
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

document.getElementById("send").onclick = function () {
  var sicon = "";
  var tia = [, , , , ,];
  var T = 0;

  const lains = document.getElementsByClassName("renkin");
  for (let index = 0; index < lains.length; index++) {
    var lain = lains.item(index);
    var icons = lain.getElementsByClassName("imgtag");
    for (let index = 0; index < icons.length; index++) {
      var icon = icons.item(index);
      if (sicon == "") {
        sicon = sicon + icon.id;
      } else {
        sicon = sicon + "," + icon.id;
      }
    }
    tia[T] = sicon;
    sicon = "";
    T++;
  }

  var raid = "";
  for (var radio of document.getElementsByName("shop")) {
    if (radio.checked) {
      raid = radio.value
    }
  }

  const form = document.createElement("form");
  form.setAttribute("method", "post");
  form.setAttribute("action", "res/");

  const Raid = document.createElement("input");
  Raid.setAttribute("type", "hidden");
  Raid.setAttribute("name", "raid");
  Raid.setAttribute("value", raid);

  const Atia = document.createElement("input");
  Atia.setAttribute("type", "hidden");
  Atia.setAttribute("name", "1tia");
  Atia.setAttribute("value", data[0]);

  const Btia = document.createElement("input");
  Btia.setAttribute("type", "hidden");
  Btia.setAttribute("name", "2tia");
  Btia.setAttribute("value", data[1]);

  const Ctia = document.createElement("input");
  Ctia.setAttribute("type", "hidden");
  Ctia.setAttribute("name", "3tia");
  Ctia.setAttribute("value", data[2]);

  const Dtia = document.createElement("input");
  Dtia.setAttribute("type", "hidden");
  Dtia.setAttribute("name", "4tia");
  Dtia.setAttribute("value", data[3]);

  const Etia = document.createElement("input");
  Etia.setAttribute("type", "hidden");
  Etia.setAttribute("name", "5tia");
  Etia.setAttribute("value", data[4]);

  const Tierout = document.createElement("input");
  Tierout.setAttribute("type", "hidden");
  Tierout.setAttribute("name", "tierout");
  Tierout.setAttribute("value", data[5]);

  form.appendChild(Raid);
  form.appendChild(Atia);
  form.appendChild(Btia);
  form.appendChild(Ctia);
  form.appendChild(Dtia);
  form.appendChild(Etia);
  form.appendChild(Tierout);

  document.body.appendChild(form);
  form.submit();
};
