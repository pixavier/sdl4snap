
agents = {}
eque = list()
t = 0

def init(event_processor, init_agents):
    global process_event, eque, agents, t
    process_event = event_processor
    agents = init_agents
    eque.clear()
    t = 0
    for key, value in agents.items():
        send(sender = '', signal = '', to = key, param = '', delay = 0)    # force start
    print('--- sdl.init() done ---')


def send (sender, signal, to, param, delay):
    global t
    eque.append({'signal': signal, 'from': sender, 'to': to, 'param': param, 't': t + delay})
    eque.sort(key = lambda msg: msg['t'])


def get_state(agent):
    return agents[agent]['state']


def set_state(agent, state):
    global agents
    agents[agent]["state"] = state


def get_agents():
    return agents


def look_ahead():
    return eque


def next_event_time():
    nt = 999999
    if (len(eque) > 0):
        nt = eque[0]['t']

    return nt

        
def tick(): 
    global agents, eque, t

    if (len(eque) > 0): 
        msg = eque.pop(0)
        t = msg['t']
        process_event(msg['to'], agents[msg['to']]['state'], msg['signal'], msg['from'], msg['param'], t)
        return True
    else:
        print ('Empty event queue')
        return False
        


