  function initMap() {
		var directionsService = new google.maps.DirectionsService;
        var directionsDisplay = new google.maps.DirectionsRenderer;
		
		  directionsDisplay.setPanel(document.getElementById('directions-panel'));
		  directionsDisplay.setMap(map);
		
	
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
		 var points = [];
		 var geocoder = new google.maps.Geocoder();
        document.getElementById('submit').addEventListener('click', function() {
          geocodeAddress(geocoder, map, points);
        });
		
		document.getElementById('directions').addEventListener('click', function(){

			calculateAndDisplayRoute(directionsService, directionsDisplay, points);
			
      });
	

  // Function to find the locations on the map of bars
      function geocodeAddress(geocoder, resultsMap, points) {

        // Making sure the searches are local to Glasgow
        var address = document.getElementById('address').value + "glasgow";

        geocoder.geocode({'address': address}, function(results, status) {
          if (status === 'OK') {
            resultsMap.setCenter(results[0].geometry.location);
            // Set a marker on the location
            var marker = new google.maps.Marker({
              map: resultsMap,
              position: results[0].geometry.location
            });

            // Keep track of all bars added
			points.push(address);

          } else {
            alert('Geocode was not successful for the following reason: ' + status);
          }
        });
      }

 }
  function calculateAndDisplayRoute(directionsService, directionsDisplay, points) {

		var start = points.shift();
		var end = points.pop();
        var waypts = [];

        // Put waypoints into proper format
        for (var i = 0; i < points.length; i++) {
            waypts.push({ location: points[i]});
          
        }

		if(!(start==null || end==null || waypts.length < 1)) {
            console.log("Waypoints (waypts)", waypts);
            var request = {
                origin: start,
                destination: end,
                waypoints: waypts,
                optimizeWaypoints: true,
                travelMode: 'WALKING'
            };
            directionsService.route(request, function (response, status) {

                if (status === 'OK') {
                    directionsDisplay.setDirections(response);
                    var ser = JSON.stringify(request);
                    console.log(ser);
                    // Get the save button
                    var saveButton = document.getElementById('save');
                    // Display the save button since a route has been found
                    saveButton.style.display = 'block';
                    // Save route

                    document.getElementById('save').addEventListener('click', function () {

                        saveRoute(start, end, waypts, points);

                    });
                } else {
                    window.alert('Directions request failed due to ' + status);
                }
            });
        }   else{
            location.reload();
                }
      }

      function saveRoute(start, end, waypts, points){
          // Save variables to session storage
          sessionStorage.setItem('start', start);
          sessionStorage.setItem('end', end);
          sessionStorage.setItem('waypts_string', points.join());
          sessionStorage.setItem('waypts_formap', JSON.stringify(waypts));
          window.location.href="/crawlr/save_route";



      }
	  