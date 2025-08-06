from idp_engine import Theory, IDP
from idp_engine.Run import model_expand, pretty_print

Kb = IDP.from_file('graph_test.idp')
T, S, V, V_draw = Kb.get_blocks("T, S, V, V_draw")

pretty_print(model_expand(T, S))

theory = Theory(T,S)
for model in theory.expand(1):
    i=0

# for model in model_expand(T,S):
#     breakpoint()
