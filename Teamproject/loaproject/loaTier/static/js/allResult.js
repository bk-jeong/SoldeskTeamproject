// alert("chack");

window.onload = function(){

const tooltip_target = document.querySelectorAll(".ebox")
const tooltip = document.querySelectorAll(".tooltip_image")

// change display to 'block' on mouseover

// function displayblock(element){
//             element.style.display = 'block';
// }

// function displaynone(element){
//     element.style.display = 'none';
// }



// for (var index = 0; index < tooltip_target.length; index++) {
   // this keyword 활용 -> 이벤트를 객체한테만 사용하기

  tooltip_target.addEventListener('mouseover', () => {
      this.tooltip.style.display = 'block';
}, true);

  // change display to 'none' on mouseleave
  tooltip_target[index].addEventListener('mouseleave', () => {
      tooltip[0].style.display = 'none';
  }, false);
       

  
// }




}