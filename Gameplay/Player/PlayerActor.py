from Core.Actors.Actor import Actor
from Core.SpriteAnimation import SpriteAnimation
from Core.ResourceLoader import ResourceLoader


class PlayerActor(Actor):
    def __init__(self, position, rotation, scale):
        self._idle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/Idle"))
        self._walk_up_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkUp"))
        self._walk_down_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkDown"))
        self._walk_left_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkLeft"))
        self._walk_right_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkRight"))
        self._walk_left_up_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkLeftUp"))
        self._walk_right_up_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkRightUp"))
        self._walk_left_down_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkLeftDown"))
        self._walk_right_down_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkRightDown"))

        super().__init__(position, rotation, scale, None)

    def get_sprite(self):
        return self._idle_animation[0]
