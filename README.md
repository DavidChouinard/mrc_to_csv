MARC21 to CSV converter
==========

Python script for converting MARC21 files to a saner format (CSV), originally designed for the freely available [Harvard Library Bibliographic Dataset](http://openmetadata.lib.harvard.edu/bibdata).

This script only conserves the following subset of MARC21 records (with only simple post-processing on them):

| Field       | Description         |
| ----------- | ------------------- |
| 020a        | ISBN                |
| 245a/245b   | Title               |
| 100/110/111 | Author              |
| 260b        | Publisher           |
| 260a        | Publisher Place     |
| 300a        | Extent (eg. pages)  |
| 300c        | Physical dimensions |
| 650c        | Subject             |
| 988a        | Inclusion date      |
| 906a        | Governing source    |
| 690 5       | Harvard Library     |


The last three fields are Harvard-specific (per Harvard's [documentation](http://openmetadata.lib.harvard.edu/sites/default/files/Harvard_Library_Bibliographic_Dataset_Documentation.pdf)) and can be easily excluded. Additional fields can also be easily added. See the Library of Congress' [official documentation](http://www.loc.gov/marc/bibliographic/) on MARC21 for standard field codes.

Usage
----------

This script expects source files will be in `data/mrc/` and will output the converted files to `data/csv/`. Simply run:

````
python convert.py
````

The script requries [pymarc](https://github.com/edsu/pymarc). Install it with:

````
pip install pymarc
````
