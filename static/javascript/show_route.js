  function calculateAndDisplayRoute(directionsService, directionsDisplay) {
        // Take in waypoints from database
		var waypts =[];
        var waypts_array = waypts_string.split(",");

		// Put it into the format required for the maps API
        for (var i = 0; i < waypts_array.length; i++) {
            waypts.push({ location: waypts_array[i]});
          
        }

		// Request for maps
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

          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
      }
	  