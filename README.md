# F1TrackJsonify
Python script to transform the raw data taken from the openf1 API into a json file with track coordinates.

The idea was to take the data from a session of a single driver from the location session in order to rebuild the path of the track.

Example of API call: "https://api.openf1.org/v1/location?session_key=7783&driver_number=1&date%3E2023-04-01T06:00:00+00:00&date%3C2023-04-01T06:10:00+00:00"

This takes in consideration 10 minutes of the driver session, beeing a Quali it's enough to also have the positions of the Pit.


Example of Json output of the API:
```
[
  {
    "date": "2023-04-01T06:00:00.067000+00:00",
    "session_key": 7783,
    "meeting_key": 1143,
    "driver_number": 1,
    "z": 91,
    "x": 4014,
    "y": 847
  },
  {
    "date": "2023-04-01T06:00:00.308000+00:00",
    "session_key": 7783,
    "meeting_key": 1143,
    "driver_number": 1,
    "z": 93,
    "x": 4161,
    "y": 795
  }
]
```
The job of the script is to extrapolate only the x and y coordinates and write them in a new file.
