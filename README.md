# BSSD Core

> **IMPORTANT NOTE** This repository is part of the _Behavior-Semantic Scenery Description (BSSD)_ framework. Check out our BSSD documentation and overview repository in your git of choice:
[![GitLab](https://img.shields.io/badge/GitLab-330F63?style=flat&logo=gitlab&logoColor=white)](https://gitlab.com/tuda-fzd/scenery-representations-and-maps/behavior-semantic-scenery-description)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/TUDa-FZD/Behavior-Semantic-Scenery-Description)

This is a low-level Python library for creating and managing the BSSD elements within the BSSD extension for Lanelet2 maps. The BSSD Core is based on [PyOsmium](https://osmcode.org/pyosmium/), a module that provides access to some features of the C++ library [Osmium](https://osmcode.org/libosmium/) from Python code. It offers various functions for processing OpenStreetMap (OSM) data - that means also Lanelet2 data - quickly and flexibly. PyOsmium or Osmium specializes in processing the ways, nodes and relations elements available in OSM. The BSSD Core builds on this library and provides functions that are adapted for BSSD elements. Classes are provided for the BSSD elements of the BSSD extension for Lanelet2. These classes already offer integrated attributes according to the [data structure](https://gitlab.com/tuda-fzd/scenery-representations-and-maps/behavior-semantic-scenery-description/-/blob/main/doc/extension_lanelet2.md#data-structure) of the BSSD extension for Lanelet2. The BSSD core therefore makes it possible to create instances of BSSD elements and set their attributes. In addition, members can be added using simple methods without knowing the correct syntax of the member elements in OSM. Since the instances of BSSD elements created in this way are translated internally into relations from OSM, it is possible to save them in an OSM file using the write functions of PyOsmium.

## Installation
### Using pip
```bash
pip install bssd-core
```
This will install the latest version of the BSSD Core library available in [PyPI](https://pypi.org/project/bssd-core/) to your environment.

### Manual Installation

Clone the source code to a directory of your choice (```path/to/bssd-core-src/```).

If you are using virtual environments, make sure to activate the correct environment to install the library into e.g:

```bash
source /<path-to-my-project>/.venv/bin/activate
```

Install the library:
```bash
pip install -e path/to/bssd-core-src/
```

## Usage
The package is build as an extension of [PyOsmium](https://osmcode.org/pyosmium/).
Following is a simple example on how to use the library. The referenced objects from the
handler are only temporary. If data is wished to be stored it must be copied out.

```python
import osmium
from bssd.core import BSSDHandler, Reservation
from bssd.core import mutable


class Handler(BSSDHandler):
    def __init__(self):
        super().__init__()
        self.writer = osmium.SimpleWriter("out.osm")

    # callback function for reservations
    def reservation(self, r: Reservation):
        # r is readonly, to change r it must be converted
        r: mutable.Reservation = r.make_mutable()
        r.bicycle = True
        # write the changed reservation to the output file
        self.writer.add_relation(r.get_osmium())


if __name__ == "__main__":
    h = Handler()
    h.apply_file("in.osm")
```

> **NOTE** For a more application-oriented example, take also a look at the integration of the BSSD Core in the tool _Lanelet2 BSSD Converter_ using a git of your choice:
[![GitLab](https://img.shields.io/badge/GitLab-330F63?style=flat&logo=gitlab&logoColor=white)](https://gitlab.com/tuda-fzd/scenery-representations-and-maps/lanelet2-bssd-converter)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/TUDa-FZD/Lanelet2-BSSD-Converter)

## BSSDHandler Callback Functions
These callback functions need to be implemented in the inheriting class to be used.
The function will receive the specified objects after calling apply_file().
The relation callback can be used to read non BSSD elements.
- behavior_space(core.BehaviorSpace)
- behavior(core.Behavior)
- boundary_lat(core.BoundaryLat)
- boundary_long(core.BoundaryLong)
- reservation(core.Reservation)
- relation(osm.Relation)
