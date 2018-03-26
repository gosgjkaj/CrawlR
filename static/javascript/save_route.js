

function initMap() {

		var directionsService = new google.maps.DirectionsService;
        var directionsDisplay = new google.maps.DirectionsRenderer;

		  directionsDisplay.setPanel(document.getElementById('directions-panel'));
		  directionsDisplay.setMap(map);
		calculateAndDisplayRoute(directionsService, directionsDisplay);

		  var nightMode = new google.maps.StyledMapType(
		  [
  {
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#242f3e"
      }
    ]
  },
  {
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#746855"
      }
    ]
  },
  {
    "elementType": "labels.text.stroke",
    "stylers": [
      {
        "color": "#242f3e"
      }
    ]
  },
  {
    "featureType": "administrative.locality",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#d59563"
      }
    ]
  },
  {
    "featureType": "poi",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#d59563"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#263c3f"
      }
    ]
  },
  {
    "featureType": "poi.park",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#6b9a76"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#38414e"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "geometry.stroke",
    "stylers": [
      {
        "color": "#212a37"
      }
    ]
  },
  {
    "featureType": "road",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#9ca5b3"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#746855"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "geometry.stroke",
    "stylers": [
      {
        "color": "#1f2835"
      }
    ]
  },
  {
    "featureType": "road.highway",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#f3d19c"
      }
    ]
  },
  {
    "featureType": "transit",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#2f3948"
      }
    ]
  },
  {
    "featureType": "transit.station",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#d59563"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "geometry",
    "stylers": [
      {
        "color": "#17263c"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "labels.text.fill",
    "stylers": [
      {
        "color": "#515c6d"
      }
    ]
  },
  {
    "featureType": "water",
    "elementType": "labels.text.stroke",
    "stylers": [
      {
        "color": "#17263c"
      }
    ]
  }
],
{name: 'Nightmode'});
		 // Create a map object, and include the MapTypeId to add
        // to the map type control.
        var glasgow = {lat: 55.864237, lng: -4.251805999999988};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: glasgow,
		   mapTypeControlOptions: {
            mapTypeIds: ['roadmap', 'satellite', 'hybrid', 'terrain',
                    'Nightmode']
          }
        });

		// Associate the styled map with the MapTypeId and set it to display.
		map.mapTypes.set('Nightmode', nightMode);
		map.setMapTypeId('roadmap');
		directionsDisplay.setMap(map);
 /*        var marker = new google.maps.Marker({
          position: glasgow,
          map: map
        }); */

		 // Using geocoding to find a pub or bar
		 // Will extend for up to 22 other bars / waypoints
		 // Then submit to retrieve google maps directions json fileCreatedDate

		 var geocoder = new google.maps.Geocoder();





 }
  function calculateAndDisplayRoute(directionsService, directionsDisplay) {
       var wayptsString = sessionStorage.getItem('waypts_formap');
       var waypts = JSON.parse(wayptsString);
		console.log("Waypoints correct",waypts);

        // Get the variables from find_directions (session storage)
    var start = sessionStorage.getItem('start');
    var end = sessionStorage.getItem('end');
    var waypts_string = sessionStorage.getItem('waypts_string');

    // Clear session storage
      sessionStorage.clear();

// Console logs for testing
    console.log("Start", start);
    console.log("End", end);
    console.log("Waypoints for database", waypts_string);

// Put values into django hidden fields in form
    document.getElementById("start").value = start;
    document.getElementById("end").value = end;
    document.getElementById("waypts").value = waypts_string;




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
			var ser = JSON.stringify(request);



          } else {
            window.alert('Directions request failed due to ' + status);
          }
        });
      }
