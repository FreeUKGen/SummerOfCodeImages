### Sample FreeCEN Data

The following files contain data from FreeCEN which can be used for 
visualization, API development, or query improvement.  Further data
will be made available in a working Ruby on Rails applicaiton and a
MongoDB database for projects that are accepted, but this subset in 
JSON may prove useful for understanding the project.

FreeCEN contains census data for dwellings and individuals in the UK,
across multiple counties.  This subset contains data from three places
in the county of Cornwall, which is organized as follows:

* `all_cornwall_places.json` The full listing of places in Cornwall for which FreeCEN records exist.
* `cornwall_places.json` The three places for which sample data is provided.
* `cornwall_pieces.json` The census "pieces" for each place -- additional metadata for entries, specific to census years.
* `dwellings.json.gz` Transcribed data for a "dwelling" -- a house, school, prison, hospital, or ship on which people lived.  Some dwellings are uninhabited.
* `individuals.json.gz`  Transcribed data for individuals within a dwelling.
* `search_records.json.gz`  A composite record used by our search engine, created out of the above elements.

