import justpy as jp
import sqlite3
import pandas as pd
import parseData
import web

def parse_database():
    print("START")
    base_path = "/home/user1/OU/Semester5/CS4620/FinalProject/WMs/"
    files = (base_path + "awesome/", base_path + "dwm/", base_path + "i3/",
             base_path + "qtile/", base_path + "spectrwm/", base_path + "stumpwm/",
             base_path + "xmonad/")

    parseData.pretty_log(files)
    print("LOGGED")

    base_path = "/home/user1/OU/Semester5/CS4620/FinalProject/Django/GitStalker/"
    files = (base_path + "awesome.txt", base_path + "dwm.txt", base_path + "i3.txt",
             base_path + "qtile.txt", base_path + "spectrwm.txt", base_path + "stumpwm.txt",
             base_path + "xmonad.txt")
    
    parseData.extract_data(files)
    print("EXTRACTED")

    return


# con = sqlite3.connect('wm.db')

# tables = {}
# table_names = ['commits', 'repo', 'user', 'works_on']
# for table_name in table_names:
#     tables[table_name] = pd.read_sql_query(f'SELECT * FROM {table_name}', con)


# def selected_event(self, msg):
#     # Runs when a table name is selected
#     # Create a new grid and use its column and row definitions for grid already on page
#     new_grid = tables[msg.value].jp.ag_grid(temp=True)
#     msg.page.g.options.columnDefs = new_grid.options.columnDefs
#     msg.page.g.options.rowData = new_grid.options.rowData
#     # return


# def main(request):
#     wp = jp.QuasarPage()
#     table_name = request.query_params.get('table', 'commits')
#     s = jp.QSelect(options=table_names, a=wp, label="Select Table", outlined=True,
#                    input=selected_event, style='width: 350px; margin: 0.25rem; padding: 0.25rem;', value=table_name)
#     g = tables[table_name].jp.ag_grid(a=wp, style='height: 90vh; width: 99%; margin: 0.25rem; padding: 0.25rem;')
#     # g.options.pagination = True
#     # g.options.paginationAutoPageSize = True
#     wp.g = g
#     return wp    

# if __name__ == "__main__":
#     jp.justpy(main)
    
print("COMPLETE")
