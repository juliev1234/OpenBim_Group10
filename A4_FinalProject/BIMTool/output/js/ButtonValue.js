var buttons = document.getElementsByTagName("button");
var buttonsCount = buttons.length;
for (var i = 0; i <= buttonsCount; i += 1) {
    buttons[i].onclick = function() {
        alert(this.id);
        //console.log("input"+this.id)
        var density = document.getElementById("input"+String(this.id)).value
        console.log(density)
    };
}