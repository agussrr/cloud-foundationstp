# Imports
import pandas as pd
import sqlalchemy
import psycopg2

#Tabla Colors
# Crear una lista con el nombre de las columnas de cada una de las tablas
columns_c = [
    "id",
    "name",
    "rgb",
    "is_trans"
]

# Crear el dataframe
df = pd.read_csv(
    "colors.csv",
    skiprows= 3,
    header =None
)

# Instanceo sqlachemy.create_engine object
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db1:5432/postgres')

# Guardar los datos del dataframe a la tabla creada en postgres
for df in pd.read_csv("colors.csv",skiprows=3,names=columns_c,chunksize=1000):
  df.to_sql(
    'colors', 
    engine,
    index=False,
    if_exists='append'
  )

# Tabla Inventories
# Crear una lista con el nombre de las columnas de cada una de las tablas
columns_i = [
    "id",
    "version",
    "set_num",
]

# Crear el dataframe
df= pd.read_csv(
    "inventories.csv",
    skiprows= 1,
    header =None
)

# Instanceo el objeto sqlachemy.create_engine
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db1:5432/postgres')

for df in pd.read_csv("inventories.csv",skiprows=1,names=columns_i,chunksize=1000):
  df.to_sql(
    'inventories', 
    engine,
    index=False,
    if_exists='append'
  )
# Tabla Themes
# Crear una lista con el nombre de las columnas de cada una de las tablas
columns_t = [
    "id",
    "name",
    "parent_id",
]

# Crear el dataframe
df = pd.read_csv(
    "themes.csv",
    skiprows= 1,
    header =None
)

# Instanceo el objeto sqlachemy.create_engine
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db1:5432/postgres')

for df in pd.read_csv("themes.csv",skiprows=1,names=columns_t,chunksize=1000):
  df.to_sql(
    'themes', 
    engine,
    index=False,
    if_exists='append'
  )

# Tabla Sets
# Crear una lista con el nombre de las columnas de cada una de las tablas
columns_s = [
    "set_num",
    "name",
    "year",
    "theme_id",
    "num_parts"
]

# Crear el dataframe
df = pd.read_csv(
    "sets.csv",
    skiprows= 1,
    header =None
)

# Instanceo el objeto sqlachemy.create_engine
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db1:5432/postgres')

for df in pd.read_csv("sets.csv",skiprows=1,names=columns_s,chunksize=1000):
  df.to_sql(
    'sets', 
    engine,
    index=False,
    if_exists='append'
  )

# Tabla Parts
# Crear una lista con el nombre de las columnas de cada una de las tablas
columns_p = [
    "part_num",
    "name",
    "part_cat_id",
]

# Crear el dataframe
df = pd.read_csv(
    "parts.csv",
    skiprows= 1,
    header =None
)

# Instanceo el objeto sqlachemy.create_engine
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db1:5432/postgres')

for df in pd.read_csv("parts.csv",skiprows=1,names=columns_p,chunksize=1000):
  df.to_sql(
    'parts', 
    engine,
    index=False,
    if_exists='append'
  )

  # Tabla Parts Categories
# Crear una lista con el nombre de las columnas de cada una de las tablas
columns= [
    "id",
    "name"
]

# Crear el dataframe
df = pd.read_csv(
    "part_categories.csv",
    skiprows= 1,
    header =None
)

# Instanceo el objeto sqlachemy.create_engine
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db1:5432/postgres')

for df in pd.read_csv("part_categories.csv",skiprows=1,names=columns,chunksize=1000):
  df.to_sql(
    'part_categories', 
    engine,
    index=False,
    if_exists='append'
  )

# Tabla Inventory Sets
# Crear una lista con el nombre de las columnas de cada una de las tablas
columns_is = [
    "inventory_id",
    "set_num",
    "quantity"
]

# Crear el dataframe
df_is = pd.read_csv(
    "inventory_sets.csv",
    skiprows= 1,
    names = columns_is,
    header = None
)

#df_is = df_is.drop_duplicates(subset= ["inventory_id"])

# Instanceo el objeto sqlachemy.create_engine
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db1:5432/postgres')
  
df_is.drop_duplicates(subset= ['inventory_id']).to_sql('inventory_sets', engine, index=False, if_exists='append')

# Tabla Inventory Parts
# Crear una lista con el nombre de las columnas de cada una de las tablas
columns_ip = [
    "inventory_id",
    "part_num",
    "color_id",
    "quantity",
    "is_spare"
]

# Crear el dataframe
df_ip = pd.read_csv(
    "inventory_parts.csv",
    skiprows= 1,
    names = columns_ip,
    header = None
)

# Instanceo el objeto sqlachemy.create_engine
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db1:5432/postgres')
  
df_ip.drop_duplicates(subset= ['inventory_id']).to_sql('inventory_parts', engine, index=False, if_exists='append')
