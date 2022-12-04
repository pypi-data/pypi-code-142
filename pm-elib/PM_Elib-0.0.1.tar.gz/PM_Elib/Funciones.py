from pandas._libs.tslibs.timedeltas import Timedelta
import pandas as pd
import numpy as np

# -------------FUNCIONES-------------
def inicializar(df):
    global u0, _u, actions, transitions, places, places_bef_transition, seq_x_id, id_x_variant, stream_id, stream_seq, all_sequence, action_x_resource, dmenos, dmas, matrizD, seq_x_id, df_seq
    u0 = []
    places = []
    places_bef_transition = []
    id_x_variant = []
    actions = df["action"].unique().tolist()
    action_x_resource = pd.crosstab(df["resource"], df["action"])
    all_sequence = df.sort_values("datetime")["action"].tolist()
    stream_seq = df["action_sequence"].unique().tolist()
    stream_id = df["id"].unique().tolist()
    transitions = actions
    resources_groups = lista_grupos_x_recursos()
    creacion_lugares(resources_groups)
    u0[0] = len(stream_id)
    _u = u0
    dmenos = np.zeros((len(transitions), len(places)), dtype=np.int32)  # entradas
    dmas = np.zeros((len(transitions), len(places)), dtype=np.int32)  # salidas
    matrizD = np.zeros((len(transitions), len(places)), dtype=np.int32)
    fillings_all_arrays_Ds(resources_groups)
    variantes_x_id()
    seq_x_id = lista_variantes()
    df_seq = secuencia(df)


def lista_grupos_x_recursos():
    lista1 = []
    resultantList = []
    for accion in actions:
        aux = action_x_resource.index[action_x_resource[accion] > 0].tolist()
        lista1.append(aux)

    for element in lista1:
        if element not in resultantList:
            resultantList.append(element)

    return resultantList


def creacion_lugares(grupos_recursos):
    global u0, places
    # Lugares de "ESPERA"
    for accion in actions:
        places.append("esp_" + accion)
        u0.append(0)
        places_bef_transition.append("esp_" + accion)

    # Lugares de "RECURSOS"
    for place in grupos_recursos:
        places.append("rec" + str(grupos_recursos.index(place) + 1))
        u0.append(len(place))

    places.append("fin")
    u0.append(0)


def fillings_all_arrays_Ds(grupos_recursos):
    global dmas, dmenos, matrizD
    for i in range(len(actions)):
        dmenos[i][i] = 1

    for i in range(len(grupos_recursos)):
        for a in range(len(actions)):
            if action_x_resource[actions[a]][grupos_recursos[i][0]] > 0:
                dmenos[a][i + len(actions)] = 1
                dmas[a][i + len(actions)] = 1

    filling_Dmas()

    matrizD = dmas - dmenos


def filling_Dmas():
    global dmas
    for i in range(len(stream_seq)):
        aux = stream_seq[i].split(sep=" ➯ ")
        j = 0
        while j < aux.index(aux[-1]):
            pos_trans = actions.index(aux[j])
            pos_lugar = places_bef_transition.index("esp_" + aux[j + 1])
            if dmas[pos_trans][pos_lugar] == 0:
                dmas[pos_trans][pos_lugar] = 1
            j = j + 1

        pos_trans = actions.index(aux[-1])
        pos_lugar = -1
        if dmas[pos_trans][pos_lugar] == 0:
            dmas[pos_trans][pos_lugar] = 1


def isEnabled(u, ve):  # u -> marcacion actual
    aux = ve.dot(dmenos)  # vector unitario * matriz D-
    aux2 = np.maximum(u, aux)

    if np.array_equiv(u, aux2):
        return True
    return False


def escoger_camino(indice, vector, fin):
    for i in range(len(vector)):
        if vector[i] == 1 and (i != indice and i != fin):
            vector[i] = 0
    return vector


def variantes_x_id():
    global id_x_variant
    for i in range(len(stream_seq)):
        aux = events[events["action_sequence"] == stream_seq[i]]
        id_x_variant.append([aux["id"].unique().tolist(), i])


def tiempo_promedio_accion(tseg):
    global tiempos_prom, costos_prom
    tiempos_prom = []
    costos_prom = []
    for accion in actions:
        aux = np.mean(events[events["action"] == accion]["duration"])
        tiempos_prom.append(aux)
        costos_prom.append((aux.total_seconds()) * tseg)


def best_variant(tiempo):
    tiempo_prom_variante = []
    costos_prom_variante = []
    for seq in stream_seq:
        aux_tiempo = "0 days 00:00:00"
        aux_costo = 0
        for acc in seq.split(sep=" ➯ "):
            indice = actions.index(acc)
            aux_tiempo += tiempos_prom[indice]
            aux_costo += costos_prom[indice]
        tiempo_prom_variante.append(aux_tiempo)
        costos_prom_variante.append(aux_costo)
    aux_bv1 = [np.abs(t - tiempo) for t in tiempo_prom_variante]
    ind = aux_bv1.index(np.min(aux_bv1))
    return (ind, tiempo_prom_variante[ind], costos_prom_variante[ind])


def secuencia(df):
    df_aux1 = df.sort_values("datetime")[["id", "action", "datetime"]]
    df_aux1["InFin"] = "I"
    df_aux1.rename(columns={"datetime": "fecha"}, inplace=True)

    df_aux2 = df.sort_values("endaction")[["id", "action", "endaction"]]
    df_aux2["InFin"] = "F"
    df_aux2.rename(columns={"endaction": "fecha"}, inplace=True)

    df_secuencia = pd.concat([df_aux1, df_aux2], ignore_index="True").sort_values(
        "fecha"
    )
    return df_secuencia


def lista_variantes():
    list_var = []
    for id in stream_id:
        list_var.append(
            events[events["id"] == id]["action_sequence"]
            .unique()
            .tolist()[0]
            .split(sep=" ➯ ")
        )
    return list_var


def creando_df():
    columnas = ["transicion"] + ["InicioFin"] + places
    fila1 = ["u0"] + ["Marca Inicial"] + u0
    df = pd.DataFrame(columns=columnas)
    nueva_fila = pd.DataFrame(fila1, index=df.columns.tolist()).T
    df = pd.concat((df, nueva_fila), ignore_index=True)
    return df


def creando_df_cb():
    df_cb = pd.DataFrame()
    df_cb["Lugar de Espera"] = None
    df_cb["Ocur. de Cuello Botella "] = None
    df_cb["Mayor Cant. En Espera"] = None
    df_cb["Recurso"] = None
    df_cb["Rec. Iniciales por Actividad"] = None
    df_cb["Cant. Rec. en 0"] = None
    df_cb["Cant. Prom. Rec. Disp."] = None
    return df_cb


def at_a_time(df_secuencia):
    df_marcacion = creando_df()
    _u1 = u0
    for ind in df_secuencia.index:
        ve = np.zeros((len(actions)), dtype=np.int32)
        i = stream_id.index(df_secuencia["id"][ind])  # indice en la lista de usuarios
        j = actions.index(
            df_secuencia["action"][ind]
        )  # primera accion - indice en la lista de actions
        rec = np.where(dmenos[j] > 0)[0][1]  # lug_recurso
        if df_secuencia["InFin"][ind] == "I":
            _u1[rec] -= 1  # Recurso ocupado
            aux_pd = [df_secuencia["action"][ind]] + ["Inicio"] + list(_u1)
            nueva_fila = pd.DataFrame(aux_pd, index=df_marcacion.columns.tolist()).T
            df_marcacion = pd.concat((df_marcacion, nueva_fila), ignore_index=True)
        else:
            _u1[rec] += 1  # Recurso liberado
            if len(seq_x_id[i]) > 1:
                ve[j] = 1
                if isEnabled(_u1, ve):
                    ve_aux = ve.dot(matrizD)
                    k = actions.index(
                        seq_x_id[i][1]
                    )  # siguiente accion de la secuencia
                    _u1 = _u1 + (escoger_camino(k, ve_aux, places.index(places[-1])))
            else:
                ve[j] = 1
                if isEnabled(_u1, ve):
                    _u1 = _u1 + (ve.dot(matrizD))
            aux_pd = [df_secuencia["action"][ind]] + ["Fin"] + list(_u1)
            nueva_fila = pd.DataFrame(aux_pd, index=df_marcacion.columns.tolist()).T
            df_marcacion = pd.concat((df_marcacion, nueva_fila), ignore_index=True)
            seq_x_id[i].pop(0)
    return df_marcacion


def cuello_botella(df):  # v3
    tips0 = []
    tips1 = []
    df_cb = creando_df_cb()
    for i in range(len(actions)):
        acc = df.columns.tolist()[(np.where(dmenos[i] > 0)[0][0]) + 2]
        rec = df.columns.tolist()[(np.where(dmenos[i] > 0)[0][1]) + 2]
        rini = df[rec].max()
        df_1 = df[
            (df["transicion"] == acc.split("_")[1]) & (df["InicioFin"] == "Inicio")
        ]
        # print("Filas: "+str(df_1["transicion"].count()))

        ocb = df_1[df_1[acc] > df_1[rec] + 1]["transicion"].count()  # cant. ocur. cb
        mce = df_1[acc].max()  # mayor cant. esp.
        rec0 = df_1[df_1[rec] == 0]["transicion"].count()  # cant. veces rec = 0
        prd = round(df_1[rec].mean())  # cant. prom. rec. disp. todo el tiempo
        aux_porc0 = rec0 / len(stream_id) * 100
        aux_disp = round((prd / rini) * 100)

        if rec0 != 0 and aux_porc0 >= 65:
            aux = (
                "Se recomienda que para la actividad "
                + acc.split("_")[1].upper()
                + " se aumente la cantidad de recursos ya que, todos los recursos son ocupados por un "
                + str(aux_porc0)
                + "%"
                + " de los casos"
            )
            tips0.append(aux)
        if prd > 0 and aux_disp >= 45:
            aux = (
                "Se recomienda que para la actividad "
                + acc.split("_")[1].upper()
                + " todos los recursos sean utilizados, ya que, se detecta que hay aproximadamente "
                + str(aux_disp)
                + "%"+" de recursos inactivos, es decir, en todo momento hay por lo menos "+str(prd)+" recursos disponibles"
            )
            tips1.append(aux)

        aux_pd = [acc, ocb, mce, rec, rini, rec0, prd]
        nueva_fila = pd.DataFrame(aux_pd, index=df_cb.columns.tolist()).T
        df_cb = pd.concat((df_cb, nueva_fila), ignore_index=True)
    return (df_cb, tips0, tips1)


def process_file(fn, days, hours, costo):
    global events
    tiempo = str(days) + " days " + str(hours)
    events = pd.read_csv(fn)
    events.columns = ["id", "action", "resource", "datetime", "endaction"]
    events["datetime"] = pd.to_datetime(events["datetime"])
    events["endaction"] = pd.to_datetime(events["endaction"])
    events["duration"] = events["endaction"] - events["datetime"]

    events["action"] = events["action"].apply(lambda x: x.strip())

    events["resource"] = events["resource"].apply(lambda x: x.strip())

    delimiter = " ➯ "

    makeEventString = lambda x: delimiter.join(x)
    makeEventString.__name__ = "makeEventString"

    caselogs = events.pivot_table(index="id", aggfunc={"action": [makeEventString]})
    caselogs = caselogs.reset_index()
    caselogs.columns = ["id", "action_sequence"]

    events = pd.merge(events, caselogs, on="id")

    inicializar(events)

    tiempo_promedio_accion(costo / Timedelta(tiempo).total_seconds())

    (ind_mejor_var, tiempo_mejor_var, costo_mejor_var) = best_variant(Timedelta(tiempo))
    mejor_var = stream_seq[ind_mejor_var].replace(" ➯ ", ", ")

    df_marcacion = at_a_time(df_seq)

    (df_bottleneck, tips0, tips1) = cuello_botella(df_marcacion)

    return (
        {
            "Generalidades": {
                "Path": fn,
                "Rows": events.shape[0],
                "Columns": events.shape[1],
                "Cant. Casos": str(len(stream_id)),
            },
            "Marcacion inicial": u0,
            "Places": places,
            "Transitions": transitions,
            "Filtrado secuencias": stream_seq,
            "Id_x_Variant": id_x_variant,
            "D-":dmenos,
            "D+":dmas,
            "D":matrizD,
            "Action_x_Resource": action_x_resource.to_dict(), 
            "Marcacion": df_marcacion.to_dict(),
            "Cuello de botella": df_bottleneck.to_dict(),
            "Consejos_0": tips0,
            "Consejos_1": tips1,
            "Mejor Variante": mejor_var,
            "Tiempo Mejor Variante Sin Tiempos Muertos": str(tiempo_mejor_var),
            "Costo Mejor Variante": costo_mejor_var,
        },
    )
