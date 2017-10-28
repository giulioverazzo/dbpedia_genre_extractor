# dbpedia_genre_extractor

dataset/MappingLastfm2DBPedia-1.2.tsv file is taken from https://github.com/sisinflab/LODrecsys-datasets/tree/master/LastFM and contains a list of music artists and their relative DBpedia pointer.

1_dbpedia_genres_file_generator.py reads from the dataset, and for each artist queries DBpedia in order to extract his list of music genres as a URI, i.e.
http://dbpedia.org/resource/Electronic_rock
The complete list is contained in output/1_genres.txt

2_genre_extractor.py takes output/1_genres.txt as input and for each line will make a query to DBpedia to extract the "foaf:name" property. Since 1_genres.txt cointains a lot of duplicates, this script uses a python set class to remove duplicates. Output of the script is the file output/2_genre_names.txt

3_createcsv.py formats output/2_genre_names.txt in a form required by Google's Dialogflow in order to import these genres as Entities. Output file is output/3_genres_for_dialogflow.txt
