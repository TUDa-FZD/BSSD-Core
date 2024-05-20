# BSSD Core

# Install
## Using pip
```bash
pip install bssd
```
This will install the latest version of the bssd core library available in [PyPI](https://pypi.org/project/bssd/) to your environment.

## Manual installation from source

Install the package into your local python3 virtual environment:
```bash
git clone https://git.rwth-aachen.de/fzd/unicar-agil/sonstiges/bssd/core.git bssd
```
If you are using virtual environments, make sure to activate the correct environment to install the library into e.g:
```bash
source /<path-to-my-project>/.venv/bin/activate
```

Install the library:
```bash
pip install -e path/to/bssd/repository
```

# Usage
The package is build as an extension of [pyosmium](https://docs.osmcode.org/pyosmium/latest/intro.html).
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

# BSSDHandler callback functions
These callback functions need to be implemented in the inheriting class to be used.
The function will receive the specified objects after calling apply_file().
The relation callback can be used to read non BSSD elements.
- behavior_space(core.BehaviorSpace)
- behavior(core.Behavior)
- boundary_lat(core.BoundaryLat)
- boundary_long(core.BoundaryLong)
- reservation(core.Reservation)
- relation(osm.Relation)
