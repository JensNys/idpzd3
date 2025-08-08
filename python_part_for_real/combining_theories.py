

from idp_engine import Theory, IDP


idp_file = "idp_files/combine_theories.idp"
Kb = IDP.from_file(idp_file)

T,V,S = Kb.get_blocks("T_draw,V_draw,S_draw")
T_draw,V_combined,S_draw = Kb.get_blocks("T_draw,V_combined,S_draw")

pureTheory = Theory(T,S)
print(pureTheory)
visTheory = Theory(T_draw,S_draw)
print(visTheory)

combinedTheory = pureTheory.add(visTheory)
print(combinedTheory)

















