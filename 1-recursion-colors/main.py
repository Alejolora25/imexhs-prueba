from typing import List, Tuple, Union, Set

Disk = Tuple[int, str]
Move = Tuple[int, str, str]
State = Tuple[Tuple[Disk, ...], ...]

def solve_recursive(
    state: State,
    goal: State,
    visited: Set[State],
    rod_names: List[str],
    path: List[Move],
    depth: int
) -> Union[List[Move], None]:
    
    if state == goal:
        return path
    
    if depth <= 0:
        return None
    
    # Generar movimientos válidos
    for i in range(3):
        if not state[i]:
            continue
        disk = state[i][-1]
        for j in range(3):
            if i == j:
                continue
            # Verificar reglas
            if state[j]:
                top_j = state[j][-1]
                if disk[0] > top_j[0] or disk[1] == top_j[1]:
                    continue
            
            # Crear nuevo estado
            new_rods = [list(r) for r in state]
            moved_disk = new_rods[i].pop()
            new_rods[j].append(moved_disk)
            new_state = tuple(tuple(r) for r in new_rods)
            
            if new_state in visited:
                continue
                
            visited.add(new_state)
            new_path = path + [(disk[0], rod_names[i], rod_names[j])]
            
            # Llamada recursiva clave
            result = solve_recursive(
                new_state,
                goal,
                visited,
                rod_names,
                new_path,
                depth - 1
            )
            
            if result is not None:
                return result
                
            visited.remove(new_state)
    
    return None

def tower_of_hanoi_with_colors(n: int, disks: List[Disk]) -> Union[List[Move], int]:
    rod_names = ['A', 'B', 'C']
    start = (tuple(disks), (), ())
    goal = ((), (), tuple(disks))
    visited = {start}
    
    # Búsqueda recursiva con profundidad incremental
    max_moves = 3**n  # Límite superior razonable
    result = None
    
    for depth in range(n*2, max_moves+1):
        result = solve_recursive(
            start,
            goal,
            visited,
            rod_names,
            [],
            depth
        )
        if result is not None:
            return result
    
    return -1
