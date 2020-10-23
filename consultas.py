import pandas as pd
import psycopg2
import time
import sqlalchemy

time.sleep(120)

consultas_dict =[{'reporte':'SELECT c.id, c.name, t.id, t.name FROM colors as c INNER JOIN inventory_parts as ip ON c.id = ip.color_id INNER JOIN inventories as i ON i.id = ip.inventory_id INNER JOIN sets as s ON s.set_num = i.set_num INNER JOIN themes as t ON t.id = s.theme_id LIMIT 10 ', 'guardo':'/Users/Agustin/Documents/Cloud/color_theme_rel.csv'},
                  {'reporte' : 'SELECT parent_id, COUNT(parent_id) as parent_total  FROM themes GROUP BY parent_id ORDER BY parent_total DESC LIMIT 10','guardo':'/Users/Agustin/Documents/Cloud/parentchildrenthem.csv'},
                  {'reporte' : 'SELECT s.theme_id, t.name, COUNT(set_num) as total_sets FROM sets as s INNER JOIN themes as t ON s.theme_id = t.id  GROUP BY s.theme_id, t.name ORDER BY total_sets DESC', 'guardo':'/Users/Agustin/Documents/Cloud/themesets.csv'},
                  {'reporte' : 'SELECT year, COUNT(*) FROM sets GROUP BY year  ORDER BY year ASC','guardo':'/Users/Agustin/Documents/Cloud/yearsets.csv'},
                  {'reporte' : 'SELECT p.part_cat_id, pc.name, COUNT(p.part_cat_id) as total_parts FROM parts as p INNER JOIN part_categories as pc ON p.part_cat_id = pc.id  GROUP BY p.part_cat_id, pc.name  ORDER BY total_parts DESC ','guardo':'/Users/Agustin/Documents/Cloud/parts_cat.csv'}]


if __name__ == "__main__": 

    engine = sqlalchemy.create_engine('postgresql://postgres:postgres@db1:5432/postgres')
    
    for c in consultas_dict:

        consulta = c['reporte']
        archivo = c['guardo']
        
        pd.read_sql(consulta, con=engine).to_csv(archivo, index=False)
    
    engine.dispose()