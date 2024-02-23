alert(document.getElementById("select1").value)
document.getElementById("viewAllResult").onclick = function () {
  const form = document.createElement("form");
  form.setAttribute("method", "post");
  form.setAttribute("action", "all/");

  var raid = document.getElementById("select1").value
  const Raid = document.createElement("input");
  Raid.setAttribute("type", "hidden");
  Raid.setAttribute("name", "raid");
  Raid.setAttribute("value", raid);

  form.appendChild(Raid);
  document.body.appendChild(form);

  form.submit();
};
