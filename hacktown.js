function initialize() {
    var mapCanvas = document.getElementById('map');
    var mapOptions = {
      center: new google.maps.LatLng(44.0519, -123.0867),
      zoom: 8,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    var map = new google.maps.Map(mapCanvas, mapOptions);
  }
google.maps.event.addDomListener(window, 'load', initialize);