from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd

#importa il dataset di lastFM/DBpedia
dataFile = 'dataset/MappingLastfm2DBpedia-1.2.tsv'
data = pd.read_csv(dataFile, sep = "\t", header = None, names = ['id', 'name', 'DBpedia'])

#crea una lista con la colonna DBpedia
artists = []
for items in data['DBpedia']:
    artists.append(items)

#apri un file in scrittura per scriverci dentro il risultato
f = open("output/1_genres.txt","w",encoding="utf8")

#per ogni artista nella lista
for artist in artists:
  
    #crea la query parametrizzata
    query = 'SELECT ?genre WHERE { <%s>   <http://dbpedia.org/ontology/genre> ?genre .}' % (artist)

    #esegui la query e converti il risultato
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    #per ogni riga del risulato (per ogni genere musicale del tale artista)
    for result in results["results"]["bindings"]:
        #scrivi nel file i generi del singolo artista
        f.write(result["genre"]["value"]) 
        f.write('\n') #aggiungi un a capo
    
f.close()