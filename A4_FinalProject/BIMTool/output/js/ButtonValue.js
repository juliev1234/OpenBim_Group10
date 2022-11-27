
// In progress weight calulator
var buttons = document.getElementsByTagName("button");
var buttonsCount = buttons.length;
for (var i = 0; i <= buttonsCount; i += 1) {
    buttons[i].onclick = function() {  
        var density = document.getElementById("input"+String(this.id)).value
        console.log(density)

        if (density) {
            alert(this.id+" has the value "+String(density));
          } else {
            alert(this.id+" has no value assigned");
        }
    };
}