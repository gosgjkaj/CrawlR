function calculateAndDisplayRoute(directionsService, directionsDisplay) {
      // Get the variables required from find_directions
      // Get waypoints in correct format for map
       var wayptsString = sessionStorage.getItem('waypts_formap');
       var waypts = JSON.parse(wayptsString);

       // Get the variables from find_directions (session storage)
       var start = sessionStorage.getItem('start')
       var end = sessionStorage.getItem('end');
       var waypts_string = sessionStorage.getItem('waypts_string');

		var request = {
          origin: start,
          destination: end,
          waypoints: waypts,
          optimizeWaypoints: true,
          travelMode: 'WALKING'
        };
        directionsService.route(request, function(response, status) {

          if (status === 'OK') {
            directionsDisplay.setDirections(response);
              sendData(start, end, waypts_string);

          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
      }

function sendData(start, end, waypts_string){
  // Put values into django hidden fields in form
      document.getElementById("id_start").value = start;
      document.getElementById("id_end").value = end;
      document.getElementById("id_waypts").value = waypts_string;


}