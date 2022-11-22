# analysis setup

Analysis of the API required interception of the network traffic between
the mobile application *MyHomeUp* and the *MyHOMEServer1* component on the local
network.

## devices

* *MyHOMEServer1* with firmware version 2.31.18
* *MyHOME_Up app* in version 2.7.13 running on iOS
* A computer used for interception of network traffic

## poking around

Early analysis with UPnP clients on the local network showed that the system
shows up as a UPnP device *MyHOMEServer1* which exposes some operations.
However, not a single of these operations pointed towards the API.

According to the manual there is a web-interace on the system, listening for
HTTPS requests on port 3443. The interface is however very limited,
providing solely the ability to export and import entire configuration data
after logging in with the *installer code*.

Overall this didn't yield a lot of useful information, except for the webserver
running on port 3443 using a self-signed certificate with a two year expiry.
In addition the server itself reports its implementation as
*Jetty(9.3.5.v20151012)*, which suggests the webserver provides more than
this limited web-interface.

## mitmproxy

Given that a webserver is running on the hardware it quickly became clear that this
is a likely target for a possible API.

As such [mitmproxy](https://mitmproxy.org) formed the basis for further analysis.
After installation and starting mitmproxy the iOS device was configured with its
new proxy settings.

In addition the *Don't verify server certificates* setting was activated in
mitmproxy and the mitmproxy root certificate was installed on the iOS device.

## first results

With the described setup in place first results of the analysis, containing the
authentication flow, were available. It showed that the app, pre-configured with a
connection before activating the proxy, does apparently not do any certificate
pinning, which revealed the HTTPS-protected communication.

Fortunately the API is a RESTful API using JSON for serialization, which made
further analysis and interpretation of calls, their parameters and returned
information simple.

For more information on the API calls head over to the [API documentation](./api.md).
