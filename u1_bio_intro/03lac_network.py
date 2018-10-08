def lacI_bound(lactose, lacI):
    return lacI and not lactose
    
def CAP_bound(glucose, CAP):
    return CAP and not glucose

def lacZ(is_lacI_bound, is_CAP_bound):
    if is_lacI_bound: return "absent"
    elif is_CAP_bound: return "high"
    else: return "low"
    
def lacZ_full_circuit(lactose, lacI, glucose, CAP):
    is_lacI_bound = lacI_bound(lactose, lacI)
    is_CAP_bound = CAP_bound(glucose, CAP)
    return lacZ(is_lacI_bound, is_CAP_bound)