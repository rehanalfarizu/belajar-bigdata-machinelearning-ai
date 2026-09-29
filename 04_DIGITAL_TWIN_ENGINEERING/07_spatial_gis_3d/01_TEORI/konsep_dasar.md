# Spatial, GIS, BIM/CAD, dan 3D

Spatial Digital Twin bukan sekadar icon di peta. Geometry harus memiliki coordinate reference system (CRS), datum, axis order, unit, precision, dan valid time. Latitude/longitude adalah angular coordinates; perhitungan jarak/area sering memerlukan projection yang sesuai lokasi dan skala.

Vector merepresentasikan points/lines/polygons; raster merepresentasikan grid; DEM menyimpan elevasi; point cloud/mesh merepresentasikan permukaan 3D. Spatial index mempercepat query, sedangkan topology menyatakan adjacency/connectivity/containment. GPS memiliki uncertainty dan dapat memerlukan map matching ke network.

BIM/CAD object ID belum tentu sama dengan operational asset ID. Buat mapping versioned dengan provenance dan lifecycle. Untuk 3D, scene graph, level of detail, streaming, occlusion, dan coordinate frame harus eksplisit. Visual adalah projection; source of truth state/command tetap service versioned dengan access control dan audit.

Use case: room/HVAC/occupancy pada building; road graph/fleet trajectory; terrain/haul road/equipment pada mining; network topology dan geographic hazard pada infrastructure/energy. Coordinate error dapat mengarahkan keputusan fisik ke lokasi salah meskipun tampilan tampak masuk akal.

Rujukan awal: [OGC SensorThings](https://www.ogc.org/standards/sensorthings/) untuk sensing/tasking geospatial. Periksa standard/domain guidance yang relevan sebelum implementasi produksi.
