$(document).ready(function() {

	if (location.pathname == "/dashboard") {
		$("#classesPanel").hide();
		$.ajax({url: "/processSyllabus", method: "GET", complete: function(data) {
			$("#loadingspan").hide();
			$("#classesPanel").show();
			console.log(data.responseText);
		}})
		$("#loading").show();
	}


	
});
