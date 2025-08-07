from idp_engine import Theory, IDP
from idp_engine.Run import model_expand, pretty_print

Kb = IDP.from_file('Shape_type.idp')
T_draw,V_draw,S_draw = Kb.get_blocks("T_draw,V_draw,S_draw")

pretty_print(model_expand(T_draw, S_draw))

theory = Theory(T_draw,S_draw)
for model in theory.expand(1):
    i=0

# for model in model_expand(T_draw,S_draw):
#     breakpoint()
