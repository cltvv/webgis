import React, {useEffect} from 'react';
import 'ol/ol.css';
import Map from 'ol/Map';
import View from 'ol/View';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import Feature from 'ol/Feature';
import Point from 'ol/geom/Point';
import {fromLonLat} from 'ol/proj';
import {Vector as VectorLayer} from 'ol/layer';
import {Vector as VectorSource} from 'ol/source';
import {Style, Text, Fill, Stroke, Icon} from 'ol/style';

import './App.css';
import axios from 'axios';

function App() {
    useEffect(() => {
        const map = new Map({
            target: 'map',
            layers: [
                new TileLayer({
                    source: new OSM(),
                }),
            ],
            view: new View({
                center: [0, 0],
                zoom: 2,
            }),
        });

        axios
            .get('http://localhost:8000/api/v1/coordinates/map-objects/')
            .then(function (response) {
                const data = response.data;

                const markers = new VectorSource();
                const markerLayer = new VectorLayer({
                    source: markers,
                });

                const iconStyle = new Style({
                    image: new Icon({
                        anchor: [0.5, 46],
                        anchorXUnits: 'fraction',
                        anchorYUnits: 'pixels',
                        src: 'https://www.geocodezip.net/mapIcons/google-maps-gps-icon-14.jpg',
                        scale: 0.1
                    })

                });

                data.forEach((mapObject) => {
                    const coordinates = fromLonLat([mapObject.longitude, mapObject.latitude]);
                    const marker = new Feature({
                        geometry: new Point(coordinates),
                        name: mapObject.name,
                    });
                    const labelStyle = new Style({
                        text: new Text({
                            font: '12px Calibri,sans-serif',
                            overflow: true,
                            fill: new Fill({
                                color: '#000'
                            }),
                            stroke: new Stroke({
                                color: '#fff',
                                width: 3
                            }),
                            offsetY: -12
                        })
                    });
                    const style = [iconStyle, labelStyle];
                    marker.setStyle(style);

                    const label = new Feature({
                        geometry: new Point(coordinates),
                        name: mapObject.name,
                    });
                    label.setStyle(labelStyle);
                    labelStyle.getText().setText(marker.get('name'));
                    markers.addFeature(marker);
                    markers.addFeature(label);
                });

                map.addLayer(markerLayer);
            })
            .catch(function (error) {
                console.log(error);
            });

        return () => {
            map.setTarget(null);
        };
    }, []);

    return <div id="map" className="map__container"></div>;
}

export default App;