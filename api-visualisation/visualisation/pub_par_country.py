from pyspark.sql.types import StringType
from connexion import get_publications 
import json

from pyspark.sql.functions import countDistinct, count, col, year,explode,split,size ,concat_ws, collect_list, struct


def get_pub_par_country():

    publications = get_publications()

    # Utilisez explode pour déplier la colonne des pays
    df_expanded_pays = publications.select(explode("countries").alias("country"))

    # Grouper par "pays" et compter le nombre de publications par pays
    nombre_publications_par_pays = df_expanded_pays.groupBy("country").agg(count("*").alias("publication")).orderBy("publication", ascending=False)

    # convertir le resultat en json et renvoyer la
    json_result = nombre_publications_par_pays.toJSON().collect()

    # improuve the json result
    json_result = [json.loads(x) for x in json_result]

    return json_result
