# myhome

*myhome* is a Python package providing an API client for the Legrand/Bticino MyHomeSERVER1 API.

This API is usually used by the *MyHome_UP* mobile application and has been partially
reverse-engineered from intercepting the traffic between the application and the server
running on the local network. You can find information on the [analysis setup](doc/analysis_setup.md)
and the [API](doc/api.md) itself in the *doc* directory of this repository.

Please be aware that this is a very early version of the library and things may change at any
point in time.
The long-term goal is to implement a library with a stable interface which can then be
used in home automation systems and frameworks, like *Home Assistant*.

## OpenAPI spec

This repository contains an [OpenAPI spec](contrib/openapi.yml) which partially describes
the API exposed by MyHomeSERVER1.

## Status

- [x] Basic light control
- [x] Basic dimmer control
- [x] Basic shutter control
- [x] Basic thermostat control
- [x] Basic room support
- [x] Basic zone support
- [x] CI pipeline
- [ ] Unit tests
- [ ] Library documentation
