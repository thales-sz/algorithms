def study_schedule(permanence_period, target_time):
    counter = 0
    if target_time == 0 or target_time is not None:
        for enter, out in permanence_period:
            if type(enter) == int and type(out) == int:
                if enter <= target_time <= out:
                    counter += 1
            else:
                return None
        return counter
    else:
        return None
