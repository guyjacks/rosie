fsm.one.on('next', 'two').do(count, 2)
fsm.one.on('next').go('two').do(count, 2)
fsm.one.next = 'two', count, 2

state = fsm.one.transition('next')
