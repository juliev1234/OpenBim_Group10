/* written by Tim McGinley 2022 */

// ok in here we need to include a lot of stuff.
// we need a menu... where would this fit?
// we need to start (over)loading stuff into the DOM.
// we need to split the screen into section and plan and KPIs and info - where should this go?


function main() {
	
	// calculate the floors
	const floors = document.getElementsByTagName("floor-");
	let num_floors = floors.length;
	console.log(num_floors);

	// calculate the beams
	//const building = document.getElementsByTagName("building-");
	//let num_beams = building.beams;
	//console.log(num_beams);

	// calculate the beams
	//const building2 = document.getElementsByTagName("building-");
	//let num_walls = building2.walls;
	//console.log(num_walls);
	
	// add data to the properties box
	$('props-').prepend('Number of floors is '+num_floors+'<br>');
	$('props-').prepend('Site elevation is '+$('site-').attr('elev')+'<br>');
	$('props-').prepend('Number of beams is '+$('building-').attr('beams')+'<br>');
	$('props-').prepend('Number of walls is '+$('building2-').attr('walls')+'<br>');
	
	// load the plan so we can edit it
	plan('Welcome to this very exciting project');
	
	// The .each() method is unnecessary here:
	$( 'floor-' ).each(function() {
	console.log($(this)[0].innerHTML);
		$( this ).on("click", function(){
			//$('plan-').css("background-color","black");
			
			changePlan($(this).attr('name')+':'+$(this).attr('level')+'<br>'
			+"Number of walls is "+$(this).attr('wallamt'));
			//$( this ).innerHTML
		});
	});
	
	
}

function plan(text) {
jQuery('<div>', {
    id: 'plan',
    class: 'plan',
    title: 'click a floor to see the plan',
	html:text
}).appendTo('plan-');  
	
}

function changePlan(text) {
	$('#plan').html(text);
}





// <project-> - title etc.... | <site-> - also menu? site specific data?
// ---------------------------------------------------------------------
// <building-> - name of the building? this then needs to split in two...
// could also be more views and show a 3d? but maybe left is consistent
// ---------------------------------------------------------------------
// #section                   |               #plan
// this shows the floors      |      this shows a floor in plan         |
// in section                 |                 #plan                   |
//    <floor...->              -----------------------------------------
//                            |                 <properties->           |
// ---------------------------------------------------------------------