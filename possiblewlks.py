from bridges import BRIDGES

def get_walks_starting_from(area, bridges=BRIDGES):
    walks = []

    def make_walks(area, walked=None, bridges_crossed=None):
        if walked is None:
            walked = (area,)  # Use a tuple to store the walked path
        if bridges_crossed is None:
            bridges_crossed = tuple()  # Use a tuple to store crossed bridges

        # Get all of the bridges connected to area that haven't been crossed
        available_bridges = [
            bridge
            for bridge in bridges
            if area in bridge and bridge not in bridges_crossed
        ]

        # Determine if the walk has ended
        if not available_bridges:
            walks.append(walked)
            return

        # Walk the bridge to the adjacent area and recurse 
        for bridge in available_bridges:
            crossing = bridge if bridge[0] == area else bridge[::-1]
            make_walks(
                area=crossing[-1],
                walked=walked + crossing,
                bridges_crossed=bridges_crossed + (bridge,),
            )

    make_walks(area)
    return walks
