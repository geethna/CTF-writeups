import sys
import angr
import claripy

p = angr.Project('./angrybird')
simgr = p.factory.simulation_manager(p.factory.full_init_state())
simgr.explore(find=0x404fda,avoid=0x404f97)
print simgr.found[0].posix.dumps(0)
