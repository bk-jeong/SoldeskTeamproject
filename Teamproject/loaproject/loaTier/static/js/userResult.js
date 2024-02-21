document.getElementById("viewAllResult").onclick = function () {
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
  radios = document.getElementsByName("shop");
  for (var radio of radios) {
    if (radio.checked) {
      alert(radio.value);
    }
  }

  //alert(tia[0]);
  const form = document.createElement("form");
  form.setAttribute("method", "post");
  form.setAttribute("action", "allRes/");

  const Atia = document.createElement("input");
  Atia.setAttribute("type", "hidden");
  Atia.setAttribute("name", "1tia");
  Atia.setAttribute("value", tia[0]);

  const Btia = document.createElement("input");
  Btia.setAttribute("type", "hidden");
  Btia.setAttribute("name", "2tia");
  Btia.setAttribute("value", tia[1]);

  const Ctia = document.createElement("input");
  Ctia.setAttribute("type", "hidden");
  Ctia.setAttribute("name", "3tia");
  Ctia.setAttribute("value", tia[2]);

  form.appendChild(Atia);
  form.appendChild(Btia);
  form.appendChild(Ctia);

  document.body.appendChild(form);
  form.submit();
};
