<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
        <meta charset="UTF-8">
        <style type="text/css">
html, body, #content {
    margin: 0;
    padding: 0;
    border: 0 none;
    height: 100%;
    min-height: 100%;
    overflow: hidden;
}

#header {
    height: 40px;
    width: 100%;
    background-color: #b1fbfc;
}

#footer {
    z-index: 2;
    height: 50px;
    width: 100%;
    border: 2px solid black;
    padding: 1px;
    font-family: Arial, Verdana, Sans-serif;
    font-size: 12px;
}

#tac {
    position: absolute;
    display: block;
    top: 4px;
    left: 4px;
    padding: 2px;
    font-family: Arial, Verdana, Sans-serif;
    font-size: 14px;
    font-weight: bold;
    white-space: nowrap;
}

#title {
    display: block;
    margin-left: auto;
    margin-right: auto;
    padding-top: 6px;
    width: 25%;
    font-family: Arial, Verdana, Sans-serif;
    font-size: 24px;
    font-weight: bold;
    text-align: center;
    white-space: nowrap;
}

#cpbutton {
    position: absolute;
    z-index: 2;
    top: 47px;
    right: 116px;
    width: 40px;
    height: 18px;
    background-color: #FFFFFF;
    border: 1px solid grey;
    border-radius: 1px;
    padding: 0px 0px 0px 0px;
    font-family: Arial, Verdana, Sans-serif;
    font-size: 14px;
    font-weight: normal;
    text-align: center;
}

#cpbutton:hover {
    background-color: #F0F0F0;
}

.close {
    display: block;
    position: absolute;
    top: 10px;
    right: 10px;
    font-weight: bold;
}

#cpclose:hover {
    color: red;
    cursor: pointer;
}

#cpanel {
    position: absolute;
    z-index: 2;
    top: 96px;
    right: 10px;
    width: 200px;
    height: 250px;
    background-color: #FFFFFF;
    border: 2px solid black;
    border-radius: 5px;
    padding: 10px;
    font-family: Arial, Verdana, Sans-serif;
    font-size: 14px;
}

.cpattribute {
    width: 160px;
    margin: 4px;
    border: 1px solid #c0c0c0;
    font-size: 12px;
}

#errorMessage {
    position: absolute;
    display: none;
    z-index: 2;
    top: 200px;
    right: 250px;
    width: 400px;
    height: 200px;
    background-color: #FFFFFF;
    border: 2px solid black;
    border-radius: 5px;
    padding: 10px;
    font-family: Arial, Verdana, Sans-serif;
    font-size: 14px;
}

#mapCanvas {
    z-index: 1;
    margin: 2px 2px 2px 2px;
    padding: 0;
    height: 100%;
}

.mapPopup {
    position: absolute;
    display: none;
    background-color: #FFFFFF;
    border: 2px solid #004C92;
    border-radius: 5px;
    padding: 10px;
    font-family: Arial, Verdana, Sans-serif;
    font-size: 11px;
}

.mapPopup .popupClose {
    color: blue;
    float: right;
    font-weight: bold;
    font-family: Arial, Verdana, Sans-serif;
    font-size: 11px;
    cursor: pointer;
    border: 1px solid black;
    border-radius: 2px;
    padding: 1px 3px 0px 3px;
}
        </style>
        <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>
        <script type="text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
        <script type="text/javascript">


var model = {
    title:      'Kart over Enhetsregisteret',
    jsonURL:    'https://api.scraperwiki.com/api/1.0/datastore/sqlite',
    schemas:    [ 'enhetsregister' ],
    query:      'select * from `swdata`,
    dataFormat: 'jsondict',
    dataSets:   new Array(),
    images:     new Array(),
    colours:    [ "FE7569", "4D90FE", "FF0000", "00FF00", "0000FF", "FFFFFF" ],
    mapOptions: {
        zoom: 8,
        center: new google.maps.LatLng(51.500000, -1.000000),
        mapTypeId: google.maps.MapTypeId.ROADMAP
    },
    gMap:       null,
    gMarkers:   null,
};


$(document).ready(function() {
    //$('#scraperwikipane').css('top', '6px')
    //                     .css('right', '140px');

    document.title = model.title;
    $('#title').text(model.title);

    $('#cpanel').hide();
    $('#cpbutton').click(function() {
        $('#cpanel').slideDown();
    });

    $('.close').click(function() {
        $(this).parent().slideUp();
    });

    $('.cpattribute img').attr('width', 12)
                         .attr('height', 20);
    $('#cpapptype_other').prev().attr('src', getIcon(0).url);
    $('#cpapptype_hydro').prev().attr('src', getIcon(1).url);

    $('#cpapptype_other').click(refreshMapMarkers);
    $('#cpapptype_hydro').click(refreshMapMarkers);
    $('#cp_refresh').click(loadData);

    createMap();
    loadData();
} );


function loadData() {

    clearMapMarkers();
    model.dataSets = new Array();

    for (var r=0; r<model.schemas.length; r++) {
        var schema = model.schemas[r];
        $.ajax( {
            url: model.jsonURL,
            dataType: 'jsonp',
            data: {
                name:   schema,
                query:  model.query,
                format: model.dataFormat
            },
            success: function(data){
                model.dataSets.push(data);
                addMarkers(data);
            },
            error: function(object, status) {
                var msg = 'Failed to retrieve data for '+schema+' ('+status+'), try again';
                errorMsg(msg);
            }
        } );
    }
}


// Create map (first time through)
function createMap() {
    if (!model.gMap)
        model.gMap = new google.maps.Map($('#mapCanvas')[0], model.mapOptions);
}


// Clear existing markers, if any   
function clearMapMarkers() {
    if (model.gMarkers) {
        for (var i=0; i<model.gMarkers.length; i++) {
            model.gMarkers[i].setMap(null);
        }
    }
    model.gMarkers = new Array();
}

 
function refreshMapMarkers() {
    clearMapMarkers();

    for (var i=0; i<model.dataSets.length; i++) {
        var dataSet = model.dataSets[i];
        addMarkers(dataSet);
    }
}


function addMarkers(dataSet) {
     for (var j=0; j<dataSet.length; j++) {
         if (showDataPoint(dataSet[j])) {
             addMarker(model.gMap, dataSet[j]);
         }
     }
 }
 
 
function showDataPoint(point) {
    if (!point|| !point.lat || !point.lng)
        return false;

    var form = document.forms['controls'];
    if (point.hydroelectric && !form.th.checked)
        return false;

    if (!point.hydroelectric && !form.to.checked)
        return false;

    return true;
}


function addMarker(map, point) {
    var icon;
    if (point.hydroelectric)
        icon = getIcon( point.locid );
    else
        icon = getIcon( 0 );
    var markerPos = new google.maps.LatLng(point.lat, point.lng);
    var markerOptions = {
        position: markerPos,
        map: map,
        title: point.site_name,
        icon: icon
    };
    var marker = new google.maps.Marker(markerOptions);
    model.gMarkers.push(marker);
    addDetailPopup(map, marker, point);
 }


function addDetailPopup(map, marker, point) {

    var text = "<div>"+
               "<a target='EA_APPS' href='"+point.url+"'>"+point.site_name+"</a>"+
               "<br/>Grid ref: "+point.location+
               "<br/>Applicant: "+point.applicant+
               "<br/>Closing date: "+point.closing_date+
               "<br/>Data fetched: "+point.scrape_date+
               "</div>"+
               (point.hydroelectric ? "<div style='text-align:right;'><b>HYDROPOWER</b></div>" : "");

    google.maps.event.addListener(marker, 'click', function() {
        $('.mapPopup').remove();
        var infoBox = new InfoBox({content: text, latlng: marker.getPosition(), map: map});
    });    
}


function getIcon( n ) {
    n = (n % model.colours.length);
    if (model.images[n])
        return model.images[n];

    var pinColour = model.colours[n];
    var pinImage = new google.maps.MarkerImage(
            "http://chart.apis.google.com/chart?chst=d_map_pin_letter&chld=%E2%80%A2|" + pinColour,
            new google.maps.Size(21, 34),
            new google.maps.Point(0,0),
            new google.maps.Point(10, 34));
    model.images[n] = pinImage;
    return pinImage;
}



function errorMsg(message) {
    $('#errorMessage').append("<br/>"+message)
                      .show();
}


/* InfoBox extends GOverlay class from the Google Maps API  */
InfoBox.prototype = new google.maps.OverlayView();


/* An InfoBox is like an info window, but it displays
 * under the marker, opens quicker, and has flexible styling.
 * @param {GLatLng} latlng Point to place bar at
 * @param {Map} map The map on which to display this InfoBox.
 * @param {Object} opts Passes configuration options - content,
 *   offsetVertical, offsetHorizontal, className, height, width
 */
function InfoBox(opts) {
  google.maps.OverlayView.call(this);
  this.latlng_ = opts.latlng;
  this.map_ = opts.map;
  this.content_ = opts.content;
  this.offsetVertical_ = -100;
  this.offsetHorizontal_ =  25;
  this.width_ = 244;
  var me = this;
  this.boundsChangedListener_ =
    google.maps.event.addListener(this.map_, "bounds_changed", function() {
      return me.panMap.apply(me);
    });

  // Once the properties of this OverlayView are initialized, set its map so
  // that we can display it.  This will trigger calls to panes_changed and
  // draw.
  this.setMap(this.map_);
};

// Removes the DIV representing this InfoBox
InfoBox.prototype.remove = function() {
  if (this.div_ && this.div_.parentNode) {
    this.div_.parentNode.removeChild(this.div_);
    this.div_ = null;
  }
};

// Redraw the Bar based on the current projection and zoom level
InfoBox.prototype.draw = function() {
  // Creates the element if it doesn't exist already.
  this.createElement();
  if (!this.div_) return;

  // Calculate the DIV coordinates of two opposite corners of our bounds to
  // get the size and position of our Bar
  var pixPosition = this.getProjection().fromLatLngToDivPixel(this.latlng_);
  if (!pixPosition) return;

  // Now position our DIV based on the DIV coordinates of our bounds
  this.div_.style.width = this.width_ + "px";
  this.div_.style.left = (pixPosition.x + this.offsetHorizontal_) + "px";
  this.div_.style.top = (pixPosition.y + this.offsetVertical_) + "px";
  this.div_.style.display = 'block';
};

/* Creates the DIV representing this InfoBox in the floatPane.  If the panes
 * object, retrieved by calling getPanes, is null, remove the element from the
 * DOM.  If the div exists, but its parent is not the floatPane, move the div
 * to the new pane.
 * Called from within draw.  Alternatively, this can be called specifically on
 * a panes_changed event.
 */
InfoBox.prototype.createElement = function() {
  var panes = this.getPanes();
  var div = this.div_;
  if (!div) {
    // This does not handle changing panes.  You can set the map to be null and
    // then reset the map to move the div.
    div = this.div_ = document.createElement("div");
    div.style.width = this.width_ + "px";
    div.className = "mapPopup";
    var contentDiv = document.createElement("div");
    contentDiv.innerHTML = this.content_;

    var topDiv = document.createElement("div");
    topDiv.className = "popupClose";
    topDiv.innerHTML = "X";

    function removeInfoBox(ib) {
      return function() {
        ib.setMap(null);
      };
    }

    google.maps.event.addDomListener(topDiv, 'click', removeInfoBox(this));

    div.appendChild(topDiv);
    div.appendChild(contentDiv);
    div.style.display = 'none';
    panes.floatPane.appendChild(div);
    this.panMap();
  } else if (div.parentNode && (div.parentNode != panes.floatPane)) {
    // The panes have changed.  Move the div.
    div.parentNode.removeChild(div);
    panes.floatPane.appendChild(div);
  } else {
    // The panes have not changed, so no need to create or move the div.
  }
}

// Pan the map to fit the InfoBox.
InfoBox.prototype.panMap = function() {
  // if we go beyond map, pan map
  var map = this.map_;
  var bounds = map.getBounds();
  if (!bounds) return;

  // The position of the infowindow
  var position = this.latlng_;

  // The dimension of the infowindow
  var iwWidth = this.width_;
  var iwHeight = this.height_;

  // The offset position of the infowindow
  var iwOffsetX = this.offsetHorizontal_;
  var iwOffsetY = this.offsetVertical_;

  // Padding on the infowindow
  var padX = 0;
  var padY = 0;

  // The degrees per pixel
  var mapDiv = map.getDiv();
  var mapWidth = mapDiv.offsetWidth;
  var mapHeight = mapDiv.offsetHeight;
  var boundsSpan = bounds.toSpan();
  var longSpan = boundsSpan.lng();
  var latSpan = boundsSpan.lat();
  var degPixelX = longSpan / mapWidth;
  var degPixelY = latSpan / mapHeight;

  // The bounds of the map
  var mapWestLng = bounds.getSouthWest().lng();
  var mapEastLng = bounds.getNorthEast().lng();
  var mapNorthLat = bounds.getNorthEast().lat();
  var mapSouthLat = bounds.getSouthWest().lat();

  // The bounds of the infowindow
  var iwWestLng = position.lng() + (iwOffsetX - padX) * degPixelX;
  var iwEastLng = position.lng() + (iwOffsetX + iwWidth + padX) * degPixelX;
  var iwNorthLat = position.lat() - (iwOffsetY - padY) * degPixelY;
  var iwSouthLat = position.lat() - (iwOffsetY + iwHeight + padY) * degPixelY;

  // calculate center shift
  var shiftLng =
      (iwWestLng < mapWestLng ? mapWestLng - iwWestLng : 0) +
      (iwEastLng > mapEastLng ? mapEastLng - iwEastLng : 0);
  var shiftLat =
      (iwNorthLat > mapNorthLat ? mapNorthLat - iwNorthLat : 0) +
      (iwSouthLat < mapSouthLat ? mapSouthLat - iwSouthLat : 0);

  // The center of the map
  var center = map.getCenter();

  // The new map center
  var centerX = center.lng() - shiftLng;
  var centerY = center.lat() - shiftLat;

  // center the map to the new shifted center
  map.setCenter(new google.maps.LatLng(centerY, centerX));

  // Remove the listener after panning is complete.
  google.maps.event.removeListener(this.boundsChangedListener_);
  this.boundsChangedListener_ = null;
};
        </script>
    </head>
    <body>
      <div id="content">
        <div id="header">
            <div id="tac"><a href="http://www.rivertac.org/">TAC</a></div>
            <div id="title"></div>
        </div>
        <div id="mapCanvas"></div>
        <div id="cpbutton">Key</div>
        <div id="cpanel">
            <div id="cpclose" class="close">[X]</div>
            Key
            <form name="controls">
                <table class="cpattribute">
                <tr><td>Application type</td></tr>
                <tr><td><img/><input id="cpapptype_hydro" type="checkbox" name="th" checked="yes">
                              <label for="type_hydro">Hydropower</label></td></tr>   
                <tr><td><img/><input id="cpapptype_other" type="checkbox" name="to" checked="yes">
                              <label for="type_other">Other</label></td></tr>   
                </table>
                <table class="cpattribute">
                <tr><td>Application status</td></tr>
                <tr><td><img/><input id="cpappstate_open" type="checkbox" name="so" checked="yes">
                              <label for="state_open">Open for comments</label></td></tr>  
                <tr><td><img/><input id="cpappstate_approved" type="checkbox" name="sa">
                              <label for="state_approved">Approved</label></td></tr>
                <tr><td><img/><input id="cpappstate_rejected" type="checkbox" name="sr">
                              <label for="state_rejected">Rejected</label></td></tr>   
                </table>
                <input id="cp_refresh" type="button" value="Refresh"/>
            </form>
            <div id="errorMessage">
              <div id="emclose" class="close">[X]</div>
              Error messages
            </div>
        </div>
      </div>
    </body>
<html>
