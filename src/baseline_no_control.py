def run(trucks):
    """Returns {truck_id: slot}. No scheduling: truck passes when it wants."""
    return {t.id: t.preferred for t in trucks}