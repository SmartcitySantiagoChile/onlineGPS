"use strict";
(function (dtpmMapOperations, window) {

    // attach your functions to the global 'DTPM' variable
    if(typeof window !== "undefined") {
        window.DTPM = dtpmMapOperations;
    }
}({
    /**
     * the next three function fetch the next data 
     * from server:
     *  - grid
     *  - route services
     *  - service information
     *  - bus stops
     *
     * Original data came from TranSapp project.
     * To parser data from csv to json, we use 
     * http://www.convertcsv.com/csv-to-json.htm
     */
    
    /**
     * fetch grid data, route data, and service data from server 
     *
     * @parameter successFunction Function that receives 3 parameter:
     *                            gridData, routeData and serviceData.
     * @parameter dataUrl         path to the json data
     */
    loadData: function (successFunction, dataUrl) {
        
        // add dataUrl to the object
        this.dataUrl = dataUrl;
        // add data to the object
        this.data = {};
        // to use inside ajax functions
        var libraryData = this.data;
        
        // filenames
        var extension = '.json';
        var gridFileName =    'grid'     + extension;
        var routeFileName =   'routes'   + extension;
        var serviceFileName = 'services' + extension;
        var stopFileName =    'busstops' + extension;
        
        var pathToFiles = dataUrl + 'data/';
        
        var pathToGridFile =    pathToFiles + gridFileName;
        var pathToRouteFile =   pathToFiles + routeFileName;
        var pathToServiceFile = pathToFiles + serviceFileName;
        var pathToStopFile =    pathToFiles + stopFileName;
        
        // load grid data
        $.getJSON(pathToGridFile, function(data) {
            libraryData.grid = data;
            console.log('grid data loaded successfully');
            
            // load route data
            $.getJSON(pathToRouteFile, function(data) {
                libraryData.route = data;
                console.log('route data loaded successfully');
                                
                // load service data
                $.getJSON(pathToServiceFile, function(data) {
                    libraryData.service = data;
                    console.log('service data loaded successfully');
                    
                    // load bus stop data
                    $.getJSON(pathToStopFile, function(data) {
                        libraryData.busStop = data;
                        console.log('bus stop data loaded successfully');
                        
                        successFunction();
                    }).fail(function(){
                        console.log("we could not load bus stop file.");
                    });                                
                }).fail(function(){
                    console.log("we could not load service file.");
                });                
            }).fail(function(){
                console.log("we could not load route file.");
            });    
        }).fail(function(){
            console.log("we could not load grid file.");
        });
    },
    
    setLayerControl: function(map) {
        // set tile layer
	var accessToken = "pk.eyJ1IjoiY2VwaGVpIiwiYSI6ImNrMzA0MHlvMjBsbmEzaHIzd24xNGV0NW0ifQ.5yTsjnoXTZ5ihlNbtf8cbw";
        var grayStyle= 'https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token=' + accessToken;
        var blackStyle='https://api.mapbox.com/styles/v1/mapbox/dark-v9/tiles/256/{z}/{x}/{y}?access_token=' + accessToken;
        var satelliteStyle = 'https://api.mapbox.com/styles/v1/mapbox/satellite-v9/tiles/256/{z}/{x}/{y}?access_token=' + accessToken;
        var outdoorStyle='https://api.mapbox.com/styles/v1/mapbox/outdoors-v9/tiles/256/{z}/{x}/{y}?access_token=' + accessToken;
        
        var attribution = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
                          'Imagery © <a href="http://mapbox.com">Mapbox</a>';
        
        var grayLayer = L.tileLayer(grayStyle, {attribution: attribution});
        var blackLayer = L.tileLayer(blackStyle, {attribution: attribution});
        var satelliteLayer = L.tileLayer(satelliteStyle, {attribution: attribution});
        var outdoorLayer = L.tileLayer(outdoorStyle, {attribution: attribution});
        
        // set default map
        grayLayer.addTo(map);
        
        var baseMaps = {
            "Gris": grayStyle,
            "Negro": blackStyle,
            "satelite": satelliteStyle,
            "outdoor": outdoorStyle,
        };
        // revisar porque no funciona
        //L.control.layers(baseMaps, {}).addTo(map);
        
        //return baseMaps;
        return grayLayer;
    },
    
    /** 
     * Calculate grid position and the cell id area. It uses grid data
     * 
     * @parameter point LatLng object
     * @return {x, y, rectangle} where the pair (x,y) is the grid id
     */
    getCellId: function(point) {
        // lower left corner
        var MIN_LATITUDE  = -33.6692;
        var MIN_LONGITUDE = -70.874;
        // upper right corner
        var MAX_LATITUDE  = -33.3193;
        var MAX_LONGITUDE = -70.4936;
        // width and height of each square
        var SIDE_LAT = 0.00349861;
        var SIDE_LON = 0.00380394;
        
        var iLat = parseInt((point.lat - MIN_LATITUDE) / SIDE_LAT);
        var iLon = parseInt((point.lng - MIN_LONGITUDE) / SIDE_LON);
        
        // cell area rectangle, if we want to draw on map
        var bounds = [[MIN_LATITUDE+iLat*SIDE_LAT, MIN_LONGITUDE+iLon*SIDE_LON],
                      [MIN_LATITUDE+(iLat+1)*SIDE_LAT, MIN_LONGITUDE+(iLon+1)*SIDE_LON]];
        var cellArea = L.rectangle(bounds, {color: "#000000", weight: 1});

        var value = {x: iLat, y: iLon, cellArea: cellArea};
        //console.log('grid position: (' + value.x + ',' + value.y + ')');
        return value;
    },

    /** 
     * get service list that cross cellId. It uses grid data 
     * 
     * @parameter cellId   Object with attribute (x, y, rectangle)
     * @return service list
     */
    getServices: function(cellId) {
        var services = [];
        $.each(this.data.grid, function(i, v) {
            if (v.iLat==cellId.x && v.iLon==cellId.y) {
                services=v.services.split('/');
                return false;
            }
        });
        //console.log('services: ' + services.join());
        
        return services;
    },
    
    /** 
     * get route for each service. It uses route data
     * 
     * @parameter services  String list with services
     * @return service routes based on service list
     */
    getRoutes: function (services) {
        var routes = [];
        var routeData = this.data.route;
        
        $.each(services, function(i, service) {
            var route = routeData[service];
            routes.push({service: service, route: route});
        });
        //console.log(routes);
        
        return routes;
    },
    
    /** 
     * DRAW FUNCTIONS
     */
     
    /** 
     * draw routes as polylines
     * 
     * @parameter routeLayer  Leaflet layer with the current routes drawed in map
     * @parameter routes      Array of routes
     */
    drawRoutes: function(routeLayer, routes) {
        routeLayer.clearLayers();        
        var serviceData = this.data.service;
        var self = this;
        $.each(routes, function(i, r){
            var points = [];
            $.each(r.route, function(i, p){
                points.push(L.latLng(p.latitud, p.longitud));
            });
            
            var serviceWithoutDirection = r.service.substring(0, r.service.length - 1);
            
            var polyline = L.polyline(points, {
                color: self.getRouteColor(serviceWithoutDirection), 
                smoothFactor: 5.0
                });
            routeLayer.addLayer(polyline);
        });
        
        return routeLayer;
    },
    
    /**
     * draw part of route as polylines
     *
     * @dependency turf
     *
     * @parameter routeLayer Leaflet layer where will save the polyline
     * @parameter route      route with direction, 506I
     * @parameter stopCode1  stop code 
     * @parameter stopCode2  stop code 
     */
    drawPartOfRoute: function (routeLayer, route, stopCode1, stopCode2) {

        var stop1 = this.data.busStop[stopCode1];
        var stop2 = this.data.busStop[stopCode2];
        var points = this.getRoutes([route])[0].route;

        var turfStopLoc1 = [stop1.latitude, stop1.longitude];
        var turfStopLoc2 = [stop2.latitude, stop2.longitude];
        var turfPoints = points.map(function(e){
	    return [e.latitud, e.longitud];
	});
	
    	var line = turf.lineString(turfPoints);
	var pt1 = turf.point(turfStopLoc1);
	var pt2 = turf.point(turfStopLoc2);
	var routePart = turf.lineSlice(pt1, pt2, line).geometry.coordinates;

        var serviceWithoutDirection = route.substring(0, route.length - 1);
        var polyline = L.polyline(routePart, {
            color: this.getRouteColor(serviceWithoutDirection),
            smoothFactor: 5.0
        });
        routeLayer.addLayer(polyline);

        return polyline;
    },
    
    /** 
     * draw bus stops for specific service
     * 
     * @parameter stopLayer Leaflet layer with the current stops drawed on map
     * @parameter service   Service name
     * @parameter direction Service direction
     */
    drawStopsForService: function(stopLayer, service, direction) {
        stopLayer.clearLayers();
            
        var stopIcon = this.getBusStopIcon();
        var stops = this.data.service[service]['stops' + direction].split('-');
        var stopData = this.data.busStop;
        $.each(stops, function(i, code){
            var stop = stopData[code];
            var latLng = L.latLng(stop.latitude, stop.longitude);
            var marker = L.marker(latLng, {
                icon: stopIcon, 
                zIndexOffset: -1000 // send stops below other layers
                });
            marker.bindPopup("<p>" + code + " - " + stop.name + "<br />" + i + "<br />" + stop.services + "</p>");
            stopLayer.addLayer(marker);
        });
        
        return stopLayer;
    },
    
    /** 
     * draw bus stops for specific service
     * 
     * @parameter stopLayer Leaflet layer with the current stops drawed on map
     * @parameter stops     Array of stops code
     */
    drawStops: function(stopLayer, stops) {
        stopLayer.clearLayers();
            
        var stopIcon = this.getBusStopIcon();
        var metroIcon = this.getMetroIcon();
        var stopData = this.data.busStop;
        $.each(stops, function(i, code){
            var stop = stopData[code];
            var latLng = L.latLng(stop.latitude, stop.longitude);
            var marker = L.marker(latLng, {
                icon: stop.type=='busstop'?stopIcon:metroIcon, 
                zIndexOffset: -1000 // send stops below other layers
                });
            marker.bindPopup("<p>" + code + " - " + stop.name + "<br />" + i + "<br />" + stop.services + "</p>");
            stopLayer.addLayer(marker);
        });
        
        return stopLayer;
    },
    
    /** 
     * draw services in web page, it uses bootstrap pills. It uses service data
     * 
     * @parameter id          tag id where pills are nested
     * @parameter pillClass   class id to identify pills
     * @parameter services    String list with services
     */
    drawlistServices: function(id, pillClass, services) {
        // clear list
        $('#'+id).empty();
        
        // add pills to list
        $.each(services, function(i, s){
            var serviceWithoutDirection = s.substring(0, s.length - 1);
            var direction = s.substring(s.length - 1, s.length);
            var serviceColor = this.data.service[serviceWithoutDirection].color;
            
            var liTagOpen = '<li role="presentation" class="' + pillClass + '" data-service="' + s + '">';
            var aTagOpen = '<a  style="background-color: #'+ serviceColor +'" href="#" data-toggle="tab">';
            var aContent = serviceWithoutDirection + ' <span class="badge">' + direction + '</span>';
            var aTagClose = '</a>';
            var liTagClose = '</li>';
            var element = liTagOpen + aTagOpen + aContent + aTagClose + liTagClose;
            
            $('#'+id).append(element);
        });
    },
    
    /** 
     * get leaflet icon to draw services in web page. It uses service data
     * 
     * @parameter service Service name that we need its icon.
     * @return L.icon object
     */
    getBusIcon: function(service, direction) {
        
        var colorId = this.data.service[service].color_id;
        var busId;
        
        switch(colorId) {
            case 1:
                busId = '02';
                break;
            case 2:
                busId = '03';
                break;
            case 3:
                busId = '04';
                break;
            case 4:
                busId = '05';
                break;
            case 5:
                busId = '06';
                break;
            case 6:
                busId = '07';
                break;
            case 7:
                busId = '08';
                break;
            default:
                busId = '01';
        }
        
        // doc: http://leafletjs.com/reference.html#icon
        var icon = L.icon({
            iconUrl: this.dataUrl + 'img/bus' + busId + direction +'.png',
            //shadowUrl: '',
            
            iconSize:     [52, 29], // size of the icon
            //shadowSize:   [50, 64], // size of the shadow
            iconAnchor:   [26, 15], // point of the icon which will correspond to marker's location
            //shadowAnchor: [26, 15],  // the same for the shadow
            popupAnchor:  [0, -14] // point from which the popup should open relative to the iconAnchor
        });
        
        return icon;
    },
    
    getBusStopIcon: function() {
        var icon = L.icon({
            iconUrl: this.dataUrl + 'img/paradero.png',
            //shadowUrl: '',
            
            iconSize:     [32, 48],   // size of the icon
            //shadowSize:   [50, 64], // size of the shadow
            iconAnchor:   [16, 48],   // point of the icon which will correspond to marker's location
            //shadowAnchor: [26, 15], // the same for the shadow
            popupAnchor:  [0, -48],    // point from which the popup should open relative to the iconAnchor
        });
        
        return icon;        
    }, 

    getMetroIcon: function() {
        var icon = L.icon({
            iconUrl: this.dataUrl + 'img/metro.png',
            //shadowUrl: '',
            
            iconSize:     [50, 41],   // size of the icon
            //shadowSize:   [50, 64], // size of the shadow
            iconAnchor:   [25, 20],   // point of the icon which will correspond to marker's location
            //shadowAnchor: [26, 15], // the same for the shadow
            popupAnchor:  [0, -41],    // point from which the popup should open relative to the iconAnchor
        });
        
        return icon;        
    }, 
    
    /** 
     * get hexadecimal color based on operator id
     * 
     * @parameter colorId color id related to operator of service.
     * @return hexadecimal color
     */
    getRouteColor: function (service) {
        var color;
        
        var colorId = this.data.service[service].color_id;
        
        switch(colorId) {
            case 1:
                color = '#ED1C24';
                break;
            case 2:
                color = '#F58220';
                break;
            case 3:
                color = '#FFD400';
                break;
            case 4:
                color = '#00D5FF';
                break;
            case 5:
                color = '#0067AC';
                break;
            case 6:
                color = '#00B33C';
                break;
            case 7:
                color = '#00D9A3';
                break;
	    // subway line 1
	    case 8:
                color = '#CD0424';
                break;
	    // subway line 2
	    case 9:
                color = '#DF6D0C';
                break;
	    // subway line 4
	    case 10:
                color = '#12275C';
                break;
	    // subway line 4a
	    case 11:
                color = '#285EA6';
                break;
	    // subway line 5
	    case 12:
                color = '#018464';
                break;
            default:
                color = '#ffffff';
        }
        
        return color;
    }
    
}, window));
