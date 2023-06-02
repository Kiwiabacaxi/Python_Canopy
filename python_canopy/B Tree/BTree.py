from typing import List, Optional
from dataclasses import dataclass

@dataclass
class Node:
    keys: List[int]
    children: List['Node']
    leaf: bool
    
@dataclass
class BTree:
    order: int
    root: Node
    
