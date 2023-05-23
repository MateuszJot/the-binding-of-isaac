class Scene:
    def __init__(self):
        self._actors = []
        self._time = 0

    def add_actor(self, actor):
        if actor not in self._actors:
            self._actors.append(actor)

    def render(self, window):
        window.fill((0, 0, 0))
        for actor in self._actors:
            actor.render(window)

    def update(self, delta_time):
        for actor in self._actors:
            actor.on_update(delta_time)
