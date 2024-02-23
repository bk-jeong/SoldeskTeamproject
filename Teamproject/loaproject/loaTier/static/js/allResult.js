// alert("chack");

window.onload = function(){

const tooltip_target = document.querySelectorAll(".ebox")
const tooltip = document.querySelectorAll(".tooltip_image")


tooltip_target.forEach( function (ebox,index){
    ebox.addEventListener('mouseover',()=>{
      tooltip[index].style.display = 'block';
    })
  });

  // change display to 'none' on mouseleave
  tooltip_target.forEach(function(ebox,index){
    ebox.addEventListener('mouseleave', () => {
      tooltip[index].style.display = 'none';
    })
  }, false);
  



}