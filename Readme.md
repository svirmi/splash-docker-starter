Repository contains two docker services to help developing with [splash](https://splash.readthedocs.io/en/stable/):
* "parser" - a generic python container to use with different python libraries and packages, like scrapy, requests etc.
* "splash" - splash container running at "0.0.0.0:8050" to process requests from inside "parser" container

**example.py** contains code to get deals page data from gearbest.com
