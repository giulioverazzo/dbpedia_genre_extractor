from SPARQLWrapper import SPARQLWrapper, JSON

#apri un file in lettura 
f =  open("genres.txt","r",encoding="utf8")
f2 = open("genre_names.txt","w",encoding="utf8")

#in Python un set è una collezione di elementi non duplicati.
genres_set = set()

#per ogni genere nel file
for line in f:
  
    #crea la query parametrizzata
    query = 'SELECT ?name WHERE { <%s>   <http://xmlns.com/foaf/0.1/name>	?name . FILTER(lang(?name) = "en")}' % (line.strip("\n"))

    #esegui la query e converti il risultato
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    #per ogni riga del risulato (per ogni genere musicale del tale artista)
    for result in results["results"]["bindings"]:
        #scrivi nel file i generi del singolo artista
        genres_set.add(result["name"]["value"])
      
    
for genre in genres_set:
    f2.write(genre+"\n")


f.close()
f2.close()