def change_system_mode(mode, enable):
    if mode not in ["night", "away"]: 
        return {"status": "error", "message": "Invalid mode"} 
    return {"status": "ok", "mode": mode, "active": enable} 



