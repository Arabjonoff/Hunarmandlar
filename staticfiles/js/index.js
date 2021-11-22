let body = document.body;
body.onscroll = ()=>{
	document.getElementById('searchInput').className = 'searchInput'
	document.getElementById('searchInput').value = ''
}
function longInput(){
    document.getElementById('searchInput').className = 'longinput'
}
let property = 0

function nextTo(){
	property+=339.5
let div = document.getElementById('first')
div.style = `margin-left:-${property}px; transition:all 0.3s;`
if(property >= 2716){
	property = -339.5}
	
}

function prewTo(){
property-=679
let div = document.getElementById('first')
div.style = `margin-left:-${property}px; transition:all 0.3s;`
if(property <= 0){
	property = 3055.5}

}


window.onload = ()=>{
  setInterval( ()=>{
  if(property >= 3055.5){
	property = -339.5}
  let div = document.getElementById('first')
  div.style = `margin-left:-${property}px; transition:all 0.3s;`
  property+=339.5

  },5000)

}

let delete_btn = document.querySelectorAll('.delete_btn')
let items_row = document.querySelectorAll('.items_row')
delete_btn.forEach( function(e) {
	e.onclick = ()=>{
		let btn_index = Array.prototype.indexOf.call(delete_btn, e)
		items_row[btn_index].style = "display:none;"
	}
});