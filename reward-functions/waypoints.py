# Racing line using Waypoints
def reward_function(params):
    left = [*insert_waypoints*]
    centerleft = [*insert_waypoints*]
    centerright = [*insert_waypoints*]
    right = [*insert_waypoints*]
    
    fast = [*insert_waypoints*]
    medium = [*insert_waypoints*]
    slow = [*insert_waypoints*]

    closest = params['closest_waypoints']
    nextwaypoint = max(closest[0], closest[1])

    if params['all_wheels_on_track'] == True:
        if (nextwaypoint in centerleft):
            if (params['distance_from_center']/params['track_width'])<=0.25 and (params['is_left_of_center']):
                reward = 14
            elif (params['distance_from_center']/params['track_width'])<=0.25 and (not params['is_left_of_center']):
                reward = 0
            else:
                reward = -7
                
        elif (nextwaypoint in centerright):
            if (params['distance_from_center']/params['track_width'])<=0.25 and (not params['is_left_of_center']):
                reward = 14
            elif (params['distance_from_center']/params['track_width'])<=0.25 and (params['is_left_of_center']):
                reward = 0
            else:
                reward = -7

        elif (nextwaypoint in left):
            if (params['is_left_of_center']) and (params['distance_from_center']/params['track_width'])>0.25 and    (params['distance_from_center']/params['track_width'])<0.48:
                reward = 14
            else:
                reward = -7
        elif (nextwaypoint in right):
            if (not params['is_left_of_center']) and (params['distance_from_center']/params['track_width'])>0.25 and(params['distance_from_center']/params['track_width'])<0.48:
                reward = 14
            else:
                reward = -7

        if nextwaypoint in fast:
            if params['speed'] == 3:
                reward += 14
            else:
                reward -= (5-params['speed'])**2
        elif nextwaypoint in medium:
            if params['speed'] == 2:
                reward += 14
            else:
                reward -= 7
        elif nextwaypoint in slow:
            if params['speed'] == 1:
                reward += 14
            else:
                reward -= (2+params['speed'])**2
                
    else:
        reward = 0.001
    
    return float(reward)

