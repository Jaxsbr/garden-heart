from dataclasses import dataclass, field

from core.components.component import Component
from core.components.living_entity_component import LivingEntityComponent


@dataclass
class EnemyAIComponent(Component):
    has_attack_target: bool | None = field(default=False)
