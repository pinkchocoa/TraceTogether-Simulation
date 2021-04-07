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
  const covid_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Coronavirus_icon.svg/1024px-Coronavirus_icon.svg.png"
  const size1 = 20;
  const size2 = 15;

  var locationmarkers = [
    [          
      "100 AM" ,
      1.274913 ,
      103.843614,0
    ],
    [
      "313@Somerset" ,
      1.301013 ,
      103.83854,0
    ],
    [
      "321 Clementi" ,
      1.316578 ,
      103.766386,0 
    ],
    [
      "888 Plaza" ,
      1.43781 ,
      103.795316 ,0
    ],
    [
      "Admiralty Place" ,
      1.439698 ,
      103.801841,0 
    ],
    [
      "Alexandra Central" ,
      1.287526 ,
      103.805291,0 
    ],
    [
      "Alexandra Retail Centre" ,
      1.273893 ,
      103.801456,0 
    ],
    [
      "AMK Hub" ,
      1.369435 ,
      103.848334,0 
    ],
    [
      "Anchorpoint" ,
      1.288675 ,
      103.805095,0 
    ],
    [
      "Aperia" ,
      1.310341 ,
      103.864027,0 
    ],
    [
      "Balestier Hill Shopping Centre" ,
      1.325442 ,
      103.842521,0 
    ],
    [
      "Beauty World Centre" ,
      1.3423624 ,
      103.7764855,0 
    ],
    [
      "Beauty World Plaza" ,
      1.34183 ,
      103.776278,0 
    ],
    [
      "Bedok Mall" ,
      1.32488 ,
      103.9292396,0 
    ],
    [
      "Bedok Point" ,
      1.3247574 ,
      103.9323895,0 
    ],
    [
      "Big Box ",
      1.3322794 ,
      103.7457493,0 
    ],
    [
      "Boon Lay Shopping Centre" ,
      1.3463367 ,
      103.7127614,0 
    ],
    [
      "Buangkok Square" ,
      1.3838388 ,
      103.8819622,0 
    ],
    [
      "Bugis Cube" ,
      1.2982756 ,
      103.8555546,0 
    ],
    [
      "Bugis Junction" ,
      1.2989008 ,
      103.855176,0
    ],
    [
      "Bugis+",
      1.2999533 ,
      103.8552781,0 
    ],
    [
      "Bukit Panjang Plaza" ,
      1.378655 ,
      103.7620908,0 
    ],
    [
      "Bukit Timah Plaza" ,
      1.3384959 ,
      103.7785106,0 
    ],
    [
      "Canberra Plaza" ,
      1.4432209 ,
      103.8305821,0 
    ],
    [
      "Capitol Piazza" ,
      1.2930198 ,
      103.8509811,0
    ],
    [
      "Cathay Cineleisure Orchard" ,
      1.3014468 ,
      103.8364807,0 
    ],
    [
      "Causeway Point" ,
      1.4361009 ,
      103.7860949,0 
    ],
    [
      "Century Square" ,
      1.3523775 ,
      103.9438195,0 
    ],
    [
      "Changi Airport" ,
      1.3575573 ,
      103.9884703,0 
    ],
    [
      "Changi City Point" ,
      1.334113 ,
      103.9627137,0 
    ],
    [
      "City Gate Mall" ,
      1.3023204 ,
      103.8622868,0 
    ],
    [
      "City Plaza" ,
      1.3147175 ,
      103.8934143,0 
    ],
    [
      "City Square Mall" ,
      1.3112429 ,
      103.8565772,0 
    ],
    [
      "CityLink Mall" ,
      1.2921921 ,
      103.8545358,0 
    ],
    [
      "Clarke Quay Central" ,
      1.2889569 ,
      103.8464961,0 
    ],
    [
      "Compass One" ,
      1.3920337 ,
      103.8949527,0 
    ],
    [
      "Djitsun Mall" ,
      1.3728879 ,
      103.8476187,0 
    ],
    [
      "Djitsun Mall Bedok" ,
      1.3260744 ,
      103.9295754,0 
    ],
    [
      "Downtown East" ,
      1.3773722 ,
      103.954648 ,0
    ],
    [
      "East Village" ,
      1.3316644 ,
      103.9462908,0 
    ],
    [
      "Eastpoint Mall" ,
      1.3424679 ,
      103.9528535,0 
    ],
    [
      "Elias Mall" ,
      1.3785553 ,
      103.9420134,0 
    ],
    [
      "Fairprice Hub" ,
      1.3255324 ,
      103.6784394,0 
    ],
    [
      "Fajar Shopping Centre" ,
      1.3834498 ,
      103.7710942,0 
    ],
    [
      "Far East Plaza" ,
      1.3071429 ,
      103.8336405,0 
    ],
    [
      "Funan" ,
      1.291313 ,
      103.8499471,0 
    ],
    [
      "Gek Po Shopping Centre" ,
      1.349176 ,
      103.6975195,0 
    ],
    [
      "Great World City" ,
      1.2934518 ,
      103.8319929,0 
    ],
    [
      "Greenridge Shopping Centre" ,
      1.3853791 ,
      103.7661902,0 
    ],
    [
      "Greenwich V" ,
      1.3875009 ,
      103.8693942,0 
    ],
    [
      "GR.ID" ,
      1.3000836 ,
      103.8492948,0 
    ],
    [
      "HarbourFront Centre" ,
      1.2642217 ,
      103.8202454,0 
    ],
    [
      "HDB Hub" ,
      1.3319765 ,
      103.8485384,0 
    ],
    [
      "Heartland Mall" ,
      1.3596301 ,
      103.8852259,0 
    ],
    [
      "Hillion Mall" ,
      1.3785082 ,
      103.7633212,0 
    ],
    [
      "HillV2" ,
      1.3629674 ,
      103.7644875,0 
    ],
    [
      "Hougang 1" ,
      1.375719 ,
      103.8794915,0 
    ],
    [
      "Hougang Green Shopping Mall" ,
      1.3791215 ,
      103.8878419,0 
    ],
    [
      "Hougang Mall" ,
      1.3725735 ,
      103.8937879,0 
    ],
    [
      "i12 Katong" ,
      1.3052327 ,
      103.9050524,0 
    ],
    [
      "IMM" ,
      1.334611 ,
      103.7467494,0 
    ],
    [
      "ION Orchard" ,
      1.3039479 ,
      103.8319051,0 
    ],
    [
      "JCube" ,
      1.3332998 ,
      103.7401593,0 
    ],
    [
      "Jem" ,
      1.3332962 ,
      103.7433912,0 
    ],
    [
      "Jewel Changi Airport" ,
      1.3602242 ,
      103.9896749,0 
    ],
    [
      "Jubilee Square" ,
      1.3718136 ,
      103.8477532,0 
    ],
    [
      "Junction 10" ,
      1.3803675 ,
      103.7601674,0 
    ],
    [
      "Junction 8" ,
      1.3505893 ,
      103.8487447,0 
    ],
    [
      "Junction 9" ,
      1.2904753 ,
      103.8520359,0 
    ],
    [
      "Jurong Point" ,
      1.3394964 ,
      103.705254,0 
    ],
    [
      "Kallang Wave Mall" ,
      1.3035107 ,
      103.8727917,0 
    ],
    [
      "Katong Shopping Centre" ,
      1.3038779 ,
      103.9011731,0 
    ],
    [
      "Katong Square" ,
      1.3047036 ,
      103.9048008,0 
    ],
    [
      "Katong V" ,
      1.3031334 ,
      103.9032312,0 
    ],
    [
      "Keat Hong Shopping Centre" ,
      1.3773319 ,
      103.7444165,0 
    ],
    [
      "KINEX" ,
      1.3147639 ,
      103.894707,0 
    ],
    [
      "Knightsbridge" ,
      1.3032346 ,
      103.8363241,0 
    ],
    [
      "Leisure Park Kallang" ,
      1.3022347 ,
      103.8765544,0 
    ],
    [
      "Liat Towers" ,
      1.3050783 ,
      103.8307259,0 
    ],
    [
      "Limbang Shopping Centre" ,
      1.3919423 ,
      103.7433051,0 
    ],
    [
      "Lot One" ,
      1.3850567 ,
      103.7450277,0 
    ],
    [
      "Loyang Point" ,
      1.3669647 ,
      103.9646487,0 
    ],
    [
      "Lucky Plaza" ,
      1.3046029 ,
      103.8339122,0 
    ],
    [
      "Marina Bay Financial Centre Tower 3" ,
      1.2789573 ,
      103.8544488,0 
    ],
    [
      "Marina Bay Link Mall" ,
      1.2808361 ,
      103.8539888,0 
    ],
    [
      "Marina Bay Sands" ,
      1.2836965 ,
      103.8607226,0 
    ],
    [
      "Marina One" ,
      1.2772586 ,
      103.8529596,0 
    ],
    [
      "Marina Square" ,
      1.2912739 ,
      103.8571836,0 
    ],
    [
      "Marsiling Mall" ,
      1.4332503 ,
      103.780787,0 
    ],
    [
      "Midpoint Orchard" ,
      1.3017143 ,
      103.8386311,0 
    ],
    [
      "Millenia Walk" ,
      1.292471 ,
      103.8596399,0 
    ],
    [
      "Mustafa Shopping Centre" ,
      1.3101174 ,
      103.8553229,0 
    ],
    [
      "myVillage At Serangoon Garden" ,
      1.3651222 ,
      103.8650484,0 
    ],
    [
      "NEX" ,
      1.3504507 ,
      103.8722447,0 
    ],
    [
      "Ngee Ann City" ,
      1.302617 ,
      103.8345284,0 
    ],
    [
      "Northpoint City" ,
      1.4282062 ,
      103.836264,0 
    ],
    [
      "Oasis Terraces" ,
      1.4028263 ,
      103.913229,0 
    ],
    [
      "OD Mall" ,
      1.3351056 ,
      103.7944923,0 
    ],
    [
      "Orchard Central" ,
      1.3008042 ,
      103.839819,0 
    ],
    [
      "Orchard Gateway" ,
      1.3014214 ,
      103.8389049,0 
    ],
    [
      "Orchard Plaza" ,
      1.3013398 ,
      103.8411567,0 
    ],
    [
      "Orchard Shopping Centre" ,
      1.3014771 ,
      103.8378934,0 
    ],
    [
      "Our Tampines Hub" ,
      1.3530262 ,
      103.9406755,0 
    ],
    [
      "Palais Renaissance" ,
      1.28967 ,
      103.85007,0 
    ],
    [
      "Paragon" ,
      1.3037371 ,
      103.8355203,0 
    ],
    [
      "Parkway Parade" ,
      1.3013733 ,
      103.9051778,0 
    ],
    [
      "Paya Lebar Quarter (PLQ)" ,
      1.3175858 ,
      103.892854,0 
    ],
    [
      "People's Park Centre",
      1.285942 ,
      103.8442264,0 
    ],
    [
      "People's Park Complex",
      1.2841387 ,
      103.842557,0 
    ],
    [
      "Pioneer Mall" ,
      1.3416979 ,
      103.6971606,0 
    ],
    [
      "Plaza Singapura" ,
      1.3004414 ,
      103.8449028,0 
    ],
    [
      "Punggol Plaza" ,
      1.399168 ,
      103.9024984,0 
    ],
    [
      "Queensway Shopping Centre" ,
      1.2875059,
      103.8035435,0
    ],
    [
      "Raffles City" ,
      1.2938762 ,
      103.8532616,0 
    ],
    [
      "Rail Mall" ,
      1.3601778 ,
      103.7675449,0 
    ],
    [
      "Rivervale Mall" ,
      1.3922451 ,
      103.9043778,0 
    ],
    [
      "Rivervale Plaza" ,
      1.3853753 ,
      103.9018221,0 
    ],
    [
      "Rochester Mall" ,
      1.3056577 ,
      103.7880838,0 
    ],
    [
      "Roxy Square" ,
      1.3033419 ,
      103.9046459,0 
    ],
    [
      "Scotts Square ",
      1.3058344 ,
      103.8329333,0 
    ],
    [
      "Sembawang Shopping Centre" ,
      1.4417425 ,
      103.8248753,0 
    ],
    [
      "Serangoon Plaza" ,
      1.3109014 ,
      103.8548135,0 
    ],
    [
      "Shaw House and Centre" ,
      1.3058298 ,
      103.831526,0 
    ],
    [
      "Sim Lim Square" ,
      1.3030332 ,
      103.8530255,0
    ],
    [
      "Singapore Post Centre (Singpost Centre)" ,
      1.3189532 ,
      103.8947901,0 
    ],
    [
      "Singapore Shopping Centre" ,
      1.2981147 ,
      103.8441112,0 
    ],
    [
      'Square 2' ,
      1.3206362 ,
      103.8441867,0 
    ],
    [
      "Sun Plaza" ,
      1.4480986 ,
      103.8190191,0 
    ],
    [
      "Sunshine Place" ,
      1.3777695 ,
      103.7386492,0 
    ],
    [
      "Sunshine Plaza" ,
      1.3003526 ,
      103.8509473,0 
    ],
    [
      "Suntec City" ,
      1.2951505 ,
      103.8598741,0 
    ],
    [
      "Taman Jurong Shopping Centre" ,
      1.3347863 ,
      103.7201085,0 
    ],
    [
      "Tampines 1" ,
      1.35422 ,
      103.9451247,0 
    ],
    [
      "Tampines Mall" ,
      1.3525434 ,
      103.9447383,0 
    ],
    [
      "Tanglin Mall" ,
      1.3048201 ,
      103.8238677,0 
    ],
    [
      "Tang Plaza" ,
      1.305109 ,
      103.8328767,0 
    ],
    [
      "Tanjong Pagar Centre" ,
      1.2766057 ,
      103.8457793,0 
    ],
    [
      "Teck Whye Shopping Centre" ,
      1.3807832 ,
      103.7524705,0 
    ],
    [
      "Tekka Centre" ,
      1.3061832 ,
      103.8505875,0 
    ],
    [
      "The Centrepoint" ,
      1.3018345 ,
      103.8397127,0 
    ],
    [
      "The ClementiMall" ,
      1.3150286 ,
      103.7644982,0 
    ],
    [
      "The Flow" ,
      1.3045554 ,
      103.9042659,0 
    ],
    [
      "The Midtown" ,
      1.370386 ,
      103.8953238,0 
    ],
    [
      "The Seletar Mall" ,
      1.3917727 ,
      103.8760148,0 
    ],
    [
      "The Shoppes at Marina Bay Sands" ,
      1.2840175 ,
      103.8587997,0 
    ],
    [
      "The Star Vista" ,
      1.3068312 ,
      103.7884268,0 
    ],
    [
      "Thomson Plaza ",
      1.3546534 ,
      103.831073,0 
    ],
    [
      "Tiong Bahru Plaza" ,
      1.2863599 ,
      103.827333,0 
    ],
    [
      "United Square" ,
      1.317258 ,
      103.8436009,0 
    ],
    [
      "Upper Serangoon Shopping Centre" ,
      1.3536587 ,
      103.8788228,0 
    ],
    [
      "Velocity@Novena Square",
      1.3197981 ,
      103.8440434,0 
    ],
    [
      "Vista Point" ,
      1.4307324 ,
      103.7940437,0 
    ],
    [
      "VivoCity" ,
      1.2643707 ,
      103.8229537,0 
    ],
    [
      "Waterway Point" ,
      1.4066031 ,
      103.9020707,0 
    ],
    [
      "West Coast Plaza",
      1.303478 ,
      103.7658546,0 
    ],
    [
      "West Mall" ,
      1.3500765 ,
      103.7492566,0 
    ],
    [
      "Westgate" ,
      1.334194 ,
      103.7428671,0 
    ],
    [
      "Wheelock Place" ,
      1.3046691 ,
      103.8306003,0 
    ],
    [
      "White Sands" ,
      1.3723844 ,
      103.9497206,0 
    ],
    [
      "Wisma Atria" ,
      1.3036967 ,
      103.8332876,0 
    ],
    [
      "Wisteria Mall" ,
      1.4182429 ,
      103.8412529,0 
    ],
    [
      "Woodlands Civic Centre" ,
      1.4350299 ,
      103.7869088,0 
    ],
    [
      "Woodlands Mart" ,
      1.4456569 ,
      103.798172,0 
    ],
    [
      "Woodlands North Plaza" ,
      1.44288 ,
      103.7908639,0 
    ],
    [
      "Yew Tee Point" ,
      1.3969577 ,
      103.7466122,0 
    ],
    [
      "Yew Tee Shopping Centre" ,
      1.3974608,
      103.7474009,
      0
    ],
    [
      "Yew Tee Square" ,
      1.3982858 ,
      103.7470082,0
    ],
    [
      "Zhongshan Mall" ,
      1.3271544 ,
      103.8464917,0 
    ] 
  ];
  // console.log(locationmarkers[0][3]);

  let allGroup = [];
  let allLocation = [];
  let covidIndex = [];
  let covidLocation = [];
  
  //Fetch data from JSON file
  fetch("json/peopleDetails.json")
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
            for(let k=0; k<locationmarkers.length; k++){
              if(covidLocation[i][j] == locationmarkers[k][0]){
                locationmarkers[k][3]+=1;
              }
            }
          }
        }
        //console.log(locationmarkers[21][3]);
        for (let i = 0; i<locationmarkers.length; i++){
          // Add the circle for this city to the map.
          if (locationmarkers[i][3] != 0){
            const cityCircle = new google.maps.Circle({
              strokeColor: "#FF0000",
              strokeOpacity: 0.8,
              strokeWeight: 1,
              fillColor: "#FF0000",
              fillOpacity: 0.35,
              map,
              center: {lat: locationmarkers[i][1], lng: locationmarkers[i][2]},
              radius: locationmarkers[i][3] * 600,
          });
          }
        }

        for(let i=0; i<covidLocation.length; i++){
          let covidLocationIndex = [];
          for(let j=0; j<covidLocation[i].length; j++){
            for(let k=0; k<locationmarkers.length; k++){
              if(covidLocation[i][j] == locationmarkers[k][0]){
                covidLocationIndex.push(k);
              }
            }
          }
          var locationCoordinates = [];
          var index=0;
          for (let f=0; f<covidLocationIndex.length; f++){
            locationCoordinates.push({ lat: locationmarkers[covidLocationIndex[index]][1], lng: locationmarkers[covidLocationIndex[index]][2]});
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




  

