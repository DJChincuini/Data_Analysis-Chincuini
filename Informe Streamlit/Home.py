import streamlit as st 
import pandas as pd
import numpy as np

# Cargo los Datasets
hechos = pd.read_csv('./Datasets/Hechos.csv')
victimas = pd.read_csv('./Datasets/Victimas.csv')
# Reemplazo valores SD (Sin Dato) por valores None
victimas = victimas.replace("SD",np.nan)
hechos = hechos.replace("SD",np.nan)

# Configura para que el layout sea "wide"
st.set_page_config(layout="wide")



### TÍTULO
st.write("### Informe sobre siniestros viales en la ciudad de Buenos Aires") 
st.write("*Creado por Dante Chincuini* \n####")



### INTRODUCCIÓN
st.write("#### **Introducción**")

st.write(
    f'''
    En este proyecto abordaré realicé un análisis sobre los siniestros viales en la ciudad autónoma de Buenos Aires. 
Primeramente, realicé un informe EDA para ver las relaciones de los datos, los nulos que contiene y buscar outliers que pueden condicionar al posterior análisis. Todo este proceso lo pueden encontrar en mi github en el siguiente link: https://github.com/DJChincuini/Data_Analysis-Chincuini/blob/main/EDA.ipynb.
\n ###''')



### KPIs
st.write("#### **KPIs**")

# Creo dos columnas para presentar los KPI
kpi1,kpi2 = st.columns(2)

# Primera Columna
with kpi1:
    st.write(f"*Reducir en un 10% la tasa de homicidios en siniestros viales de los últimos seis meses.*")    
    # Fórmula del primer KPI    
    st.latex(
        r'''
        KPI = \frac{\left(\frac{H actual}{S actual}\right)}{\left(\frac{H anterior}{S anterior}\right) * 0.9}
        '''
    )
    
    # Descipción de la fórmula
    st.write(f'''
    Dónde:\n
    + *H actual* es la cantidad de homicidios en siniestros en el último semestre\n
    + *S actual* es la cantidad total de siniestros en el último semestre\n
    + *H anterior* es la cantidad de homicidios en siniestros en el semestre anterior\n
    + *S anterior* es la cantidad total de siniestros en el semestre anterior
    ''')

# Segunda Columna
with kpi2:
    st.write(f"*Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año*")
    st.latex(
        r'''
        KPI = \frac{SM actual}{SM anterior * 0.7}
        '''
    )

    # Descripción de la fórmula
    st.write(f'''
    Dónde:\n
    + *SM actual* es la cantidad de siniestros dónde estén implicadas motocicletas en el último año\n
    + *SM anterior* es la cantidad de siniestros dónde estén implicadas motocicletas en el año anterior         
    ''')
st.write("##")



### DATASETS
st.write('#### **Datasets**')

st.write(
    '''
    Para poder llevar a cabo esta investigación, utilicé los datos pertenecientes del datasets de homicidios.xlsx provisto por el Observatorio de Movilidad y Seguridad Vial de la ciudad autónoma de Buenos Aires.
    '''
)

# Datasets Hechos
with st.expander("Hechos"):
    st.write("En este Dataset se registran los datos sobre el lugar geográfico y la hora de cada siniestro")
    st.dataframe(hechos,column_config={
        "AAAA": st.column_config.NumberColumn("AÑO",format="%d"),
        "MM": st.column_config.NumberColumn("MES"),
        "DD": st.column_config.NumberColumn("DIA"),
        "FECHA":st.column_config.DateColumn(format="DD.MM.YYYY")
    })
    
# Datasets Victimas
with st.expander("Victimas"):
    st.write("En este Dataset se registran los datos centrados en los participantes de los siniestros, el estado de las victimas y los vehículos implicados")
    st.dataframe(victimas, column_config={
        "FECHA":st.column_config.DateColumn(format="DD.MM.YYYY"),
        "FECHA_FALLECIMIENTO":st.column_config.DatetimeColumn(format="DD.MM.YYYY h:mm a")
    })
st.write("##")



### ABOUT ME
st.write("#### Sobre el autor")
st.write(
    '''
    👋 Hola, me llamo Dante.
    
    📌 Soy un estudiante apasionado de programación y la estadística con un enfoque especial en el diseño, desarrollo e implementación de soluciones robustas por medio del Data Engineering 💻 así cómo también de la búsqueda de insights a través de los datos y del pensamiento analítico a la hora de la toma de decisiones 📊.

    📈 Me considero experto en la creación de arquitecturas escalables para procesamiento gracias a mí conocimientos de GCP y Python, cómo también del análisis de datos y el diseño de estrategias ayudándome con mi conocimiento de SQL y PowerBI. También poseo conocimientos en estadística y marketing gracias a mí tecnicatura en Diseño y Comunicación Multimedial.

    💪 Siempre en busca de desafíos que impulsen la innovación y la eficiencia en el mundo de la tecnología, mí objetivo es poder colaborar con profesionales tan apasionados cómo yo en pos de impulsar la toma de decisiones empresariales basándonos en lo que los datos pueden proveernos.
    ''')
