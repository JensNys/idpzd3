from idp_engine import Theory, IDP
from idp_engine.Run import model_expand, pretty_print
import json


def to_dictionary(structure,assignments):
    d3_dict = {}

    svg_entry = {"width":int(assignments['d3_width()'].value.number),"height":int(assignments['d3_height()'].value.number)}
    d3_dict['svg'] = svg_entry
    d3_dict['circles']=[]
    d3_dict['links']=[]
    keys = structure.interpretations['key'].enumeration.tuples;

    for key in keys:
        match assignments["d3_type("+key.code+")"].value.name:
            case "circ":
                circle_entry = {}
                circle_entry["id"] = int(key.code)
                circle_entry["cx"] = int(assignments["d3_x("+key.code+")"].value.number)
                circle_entry["cy"] = int(assignments["d3_y("+key.code+")"].value.number)
                circle_entry["r"] = int(assignments["d3_circ_r("+key.code+")"].value.number)

                print(circle_entry)
                d3_dict['circles'].append(circle_entry)
            case "link":
                link_entry = {}
                link_entry["id"] = int(key.code)
                link_entry["from"] = int(assignments["d3_link_from(" + key.code + ")"].value.number)
                link_entry["to"] = int(assignments["d3_link_to(" + key.code + ")"].value.number)


                d3_dict['links'].append(link_entry)


    return d3_dict

def make_json(structure,assignments):
    d3_dict = to_dictionary(structure,assignments)
    return json.dumps(d3_dict)






print("imports finished")

Kb = IDP.from_file('idp_files/old_api.idp')
T_draw,V_draw,S_draw = Kb.get_blocks("T_draw,V_draw,S_draw")

# mx = model_expand(T_draw, S_draw)
# for m in mx:
#     print(m)
#
print("make theory")
theory = Theory(T_draw,S_draw)
print("loop")
for model in theory.expand(1):
    result = make_json(S_draw, model)


    with open("out/visualisation.json", "w") as f:
      f.write(result)
    with open("out/visualisation.json") as f:
      print(f.read())

# run http server http-server &
# run firefox http:localhost:8080/index.html