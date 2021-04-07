function initMap(){
  map = new google.maps.Map(document.getElementById('map'), {
      center: {lat: 1.357912699946735, lng: 103.86402586050852},
      zoom: 12,
      mapId: 'd06829fc6911d098',
      mapTypeControl: false,
      fullScreenControl: false,
      streetViewControl: false
    });

  const image_url = "https://freesvg.org/img/location_icon.png";
  const size1 = 30;
  const size2 = 20;

  let allMall = [];
  let allLat = [];
  let allLng = [];
  let allGroup = [];
  let allPopulation = [];
  let allLocation = [];
  let covidIndex = [];
  let covidLocation = [];
  
  //Fetch data from JSON file
  fetch("json/locationdata.json")
     .then(function(resp){
         return resp.json();
     })
     .then(function(data){
         for (let i=0; i<data.locationData.length; i++){
             allMall[i]=data.locationData[i].location;
         }

         for (let i=0; i<data.locationData.length; i++){
             var d = data.locationData[i].lat;
             allLat[i]=Number(d);
         }

         for (let i=0; i<data.locationData.length; i++){
             var d = data.locationData[i].lng;
             allLng[i]=Number(d);
         }
         for (let i=0; i<data.locationData.length; i++){
             allPopulation[i]=data.locationData[i].population;
         }
         //console.log(allPopulation);
         //console.log(allLng);

         for (let i=0; i<data.locationData.length; i++){
    
          const marker = new google.maps.Marker({
            position: {lat: allLat[i], lng: allLng[i]},
            map,
            icon: {
                url: image_url,
                scaledSize: new google.maps.Size(size1,size2)
            },
            animation: google.maps.Animation.DROP
          });
      
          const infowindow = new google.maps.InfoWindow({
            content: allMall[i],
          });
      
          marker.addListener("mouseover", () => {
              infowindow.open(map, marker);
            });
          marker.addListener("mouseout", () => {
              infowindow.close(map, marker);
            });
         }
          locationPath.setMap(map);
        } 
     })

  for (let i=0; i<locationmarkers.length; i++){
    const currentMarker=locationmarkers[i];

    const marker = new google.maps.Marker({
      position: {lat:currentMarker[1], lng: currentMarker[2]},
      map,
      icon: {
          url: image_url,
          scaledSize: new google.maps.Size(size1,size2)
      },
      animation: google.maps.Animation.DROP
    });

    const infowindow = new google.maps.InfoWindow({
      content: currentMarker[0],
    });

    marker.addListener("click", () => {
        infowindow.open(map, marker);
      });
}

//   for (const location in locationmap) {
//   // Add the circle for this city to the map.
//     const cityCircle = new google.maps.Circle({
//       strokeColor: "#FF0000",
//       strokeOpacity: 0.8,
//       strokeWeight: 2,
//       fillColor: "#FF0000",
//       fillOpacity: 0.35,
//       map,
//       center: locationmap[location].center,
//       radius: locationmap[location].population * 1000,
//   });
// }

  // var locationCoordinates = [
  //   { lat: locationmarkers[6][1], lng: locationmarkers[6][2] },
  //   { lat: locationmarkers[100][1], lng: locationmarkers[100][2] },
  // ];
  // const locationPath = new google.maps.Polyline({
  //   path: locationCoordinates,
  //   geodesic: true,
  //   strokeColor: "#FF0000",
  //   strokeOpacity: 3.0,
  //   strokeWeight: 2,
  // });
  // locationPath.setMap(map);
}


         fetch("json/personDetails.json")
            .then(function(resp){
                return resp.json();
            })
            .then(function(data){
                for (let i=0; i<data.details.length; i++){
                    allGroup[i]=data.details[i].group;
                }

                for (let i=0; i<data.details.length; i++){
                    allLocation[i]=data.details[i].location;
                }
                //console.log(allMall);

                for (let i=0; i<allGroup.length; i++){
                if (allGroup[i] == "covid"){
                    covidIndex.push(i);
                }
                }
                var index = 0;
                for (let i=0; i<covidIndex.length; i++){
                  covidLocation[i]=allLocation[covidIndex[index]];
                  index+=1;
                }
                //console.log(covidLocation);
                //console.log(covidLocation[0][3]);
                //console.log(covidLocation[0].length);
                for(let i=0; i<covidLocation.length; i++){
                  for(let j=0; j<covidLocation[i].length; j++){
                    for(let k=0; k<allMall.length; k++){
                      if(covidLocation[i][j] == allMall[k]){
                         allPopulation[k]+=1;
                      }
                    }
                  }
                }
                //console.log(locationmarkers[21][3]);
                for (let i = 0; i<allPopulation.length; i++){
                  // Add the circle for this city to the map.
                  if (allPopulation[i] != 0){
                    const cityCircle = new google.maps.Circle({
                      strokeColor: "#FF0000",
                      strokeOpacity: 0.8,
                      strokeWeight: 2,
                      fillColor: "#FF0000",
                      fillOpacity: 0.35,
                      map,
                      center: {lat: allLat[i], lng: allLng[i]},
                      radius: allPopulation[i] * 1000,


                  });
                  }
                }

                for(let i=0; i<covidLocation.length; i++){
                  let covidLocationIndex = [];
                  for(let j=0; j<covidLocation[i].length; j++){
                    for(let k=0; k<allPopulation.length; k++){
                      if(covidLocation[i][j] == allMall[k]){
                        covidLocationIndex.push(k);
                      }
                    }
                  }
                  var locationCoordinates = [];
                  var index=0;
                  for (let f=0; f<covidLocationIndex.length; f++){
                    locationCoordinates.push({ lat: allLat[covidLocationIndex[index]], lng: allLng[covidLocationIndex[index]]});
                    index+=1;
                  }
                  const locationPath = new google.maps.Polyline({
                    path: locationCoordinates,
                    geodesic: true,
                    strokeColor: "#000000",
                    strokeOpacity: 3.0,
                    strokeWeight: 2,
                  });
                  locationPath.setMap(map);
                } 
          //console.log(allLng);
      })

    })
  }


  

