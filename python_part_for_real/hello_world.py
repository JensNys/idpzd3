from idp_engine import Theory, IDP
from idp_engine.Run import model_expand, pretty_print
import json
import os
import time
"""
function that returns the elements that are in the assignments that starts



examples: if there is a set in the vocabulary my_set = {A,B,C} then assignments contains my_set(A),my_set(B),my_set(C)
this function returns ['A','B','C']

"""
def get_set_from_assignment(set_name,assignments):
    result = []
    for element in assignments:
        if element.startswith(set_name+"(") and assignments[element].value.code == 'true':
            result.append(element.replace(set_name,"").replace("(","").replace(")",""))
    return result

def to_dictionary(structure,assignments):
    d3_dict = {}

    svg_entry = {"width":int(assignments['d3_width()'].value.number),"height":int(assignments['d3_height()'].value.number)}
    d3_dict['svg'] = svg_entry
    d3_dict['circles']=[]
    d3_dict['links']=[]
    d3_dict['rects']=[]

    valid_keys = get_set_from_assignment("dom_d3_type",assignments)
    print(valid_keys)

    
    for key in valid_keys:
        match assignments["d3_type("+key+")"].value.name:
            case "circ":
                circle_entry = {}
                circle_entry["id"] = int(key)
                circle_entry["cx"] = int(assignments["d3_x("+key+")"].value.number)
                circle_entry["cy"] = int(assignments["d3_y("+key+")"].value.number)
                circle_entry["r"] = int(assignments["d3_circ_r("+key+")"].value.number)
                circle_entry["color"] = assignments["d3_color("+key+")"].value.code

                d3_dict['circles'].append(circle_entry)
            case "link":
                link_entry = {}
                link_entry["id"] = int(key)
                link_entry["from"] = int(assignments["d3_link_from(" + key + ")"].value.number)
                link_entry["to"] = int(assignments["d3_link_to(" + key + ")"].value.number)
                link_entry["color"] = assignments["d3_color("+key+")"].value.code

                d3_dict['links'].append(link_entry)
            case "rect":
                rect_entry = {}
                rect_entry["id"] = int(key)
                rect_entry["x"] = int(assignments["d3_x("+key+")"].value.number)
                rect_entry["y"] = int(assignments["d3_y("+key+")"].value.number)
                rect_entry["width"] = int(assignments["d3_rect_width("+key+")"].value.number)
                rect_entry["height"] = int(assignments["d3_rect_height("+key+")"].value.number)
                rect_entry["color"] = assignments["d3_color("+key+")"].value.code
                d3_dict['rects'].append(rect_entry)


    return d3_dict

def make_json(structure,assignments):
    d3_dict = to_dictionary(structure,assignments)
    return json.dumps(d3_dict)

def show_file():
    port = "8085"
    # Start the server in the background and capture its PID
    os.system(f"python3 -m http.server {port} & echo $! > server_pid.txt")
    # Give it a moment to start
    time.sleep(1)
    # Open Firefox to the html
    os.system(f"firefox http://localhost:{port}/out/index.html &")
    # Let the server run for 10 seconds
    time.sleep(2)
    # Kill the server
    with open("server_pid.txt") as f:
        pid = f.read().strip()
    os.system(f"kill {pid}")
    os.remove("server_pid.txt")


print("imports finished")

Kb = IDP.from_file('idp_files/old_api_combined.idp')
T_draw,V_draw,S_draw = Kb.get_blocks("T_draw,V_draw,S_draw")

# mx = model_expand(T_draw, S_draw)
# for m in mx:
#     print(m)
#

print("make theory")
theory = Theory(T_draw,S_draw)
print("loop")
for model in theory.expand(1):
    print(model)
    result = make_json(S_draw, model)


    with open("out/visualisation.json", "w") as f:
      f.write(result)
    with open("out/visualisation.json") as f:
      print(f.read())
    print("succesfully written")
    show_file()





# run http server http-server &
# run firefox http:localhost:8080/index.html

