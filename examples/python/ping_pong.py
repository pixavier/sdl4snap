
import sdl
import time


def anim_to(param):
    print(param)


def sdl_logic (to, state, signal, sender, param, time): 

    self = to
    match to:
        case "Env":
            match state:
                case '':   # start
                    sdl.send(self, 'mStart', 'pPing', '', 0)
                    sdl.set_state(self, 'idle')

        case "pPing":
            match state:
                case '':    # start
                    sdl.set_state(self, 'idle')
                case 'idle':
                    match signal:
                        case 'mStart':
                            sdl.send(self, 'mPing', 'pPong', '', 0)
                            sdl.set_state(self, 'running')
                case 'running':
                    match signal:
                        case 'mPong':
                            anim_to("pPong")
                            sdl.send(self, 'tWait', self, '', 1)
                            sdl.set_state(self, 'running')
                        case 'mStop':
                            sdl.set_state(self, 'idle')
                        case 'tWait':
                            sdl.send(self, 'mPing', 'pPong', '', 0)
                            sdl.set_state(self, 'running')

        case "pPong":
            match state:
                case '':    # start
                    sdl.set_state(self, 'idle')
                case 'idle':
                    match signal:
                        case 'mPing':
                            anim_to("pPing")
                            sdl.send(self, 'mPong', sender, '', 1)
                            sdl.set_state(self, 'idle')


def monitor():
    print(f'SDL time = {sdl.t}')
    print(f"SDL agents/states = {sdl.get_agents()}")
    print(f'SDL look ahead: {sdl.look_ahead()}')
    print(f'SDL next event time = {sdl.next_event_time()}')


def main():
    init_agents = {
        "Env": {"state":""},
        "pPing": {"state":""},
        "pPong": {"state":""}
    }

    sdl.init(sdl_logic, init_agents)
    monitor()
    while True:
        print('--------------')
        sdl.tick()
        monitor()
        time.sleep(sdl.next_event_time() - sdl.t)

main()

